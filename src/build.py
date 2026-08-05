from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import shutil
import time
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from zoneinfo import ZoneInfo

import feedparser
import requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
OUT = ROOT / "site"
REPORTS = ROOT / "reports"
CACHE = ROOT / "cache" / "ai-analysis"
TIMEOUT = 30
HEADERS = {
    "User-Agent": "tech-weekly-dashboard/2.0",
    "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
}


@dataclass
class TrendingRepo:
    rank: int
    full_name: str
    url: str
    description: str
    language: str
    stars_total: int | None
    forks_total: int | None
    stars_period: int | None
    api: dict[str, Any]
    readme: dict[str, Any]
    analysis: dict[str, Any]


def number(text: str) -> int | None:
    match = re.search(r"(\d+(?:\.\d+)?)\s*([kKmM])?", text.strip().replace(",", ""))
    if not match:
        return None
    value = float(match.group(1))
    suffix = (match.group(2) or "").lower()
    return int(value * (1_000 if suffix == "k" else 1_000_000 if suffix == "m" else 1))


def gh_headers(raw: bool = False) -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github.raw+json" if raw else "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        **HEADERS,
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def get_json(url: str, headers: dict[str, str], attempts: int = 3) -> requests.Response:
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            response = requests.get(url, headers=headers, timeout=TIMEOUT)
            if response.status_code < 500 and response.status_code != 429:
                return response
            last_error = RuntimeError(f"HTTP {response.status_code}: {url}")
        except requests.RequestException as exc:
            last_error = exc
        time.sleep(2**attempt)
    raise RuntimeError(str(last_error or f"Request failed: {url}"))


def repo_api(name: str) -> dict[str, Any]:
    response = get_json(f"https://api.github.com/repos/{name}", gh_headers())
    if response.status_code != 200:
        return {"error": f"HTTP {response.status_code}"}
    data = response.json()
    return {
        "default_branch": data.get("default_branch"),
        "license": (data.get("license") or {}).get("spdx_id"),
        "updated_at": data.get("updated_at"),
        "pushed_at": data.get("pushed_at"),
        "open_issues": data.get("open_issues_count"),
        "archived": data.get("archived"),
        "size_kb": data.get("size"),
        "topics": data.get("topics", []),
    }


def fetch_readme(name: str) -> dict[str, Any]:
    url = f"https://api.github.com/repos/{name}/readme"
    response = get_json(url, gh_headers())
    if response.status_code == 404:
        return {"status": "not_found", "text": "", "sha": None, "path": None}
    if response.status_code != 200:
        return {"status": "error", "text": "", "sha": None, "path": None, "error": f"HTTP {response.status_code}"}

    metadata = response.json()
    encoded = metadata.get("content", "")
    try:
        text = base64.b64decode(encoded).decode("utf-8", errors="replace")
    except Exception as exc:
        return {"status": "error", "text": "", "sha": metadata.get("sha"), "path": metadata.get("path"), "error": str(exc)}

    max_chars = int(CONFIG.get("readme_max_chars", 30000))
    prepared = prepare_readme(text, max_chars)
    return {
        "status": "ok",
        "text": prepared,
        "sha": metadata.get("sha"),
        "path": metadata.get("path", "README.md"),
        "truncated": len(text) > len(prepared),
        "original_chars": len(text),
        "used_chars": len(prepared),
    }


def prepare_readme(text: str, max_chars: int) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<img\b[^>]*>", "", text, flags=re.I)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    if len(text) <= max_chars:
        return text

    preferred = {
        "overview", "about", "features", "feature", "use cases", "use case",
        "usage", "quick start", "quickstart", "getting started", "installation",
        "requirements", "examples", "example", "limitations", "security",
    }
    sections = re.split(r"(?m)^(#{1,3}\s+.+)$", text)
    selected: list[str] = [text[:4000]]
    for index in range(1, len(sections) - 1, 2):
        heading = sections[index]
        body = sections[index + 1]
        normalized = re.sub(r"[^a-z ]", "", heading.lower()).strip()
        if any(key in normalized for key in preferred):
            selected.append(f"{heading}\n{body}")
    result = "\n\n".join(selected)
    return result[:max_chars]


def empty_analysis(status: str, note: str, original_description: str = "") -> dict[str, Any]:
    return {
        "status": status,
        "summary_ja": original_description or "日本語分析は未完了です。",
        "capabilities": [],
        "use_cases": [],
        "first_trial": {
            "goal": "未確認",
            "steps": [],
            "success_criteria": "未確認",
        },
        "evidence_sections": [],
        "unconfirmed": [note],
        "model": None,
        "cached": False,
    }


