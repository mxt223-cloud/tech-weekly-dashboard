from __future__ import annotations
import json, os, re, shutil
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin
from zoneinfo import ZoneInfo
import feedparser, requests
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, select_autoescape
ROOT=Path(__file__).resolve().parents[1]
CONFIG=json.loads((ROOT/'config.json').read_text(encoding='utf-8'))
OUT,REPORTS=ROOT/'site',ROOT/'reports'
TIMEOUT=20
HEADERS={'User-Agent':'tech-weekly-dashboard/1.0','Accept-Language':'en-US,en;q=0.9,ja;q=0.8'}
@dataclass
class TrendingRepo:
    rank:int; full_name:str; url:str; description:str; language:str
    stars_total:int|None; forks_total:int|None; stars_period:int|None; api:dict[str,Any]
def number(text:str)->int|None:
    m=re.search(r'(\d+(?:\.\d+)?)\s*([kKmM])?',text.strip().replace(',',''))
    if not m:return None
    n=float(m.group(1)); s=(m.group(2)or'').lower()
    return int(n*(1000 if s=='k' else 1000000 if s=='m' else 1))
def gh_headers():
    h={'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28',**HEADERS}
    if os.getenv('GITHUB_TOKEN'): h['Authorization']=f"Bearer {os.environ['GITHUB_TOKEN']}"
    return h
def repo_api(name):
    r=requests.get(f'https://api.github.com/repos/{name}',headers=gh_headers(),timeout=TIMEOUT)
    if r.status_code!=200:return {'error':f'HTTP {r.status_code}'}
    d=r.json(); return {'default_branch':d.get('default_branch'),'license':(d.get('license')or{}).get('spdx_id'),'updated_at':d.get('updated_at'),'pushed_at':d.get('pushed_at'),'open_issues':d.get('open_issues_count'),'archived':d.get('archived'),'size_kb':d.get('size'),'topics':d.get('topics',[])}
def github_trending():
    lang=CONFIG.get('github_trending_language','').strip('/'); since=CONFIG.get('github_trending_since','weekly'); limit=int(CONFIG.get('github_limit',10))
    url='https://github.com/trending'+(f'/{lang}' if lang else '')
    r=requests.get(url,params={'since':since},headers=HEADERS,timeout=TIMEOUT); r.raise_for_status()
    soup=BeautifulSoup(r.text,'html.parser'); out=[]
    for row in soup.select('article.Box-row')[:limit]:
        a=row.select_one('h2 a')
        if not a:continue
        name=re.sub(r'\s+','',a.get_text(' ',strip=True)); links=row.select('a.Link--muted'); period=row.select_one('span.d-inline-block.float-sm-right')
        desc=row.select_one('p'); langel=row.select_one("[itemprop='programmingLanguage']")
        out.append(TrendingRepo(len(out)+1,name,urljoin('https://github.com',a.get('href','')),desc.get_text(' ',strip=True) if desc else '',langel.get_text(strip=True) if langel else '不明',number(links[0].get_text(' ',strip=True)) if len(links)>0 else None,number(links[1].get_text(' ',strip=True)) if len(links)>1 else None,number(period.get_text(' ',strip=True)) if period else None,repo_api(name)))
    if not out:raise RuntimeError('GitHub TrendingのHTML構造を解析できませんでした。selector更新が必要です。')
    return out
def zenn_feed():
    p=feedparser.parse(CONFIG.get('zenn_feed','https://zenn.dev/feed'))
    if getattr(p,'bozo',False) and not p.entries:raise RuntimeError(f'Zenn RSS取得失敗: {p.bozo_exception}')
    out=[]
    for e in p.entries[:int(CONFIG.get('zenn_limit',20))]:
        summary=BeautifulSoup(e.get('summary',''),'html.parser').get_text(' ',strip=True)
        out.append({'title':e.get('title',''),'url':e.get('link',''),'author':e.get('author',''),'published':e.get('published',''),'summary':summary[:240]})
    return out
def terms(repos,zenn):
    stop={'with','from','that','this','your','into','using','open','source','github','zenn','ため','する','して','ます','から','こと','これ','the','and','for','you','are','not','app','tool'}
    a=' '.join(f"{r.full_name} {r.description} {' '.join(r.api.get('topics',[]))}" for r in repos).lower(); b=' '.join(f"{x['title']} {x['summary']}" for x in zenn).lower()
    tok=lambda s:{t for t in re.findall(r'[a-zA-Z][a-zA-Z0-9.+#-]{2,}|[一-龥ァ-ヶー]{2,}',s) if t not in stop}
    return sorted(tok(a)&tok(b),key=lambda t:a.count(t)+b.count(t),reverse=True)[:12]
def main():
    repos,zenn=github_trending(),zenn_feed(); now=datetime.now(ZoneInfo(CONFIG.get('timezone','Asia/Tokyo'))); week=now.strftime('%Y-%m-%d')
    data={'generated_at':now.isoformat(),'week':week,'title':CONFIG.get('site_title','Tech Weekly'),'github':[asdict(r) for r in repos],'zenn':zenn,'common_terms':terms(repos,zenn),'verification':{'mode':'metadata-only','completed':0,'pending':len(repos),'note':'自動収集ではコードを実行しません。'}}
    (OUT/'data').mkdir(parents=True,exist_ok=True); REPORTS.mkdir(parents=True,exist_ok=True)
    text=json.dumps(data,ensure_ascii=False,indent=2)
    for p in [OUT/'data/latest.json',REPORTS/f'{week}.json',REPORTS/'latest.json']:p.write_text(text,encoding='utf-8')
    env=Environment(loader=FileSystemLoader(ROOT/'templates'),autoescape=select_autoescape(['html','xml']))
    (OUT/'index.html').write_text(env.get_template('index.html.j2').render(data=data),encoding='utf-8')
    md=env.get_template('report.md.j2').render(data=data)
    for p in [REPORTS/f'{week}.md',REPORTS/'latest.md']:p.write_text(md,encoding='utf-8')
    for n in ['manifest.webmanifest','sw.js','icon.svg']:shutil.copy2(ROOT/'static'/n,OUT/n)
    print(f'Generated {len(repos)} repos and {len(zenn)} Zenn items')
if __name__=='__main__':main()
