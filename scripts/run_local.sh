#!/usr/bin/env bash
set -euo pipefail
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python src/build.py
python -m http.server 8000 --directory site