def analysis_schema() -> dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "summary_ja": {"type": "string"},
            "capabilities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "evidence_section": {"type": "string"},
                    },
                    "required": ["text", "evidence_section"],
                },
            },
            "use_cases": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "text": {"type": "string"},
                        "basis": {"type": "string"},
                        "evidence_section": {"type": "string"},
                    },
                    "required": ["text", "basis", "evidence_section"],
                },
            },
            "first_trial": {
                "type": "object",
                "properties": {
                    "goal": {"type": "string"},
                    "steps": {"type": "array", "items": {"type": "string"}},
                    "success_criteria": {"type": "string"},
                },
                "required": ["goal", "steps", "success_criteria"],
            },
            "evidence_sections": {"type": "array", "items": {"type": "string"}},
            "unconfirmed": {"type": "array", "items": {"type": "string"}},
        },
        "required": [
            "summary_ja", "capabilities", "use_cases", "first_trial",
            "evidence_sections", "unconfirmed",
        ],
    }


def analyze_repository(repo: TrendingRepo) -> dict[str, Any]:
    if repo.readme.get("status") != "ok" or not repo.readme.get("text"):
        return empty_analysis("no_readme", "READMEを取得できませんでした。", repo.description)

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return empty_analysis("no_api_key", "GEMINI_API_KEYが設定されていません。", repo.description)

    model = CONFIG.get("gemini_model", "gemini-3.5-flash-lite")
    prompt_version = CONFIG.get("analysis_prompt_version", "v1")
    readme_sha = repo.readme.get("sha") or hashlib.sha256(repo.readme["text"].encode()).hexdigest()
    cache_key = hashlib.sha256(
        f"{repo.full_name}|{readme_sha}|{model}|{prompt_version}".encode()
    ).hexdigest()[:24]
    cache_file = CACHE / f"{repo.full_name.replace('/', '__')}__{cache_key}.json"

    if cache_file.exists():
        cached = json.loads(cache_file.read_text(encoding="utf-8"))
        cached["cached"] = True
        return cached

    prompt = f"""
あなたはGitHubリポジトリのREADMEを根拠に、日本語の技術紹介を作る分析者です。

厳守事項:
- READMEと入力メタデータに書かれていない機能を事実として追加しない。
- 不明な内容は unconfirmed に記載する。
- capabilities は確認できる範囲で最大3件。数合わせで捏造しない。
- use_cases は最大3件。READMEに明示されている場合は basis を「README明記」、機能から直接導ける提案の場合は「提案」とする。
- first_trial はREADMEのQuick Start、Installation、Examplesに沿った最小確認手順。コマンドが確認できない場合は具体的コマンドを創作しない。
- 固有名詞、リポジトリ名、製品名、コマンドは翻訳・改変しない。
- 簡潔で、非専門家にも意味が分かる日本語にする。
- evidence_section にはREADMEの見出し名を書く。見出しを特定できない場合は「README冒頭」とする。

リポジトリ情報:
- 名前: {repo.full_name}
- 説明: {repo.description}
- 主言語: {repo.language}
- Topics: {', '.join(repo.api.get('topics', [])) or 'なし'}
- READMEパス: {repo.readme.get('path') or 'README.md'}

README:
---
{repo.readme['text']}
---
""".strip()

    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
    payload = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.2,
            "responseMimeType": "application/json",
            "responseJsonSchema": analysis_schema(),
        },
    }

    try:
        response = requests.post(
            endpoint,
            params={"key": api_key},
            json=payload,
            headers={"Content-Type": "application/json", **HEADERS},
            timeout=90,
        )
        if response.status_code != 200:
            message = response.text[:500]
            return empty_analysis("api_error", f"Gemini API HTTP {response.status_code}: {message}", repo.description)

        body = response.json()
        candidates = body.get("candidates", [])
        if not candidates:
            return empty_analysis("empty_response", "Geminiから候補が返りませんでした。", repo.description)
        parts = candidates[0].get("content", {}).get("parts", [])
        text = "".join(part.get("text", "") for part in parts)
        result = json.loads(text)
        result["capabilities"] = result.get("capabilities", [])[:3]
        result["use_cases"] = result.get("use_cases", [])[:3]
        result["status"] = "ok"
        result["model"] = model
        result["cached"] = False
        result["readme_sha"] = readme_sha
        result["generated_at"] = datetime.now(ZoneInfo(CONFIG.get("timezone", "Asia/Tokyo"))).isoformat()

        CACHE.mkdir(parents=True, exist_ok=True)
        cache_file.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        return result
    except (requests.RequestException, ValueError, KeyError, TypeError) as exc:
        return empty_analysis("exception", f"AI分析失敗: {exc}", repo.description)


