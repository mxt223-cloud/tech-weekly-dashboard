# Tech Daily — 2026-11-25

生成日時: 2026-11-25T13:29:54.481946+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

**概要:** Plannotatorは、AIコーディングエージェントと人間の間のレビューを仲介するローカルのブラウザベースのツールです。エージェントの計画、仕様、HTML、コード差分などをブラウザ上でアノテーションやコメント、コードレビューを行い、そのフィードバックをワンクリックでエージェントに送り返すことができます。

- 言語: TypeScript
- 今週のスター: 1956
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- プラン、仕様書、Markdown、HTML、その他のインタラクティブな成果物の確認とアノテーション（根拠: README冒頭）

- ローカルの変更点やリモートのプルリクエスト（PR）のコードレビュー、差分やコードへのコメント、ガイド付きレビュー機能（根拠: README冒頭）

- プラグイン、フック、コマンドを通じて主要なAIエージェントと直接連携し、フィードバックをエージェントへ送り返す仕組み（根拠: README冒頭）


### 利用例

- AIコーディングエージェントが作成した計画や仕様書に対してブラウザ上でコメントや指示を書き込み、エージェントの次の動作に反映させる（README明記／根拠: Plannotator Inbox）

- Gitなどのリポジトリのローカル変更やプルリクエストの差分をブラウザやターミナルでレビューし、コードの提案や修正指示をエージェントに戻す（README明記／根拠: README冒頭）

- ローカルで稼働しているWebサイトやHTMLファイルをプロ経由でブラウザ上に表示し、実際のページを見ながらコメントをつける（README明記／根拠: HTML artifacts, live sites, and guided reviews）


### 最初に試すこと

Plannotatorのインストーラーを使用してツールを導入し、エージェントのメッセージや差分のレビュー機能を試す

1. curl -fsSL https://plannotator.ai/install.sh | bash を実行してバイナリと対応する設定をインストールする

2. /plannotator-last コマンドを実行してエージェントの最後の返信に対するアノテーションを開く


成功の目安: ブラウザまたは指定されたインターフェース上でレビュー画面やアノテーション機能が起動し、操作できるようになること




## 2. [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)

**概要:** Google Stitchサーバーと連携するためのエージェントスキルおよびプラグインのコレクションです。デザイン、ビルド、ユーティリティの各カテゴリに分かれた機能を提供します。

- 言語: TypeScript
- 今週のスター: 2626
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- フロントエンドコードをHTML抽出やデザインシステム適用を通じてStitchデザインに変換・アップロードする（根拠: Design (stitch-design)）

- Stitchの画面をReactコンポーネントやReact Nativeコンポーネントに変換する（根拠: Build (stitch-build)）

- 曖昧なUIのアイデアを洗練されたStitch最適化プロンプトに変換したり、DESIGN.mdファイルを生成・検証したりする（根拠: Utilities (stitch-utilities)）


### 利用例

- フロントエンドのコードからデザインシステムを抽出し、DESIGN.mdファイルを作成する（README明記／根拠: Design (stitch-design)）

- Stitchプロジェクトの画面からRemotionを使用してウォークスルー動画を生成する（README明記／根拠: Build (stitch-build)）

- 設定ページなどのあいまいなUI作成の指示を、詳細なUI/UXキーワードを含むプロンプトに拡張する（README明記／根拠: Utilities (stitch-utilities)）


### 最初に試すこと

プラグインのヘルプドキュメントを表示して導入を確認する

1. npx plugins --help

2. npx skills --help


成功の目安: プラグインやスキルのヘルプドキュメントが表示されること

未確認: 対応するコーディングエージェントのうちCodexやOpenCode以外の詳細な内部動作／Stitch MCPサーバーの具体的なセットアップ手順の詳細


## 3. [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

**概要:** コーディングエージェント向けに最新のウェブ標準のベストプラクティスやブラウザ互換性データを提供するツールです。レガシーなパターンを避け、モダンなウェブプラットフォームの機能や高性能な解決策を活用できるようエージェントを誘導します。

