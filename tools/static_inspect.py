from pathlib import Path
import hashlib,re,sys
root=Path(sys.argv[1] if len(sys.argv)>1 else '.').resolve()
patterns={'秘密情報らしき文字列':re.compile(r'(api[_-]?key|secret|token|password)',re.I),'危険なシェル操作':re.compile(r'(curl.+\|\s*(sh|bash)|wget.+\|\s*(sh|bash)|rm\s+-rf|sudo\s+)',re.I),'Docker高権限':re.compile(r'(privileged:\s*true|/var/run/docker\.sock)',re.I)}
interesting={'Dockerfile','docker-compose.yml','compose.yml','package.json','pyproject.toml','requirements.txt','Cargo.toml','go.mod','Makefile','LICENSE','SECURITY.md'}
print(f'# Static inspection: {root.name}\n\n注意: 文字列ベースの一次調査で、安全性を保証しません。\n\n## 主要ファイル')
for p in sorted(root.rglob('*')):
    if p.is_file() and (p.name in interesting or p.name.lower().startswith('readme')):print(f'- {p.relative_to(root)}')
print('\n## 検出事項'); found=False
for p in sorted(root.rglob('*')):
    if not p.is_file() or '.git' in p.parts or p.stat().st_size>1000000:continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    for label,pat in patterns.items():
        for m in list(pat.finditer(text))[:5]:
            found=True; line=text.count('\n',0,m.start())+1; print(f'- **{label}**: `{p.relative_to(root)}:{line}` — `{m.group(0)[:100]}`')
if not found:print('- 単純パターン検査では該当なし')
print('\n## 主要ファイルSHA-256')
for p in sorted(root.rglob('*')):
    if p.is_file() and p.name in interesting:print(f'- `{p.relative_to(root)}`: `{hashlib.sha256(p.read_bytes()).hexdigest()}`')
