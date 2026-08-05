$ErrorActionPreference = "Stop"
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\build.py
.\.venv\Scripts\python.exe -m http.server 8000 --directory site