- 言語: TypeScript
- 今週のスター: 2494
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- インタラクティブなウィザードを使用して Modern Web Guidance をインストールする（根拠: Quickstart）

- インストールせずに、関連するガイドの検索やIDによるガイドの取得、コードベースのレガシーパターンスキャンを行う（根拠: Quickstart）

- ユーザーエクスペリエンス、CSSレイアウト、パフォーマンスなどのコアディシプリンに関する専門的でトークン効率の良いガイドラインをエージェントに提供する（根拠: What's Included?）


### 利用例

- コーディングエージェントがレガシーなパターンを生成するのを防ぎ、モダンなウェブプラットフォーム機能を利用したコードを書くように誘導する（README明記／根拠: Why?）

- CLIツールを使用して関連するガイドを検索し、エージェントのコンテキストウィンドウに直接ターゲットを絞った専門的なガイドラインを返す（README明記／根拠: Quickstart）

- コードベースをスキャンして古いパターンを見つけ出し、最新化する作業を支援する（README明記／根拠: Quickstart）


### 最初に試すこと

インストールせずにコマンドを実行して機能を試す

1. npx modern-web-guidance@latest search "animate a dialog modal backdrop"


成功の目安: 関連するガイドの検索結果が表示されること

未確認: 詳細なインストール後の設定項目やカスタマイズ方法


## 4. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

**概要:** OpenCodeReviewは、確実な決定論的パイプラインとLLMエージェントを組み合わせたハイブリッドなアーキテクチャを持つ、AIを活用したコードレビューCLIツールです。

- 言語: Go
- 今週のスター: 2638
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- Gitの差分を読み込み、変更されたファイルをLLMエージェントに送信して行単位の正確な構造化レビューコメントを生成する（根拠: What is Open Code Review?）

- ocr scanコマンドを使用して、変更履歴のないコードベースやディレクトリ全体をスキャンし監査する（根拠: What is Open Code Review?）

- ファイルを選択してレビューするための決定論的なエンジニアリングハード制約と、動的なコンテキスト取得を行うエージェントを組み合わせる（根拠: Core Design: Deterministic Engineering × Agent Hybrid）


### 利用例

- ワークスペースモードですべてのステージ済み、未ステージ、未追跡の変更をレビューする（README明記／根拠: Quick Start）

- メインブランチから分岐した機能ブランチの変更範囲をレビューする（README明記／根拠: Quick Start）

- 特定のディレクトリやファイル全体をスキャンしてコードレビューを行う（README明記／根拠: Quick Start）


### 最初に試すこと

CLIツールをインストールしてモデルを設定し、レビューを実行する

1. npm install -g @alibaba-group/open-code-review

2. ocr config provider

3. ocr config model

4. ocr review


成功の目安: ocr reviewコマンドが正常に実行され、プロジェクトのコードレビュー結果が出力されること

未確認: サポートされている全てのモデルプロバイダーの個別名称や対応しているAPIの完全な仕様／CI/CDインテグレーションの具体的な設定ファイルの詳細


## 5. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

**概要:** Reddit、X、YouTube、Hacker News、Polymarket、Webなどから指定したトピックに関する直近30日間の情報をAIエージェントが並行して検索・統合し、要約を提供するツールです。

- 言語: Python
- 今週のスター: 5369
- ライセンス: MIT
- AI分析状態: ok

### できること

- Reddit、X、YouTube、TikTok、Hacker News、Polymarket、GitHub、Webなど複数のプラットフォームを横断して検索を行います。（根拠: README冒頭）

- 検索結果をアップボートや「いいね」、実際の資金によるオッズなどのエンゲージメント指標をもとにスコアリングし、AIエージェントが要約を作成します。（根拠: README冒頭）


### 利用例

- 商談の前に企業の直近の動向や真実の情報を調べるために実行します。（README明記／根拠: Why this exists）

