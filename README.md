# Tech Weekly Dashboard

GitHub Trending週間上位10件とZenn公式RSSを週次取得し、Markdown、JSON、PWA対応ページを生成します。

## 導入
1. このフォルダをGitHubの新規リポジトリへpush。
2. Settings → Pages → Sourceで **GitHub Actions** を選択。
3. Actions → **Weekly Tech Report** を手動実行。以後、毎週月曜07:15 JSTに自動更新。
4. 公開URLをスマホで開き、ホーム画面に追加。

## iPhoneウィジェット
Scriptableへ `widget/Scriptable.js` を貼り付け、先頭の2つのURLを自分のGitHub Pages URLに変更します。

## Android
Chromeで公開URLを開き、メニューから「ホーム画面に追加」または「アプリをインストール」。

## ローカル実行
Windows: `.\scripts\run_local.ps1`
macOS/Linux: `chmod +x scripts/run_local.sh && ./scripts/run_local.sh`

## 上位10件の検証
Actionsの **Inspect Trending Repository** で `owner/repository` と、可能ならcommit SHAを指定します。これはcloneと静的検査のみで、対象コードを実行しません。

Docker検証は静的確認後、対象を `target/` に置いて実行します。
`docker compose -f docker/compose.yml build`
`docker compose -f docker/compose.yml run --rm sandbox`

初期状態はネットワークなし、非root、read-only、capability削除、CPU 1、メモリ1GB、PID 128です。

## 制約
GitHub Trendingには安定性が保証された公式APIがないため、公開HTMLを解析します。GitHub側のHTML変更時は `src/build.py` のselector修正が必要です。ランキングやスター数は安全性を保証しません。