def github_trending() -> list[TrendingRepo]:
    lang = CONFIG.get("github_trending_language", "").strip("/")
    since = CONFIG.get("github_trending_since", "weekly")
    limit = int(CONFIG.get("github_limit", 10))
    url = "https://github.com/trending" + (f"/{lang}" if lang else "")
    response = requests.get(url, params={"since": since}, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    repos: list[TrendingRepo] = []

    for row in soup.select("article.Box-row")[:limit]:
        link = row.select_one("h2 a")
        if not link:
            continue
        name = re.sub(r"\s+", "", link.get_text(" ", strip=True))
        links = row.select("a.Link--muted")
        period = next(
            (span for span in row.find_all("span") if "stars this week" in span.get_text(" ", strip=True).lower()),
            row.select_one("span.d-inline-block.float-sm-right"),
        )
        description = row.select_one("p")
        language = row.select_one("[itemprop='programmingLanguage']")
        api = repo_api(name)
        readme = fetch_readme(name)
        repo = TrendingRepo(
            rank=len(repos) + 1,
            full_name=name,
            url=urljoin("https://github.com", link.get("href", "")),
            description=description.get_text(" ", strip=True) if description else "",
            language=language.get_text(strip=True) if language else "不明",
            stars_total=number(links[0].get_text(" ", strip=True)) if len(links) > 0 else None,
            forks_total=number(links[1].get_text(" ", strip=True)) if len(links) > 1 else None,
            stars_period=number(period.get_text(" ", strip=True)) if period else None,
            api=api,
            readme={key: value for key, value in readme.items() if key != "text"},
            analysis={},
        )
        repo.readme["text"] = readme.get("text", "")
        repo.analysis = analyze_repository(repo)
        repo.readme.pop("text", None)  # 公開JSONへREADME全文を含めない
        repos.append(repo)

    if len(repos) < limit:
        raise RuntimeError(f"GitHub Trendingを{limit}件取得予定でしたが、{len(repos)}件しか解析できませんでした。")
    return repos


def zenn_feed() -> list[dict[str, Any]]:
    parsed = feedparser.parse(CONFIG.get("zenn_feed", "https://zenn.dev/feed"))
    if getattr(parsed, "bozo", False) and not parsed.entries:
        raise RuntimeError(f"Zenn RSS取得失敗: {parsed.bozo_exception}")
    items = []
    for entry in parsed.entries[: int(CONFIG.get("zenn_limit", 20))]:
        summary = BeautifulSoup(entry.get("summary", ""), "html.parser").get_text(" ", strip=True)
        items.append({
            "title": entry.get("title", ""),
            "url": entry.get("link", ""),
            "author": entry.get("author", ""),
            "published": entry.get("published", ""),
            "summary": summary[:240],
        })
    return items


def terms(repos: list[TrendingRepo], zenn: list[dict[str, Any]]) -> list[str]:
    stop = {"with", "from", "that", "this", "your", "into", "using", "open", "source", "github", "zenn", "ため", "する", "して", "ます", "から", "こと", "これ", "the", "and", "for", "you", "are", "not", "app", "tool"}
    repo_text = " ".join(f"{r.full_name} {r.description} {' '.join(r.api.get('topics', []))}" for r in repos).lower()
    zenn_text = " ".join(f"{item['title']} {item['summary']}" for item in zenn).lower()
    tokenize = lambda text: {token for token in re.findall(r"[a-zA-Z][a-zA-Z0-9.+#-]{2,}|[一-龥ァ-ヶー]{2,}", text) if token not in stop}
    return sorted(tokenize(repo_text) & tokenize(zenn_text), key=lambda token: repo_text.count(token) + zenn_text.count(token), reverse=True)[:12]


def main() -> None:
    repos = github_trending()
    zenn = zenn_feed()
    now = datetime.now(ZoneInfo(CONFIG.get("timezone", "Asia/Tokyo")))
    date_id = now.strftime("%Y-%m-%d")
    successful = sum(1 for repo in repos if repo.analysis.get("status") == "ok")
    data = {
        "generated_at": now.isoformat(),
        "week": date_id,
        "title": CONFIG.get("site_title", "Tech Weekly"),
        "github": [asdict(repo) for repo in repos],
        "zenn": zenn,
        "common_terms": terms(repos, zenn),
        "ai_analysis": {
            "enabled": bool(os.getenv("GEMINI_API_KEY")),
            "model": CONFIG.get("gemini_model", "gemini-3.5-flash-lite"),
            "successful": successful,
            "total": len(repos),
        },
        "verification": {
            "mode": "metadata-and-readme-analysis",
            "completed": 0,
            "pending": len(repos),
            "note": "AI分析はREADMEの要約であり、実行検証や安全性保証ではありません。",
        },
    }

    (OUT / "data").mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    serialized = json.dumps(data, ensure_ascii=False, indent=2)
    for path in [OUT / "data/latest.json", REPORTS / f"{date_id}.json", REPORTS / "latest.json"]:
        path.write_text(serialized, encoding="utf-8")

    env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html", "xml"]))
    (OUT / "index.html").write_text(env.get_template("index.html.j2").render(data=data), encoding="utf-8")
    markdown = env.get_template("report.md.j2").render(data=data)
    for path in [REPORTS / f"{date_id}.md", REPORTS / "latest.md"]:
        path.write_text(markdown, encoding="utf-8")
    for name in ["manifest.webmanifest", "sw.js", "icon.svg"]:
        shutil.copy2(ROOT / "static" / name, OUT / name)
    print(f"Generated {len(repos)} repos; AI analysis succeeded for {successful}/{len(repos)}")


if __name__ == "__main__":
    main()