- 会議の前に人物の最近のツイートやポッドキャストの文字起こしを読み込むために使用します。（README明記／根拠: Why this exists）

- 何かを構築する前に、コミュニティが実際に直面している課題を把握するために利用します。（README明記／根拠: Why this exists）


### 最初に試すこと

Claude Code環境へプラグインを追加する

1. /plugin marketplace add mvanhorn/last30days-skill

2. /plugin install last30days


成功の目安: プラグインが正常に追加およびインストールされること

未確認: 詳細な検索オプションや設定画面の具体的な全パラメータ／対応している全ソースの詳細なAPI要件


## 6. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**概要:** chrome-devtools-mcpは、コーディングエージェントがライブのChromeブラウザを制御・検査できるようにするモデルコンテキストプロトコル(MCP)サーバーおよびCLIツールです。

- 言語: TypeScript
- 今週のスター: 1258
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- Chrome DevToolsを使用してトレースを記録し、パフォーマンスインサイトを抽出する（根拠: Key features）

- ネットワークリクエストの分析、スクリーンショットの撮影、ブラウザコンソールメッセージの確認を行う（根拠: Key features）

- Puppeteerを使用してChrome内のアクションを自動化し、結果を自動的に待機する（根拠: Key features）


### 利用例

- ウェブページのパフォーマンスをチェックして改善する（README明記／根拠: Getting started）

- ターミナルからCLIを使用してブラウザを操作・制御する（README明記／根拠: CLI）

- アクセシビリティの問題を監査および修正する（README明記／根拠: Skills）


### 最初に試すこと

MCPクライアントからパフォーマンスをチェックして動作を確認する

1. MCPクライアントに設定を追加する

2. MCPクライアントにプロンプト「Check the performance of https://developers.chrome.com」を入力する


成功の目安: MCPクライアントがブラウザを開き、パフォーマンスのトレースを記録すること




## 7. [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)

**概要:** tradermonty/claude-trading-skillsは、時間のない個人投資家向けにClaude Codeのスキルを活用した取引ワークフローツールキットです。売買の自動化ではなく、市場の確認やリスク管理、トレード計画、ジャーナル記録などの意思決定プロセスを構造化します。

- 言語: Python
- 今週のスター: 1504
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 15分間の日次市場チェックを含む複数の運用ワークフローの提供（根拠: Recommended Starting Path）

- 週次長期ポートフォリオレビューの実施（根拠: Recommended Starting Path）

- 取引終了後の記録と学習を行うためのワークフローの提供（根拠: Recommended Starting Path）


### 利用例

- 限られた時間の中で日次市場の状況を手早く確認する（README明記／根拠: Recommended Starting Path）

- 長期投資や配当株・ETFを中心に据えつつ、規律あるスイングトレードを行う（README明記／根拠: Claude Trading Skills）

- 取引の記録と振り返りを通じて意思決定プロセスを改善する（README明記／根拠: Who This Is For）


### 最初に試すこと

プロバイダーキーなしでオフラインクイックスタートを試す

1. Offline Quick Start (docs/en/offline-quickstart.md) を参照する


成功の目安: 架空のレポートからNavigatorまでを確認できること

未確認: 具体的なインストールコマンドや具体的な実行コマンド／API要件の詳細な設定手順


## 8. [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)

**概要:** AG-UIは、AIエージェントとユーザー向けアプリケーションを接続するためのオープンで軽量なイベントベースのプロトコルです。フレームワークに依存せず、双方向のイベントストリームを用いてエージェントの出力をクライアントで描画できるようにします。

- 言語: TypeScript
- 今週のスター: 1753
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- フレームワークやアプリケーションに関わらず、AIエージェントを接続する双方向イベントストリームの提供（根拠: README冒頭）

- TypeScript、Python、.NETなど公式SDKを用いたエージェントとクライアントの実装（根拠: SDKs）

- ストリーミングチャット、生成AIによるUI表示、共有状態管理、ヒューマン・イン・the・ループなどの多様な機能の構築（根拠: Features: what you can build）


### 利用例

- 同一のAIエージェントを用いてウェブアプリ、モバイルアプリ、ターミナル、Slackなどの多様なクライアントを駆動させる（README明記／根拠: README冒頭）

- LangChain、CrewAI、Microsoft Agent Frameworkなどの各種エージェントフレームワークとの連携（README明記／根拠: Integrations）

- AIエージェントの思考プロセスやサブエージェントの動作をイベントとしてストリーミング表示する（README明記／根拠: Features: what you can build）


### 最初に試すこと

CLIを使用して新しいAG-UIアプリケーションの雛形を作成する

1. npx create-ag-ui-app@latest

2. export OPENAI_API_KEY="sk-..."


成功の目安: CLIによるアプリのテンプレート生成と環境変数の設定が完了すること

未確認: CLIで生成されるテンプレートの具体的な動作検証結果／コミュニティSDKの細かな実装差異


## 9. [meta/astryx](https://github.com/meta/astryx)

**概要:** Metaで開発されたオープンソースのデザインシステムであり、150以上のアクセシブルなコンポーネント、テーマ機能、CLIを提供し、人間とAIアシスタントの両方が同じツールと規約でUIを構築できるように設計されています。

- 言語: TypeScript
- 今週のスター: 2890
- ライセンス: MIT
- AI分析状態: ok

### できること

- 150以上のアクセシブルなコンポーネント、ブランドレベルのテーマ、ダークモード、テンプレート、CLIを単一のシステムとして提供する（根拠: Overview）

- コンポーネントの完全なソースコードをプロジェクト内に抽出して所有できるスウィズル機能を持つ（根拠: Overview）

- React 19以降とStyleXを基盤とし、TailwindやCSSモジュールなどの既存のスタイル手法でオーバーライドできる（根拠: Overview）


### 利用例

- 人間とAIアシスタントが同じ参照情報とツールを使用してUIを構築する（README明記／根拠: Overview）

- CSSカスタムプロパティのオーバーライドによって、コンポーネントのソースコードをフォークせずにカスタムテーマを適用する（README明記／根拠: Overview）

- CLIツールを使用してコンポーネントのドキュメント参照や初期化を行う（README明記／根拠: Getting Started）


### 最初に試すこと

Astryxのコアパッケージ、テーマ、ピア依存関係、およびCLIをインストールする

1. npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex

2. npm install -D @astryxdesign/cli

3. npx @astryxdesign/cli init


成功の目安: 初期化コマンドが実行され、ガイドファイルが保存されること

未確認: Next.jsやViteなどの個別フレームワークでの詳細な統合手順（外部のコアREADMEへのリンクとなっているため本README内では未記載）


## 10. [pookjw/HermesEnabler](https://github.com/pookjw/HermesEnabler)

**概要:** HermesEnablerは、任意のApple Watchでエルメスの文字盤を使えるようにするためのツールです。macOSまたはWindows環境でサイドロードやXcodeを使ってインストールし、Apple Watch上のアプリから設定を行います。

- 言語: Objective-C
- 今週のスター: 328
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 任意のApple Watchデバイスでエルメスの文字盤を利用可能にする（根拠: README冒頭）

- macOS向けにSideloadlyを用いたIPAインストールやXcodeでのビルドをサポートする（根拠: macOS）

- Windows向けにコミュニティツールWatchBridgeを通じたインストールをサポートする（根拠: Windows）


### 利用例

- 非対応のApple Watchでエルメスの文字盤を表示させたい場合に、アプリをインストールして利用する（README明記／根拠: README冒頭）


### 最初に試すこと

対応するwatchOSを搭載したApple Watchとペアリングされた環境で、HermesEnabler2をインストールしてアプリ内の手順を開始する

1. ReleasesからIPAをダウンロードする

2. macOSの場合はSideloadly等を使用してiPhoneおよびApple Watchへアプリをインストールする

3. Apple Watch上でHermesEnabler2を開き、アプリ内の手順に従う


成功の目安: Apple Watch上でHermesEnabler2が起動し、アプリ内の手順に進めること

未確認: アプリ内でエルメス文字盤を有効化する具体的な仕組みや手順の詳細



## Zenn

- [MCPの記録ツールを追記だけで作ると、訂正のたびに重複が残る。AIは「消せない」と正直に言うが、集計は間違える](https://zenn.dev/kentaro_tak/articles/mcp-logger-append-only-corrections) — kentaro

- [Copilot Studioのエージェント開発をClaude Codeにどこまで任せられるか試した](https://zenn.dev/upgradetech/articles/a9a1637d3071c1) — masa

- [JSConf JP 2026 参加ログ](https://zenn.dev/aishift/articles/b6dbe1c0acc505) — さっちゃん

- [Gemini 4 Neon を API で叩いて Claude Code・Codex CLI と比べた：65万トークンの超長文、費用、失敗](https://zenn.dev/canly/articles/40e773759da8f8) — haginota

- [Claude Code の /ship を図解する](https://zenn.dev/peoplex_blog/articles/claude-code-ship) — Aki 🚀 Product Engineer @ PeopleX

- [Microsoft Foundry で AI エージェントを設計するときに決める5つのこと](https://zenn.dev/microsoft/articles/daedf42c8463b8) — Yusuke Shimizu

- [Claude Code を5〜8個並べても迷わないように、自分用のダッシュボードをバイブコーディングで作った](https://zenn.dev/nexta_/articles/a3ff76a9f98f1c) — bik

- [Alpamayo は Jetson でリアルタイム推論できるか？ R1 から 2 Edge まで、H100 プロファイルからの実行時間推定](https://zenn.dev/fixstars/articles/alpamayo-h100) — Togo Sakurai

- [「コードを書く」から「迷わず判断する」へ——AIエージェント時代の開発ワークフローを自作ツールで再設計した話](https://zenn.dev/syarihu/articles/ba25f243ca79ed) — syarihu

- [コードを全部は読まずにClaude Codeで本番リリースするためにしたこと](https://zenn.dev/teradox_blog/articles/8ec76cc0d9e2bb) — A.Yoshikawa

- [JSConf JP 2026に参加記録・初登壇の反省など](https://zenn.dev/igrep/articles/2026-11-jsconfjp) — YAMAMOTO Yuji

- [JSConf JP 2026 公開資料・Xアカウントリンクまとめ](https://zenn.dev/h_yoshikawa0724/articles/2026-11-23-jsconf-jp-2026) — よし

- [著名なRust製OSSをLean 4で形式検証してみたら、めちゃめちゃバグが見つかった話](https://zenn.dev/koukyosyumei/articles/31c8fcf4da45b7) — Koukyosyumei

- [プログラミング教育の功罪](https://zenn.dev/nobkz/articles/a8ed5591cd3e7d) — Nobkz

- [Orca Botsが良さそう、何ができるのか](https://zenn.dev/kg_motors_mibot/articles/orca-bot-intro) — Sota Nakamura

- [【TLA+】AIにテストケースを書かせるな。ルールを書け](https://zenn.dev/karamage/articles/73027ee36796dc) — karamage

- [寝てる間に自動で動くAIエージェントを誰でも作れる：10分でわかる pstack 実践ガイド](https://zenn.dev/canly/articles/ca6875cd79539f) — haginota

- [自分の代わりに動くAgentへ。Claude CodeとCodexで作る自律改善ハーネス](https://zenn.dev/nttdata_tech/articles/9562962cc181a1) — Kazuma Yoshimoto | 吉本 和真

- [相次ぐOSSの脆弱性に、とりあえずクラウドWAF入れるだけでだいぶ違う話+Rootlessコンテナもいいぞ](https://zenn.dev/kusuke/articles/98e178e6824cac) — Yusuke Kawabata

- [なぜ今形式検証なのか](https://zenn.dev/ncdc/articles/dcec80b0c067b0) — senna


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。