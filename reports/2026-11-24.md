# Tech Daily — 2026-11-24

生成日時: 2026-11-24T14:27:37.178055+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

**概要:** Plannotatorは、AIコーディングエージェントと人間の間のレビューを仲介するローカルのブラウザベースのツールです。エージェントの計画、仕様、HTML、コード差分などをブラウザ上でアノテーションやコメント、コードレビューを行い、そのフィードバックをワンクリックでエージェントに送り返すことができます。

- 言語: TypeScript
- 今週のスター: 2395
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
- 今週のスター: 2572
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
- 今週のスター: 2694
- ライセンス: Apache-2.0
- AI分析状態: ok

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

**概要:** Open Code Reviewは、決定論的なエンジニアリングパイプラインとLLMエージェントを組み合わせた、AI駆動型のコードレビューCLIツールです。行単位の正確なコメント生成や、大規模な変更に対するスマートなファイルバンドル機能などを提供します。

- 言語: Go
- 今週のスター: 3015
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- Gitの差分を読み取り、行単位の正確さで構造化されたレビューコメントを生成する機能（根拠: What is Open Code Review?）

- 変更のあったファイルだけでなく、ファイル全体を対象に監査するocr scan機能（根拠: What is Open Code Review?）

- 関連するファイルをひとつのレビュー単位にまとめて並行レビューを行うスマートファイルバンドル機能（根拠: Core Design: Deterministic Engineering × Agent Hybrid）


### 利用例

- ステージング、未ステージング、追跡されていない変更を含むワークスペース全体のコードレビュー（README明記／根拠: Quick Start）

- メインブランチから分岐した機能ブランチ間などの差分レビュー（README明記／根拠: Quick Start）

- gitの履歴がないプロジェクトや馴染みのないコードベース全体のフルファイルスキャン監査（README明記／根拠: Quick Start）


### 最初に試すこと

CLIツールをインストールしてモデルを設定し、プロジェクトのコードレビューを実行する

1. npm install -g @alibaba-group/open-code-review

2. ocr config provider

3. ocr config model

4. cd your-project

5. ocr review


成功の目安: LLMの設定が完了し、プロジェクトのコードレビュー結果が出力されること

未確認: サポートされている特定の商用LLMプロバイダーの全リスト／詳細なCLI設定オプションの全仕様


## 5. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

**概要:** Reddit、X、YouTube、Hacker News、Polymarket、Webなどから指定したトピックに関する直近30日間の情報を並行検索し、AIエージェントが要約を作成するスキルです。

- 言語: Python
- 今週のスター: 5448
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- Reddit、X、YouTube、Hacker News、Polymarket、Webなどの複数プラットフォームを並行して検索し、AIエージェントが要約を生成する。（根拠: README冒頭）

- Claude Codeなどのプラグイン機構やnpxコマンドを通じて導入できる。（根拠: README冒頭）


### 利用例

- ビジネスの打ち合わせ前に、企業の直近30日間の動向や事実を調べる。（README明記／根拠: Why this exists）

- 人物の最近のツイートやポッドキャストのトランスクリプトを会議前に確認する。（README明記／根拠: Why this exists）

- 旅行の計画前に、アトラクションの状況やコミュニティの意見を調査する。（README明記／根拠: Why this exists）


### 最初に試すこと

Claude Codeを利用してプラグインを追加・インストールする

1. /plugin marketplace add mvanhorn/last30days-skill

2. /plugin install last30days


成功の目安: Claude Code環境へプラグインが追加およびインストールされること

未確認: 詳細なインストールオプション（claude.ai web、OpenClaw、手動）の具体的な手順／セットアップウィザードの詳細な挙動


## 6. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**概要:** chrome-devtools-mcpは、コーディングエージェントがライブのChromeブラウザを制御・検査できるようにするモデルコンテキストプロトコル(MCP)サーバーおよびCLIツールです。

- 言語: TypeScript
- 今週のスター: 1581
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
- 今週のスター: 1903
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
- 今週のスター: 2966
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

**概要:** Astryxは、Metaで開発されたオープンソースのカスタマイズ可能なデザインシステムです。React 19以降とStyleXを基盤にし、150以上のアクセシブルなコンポーネント、テーマ、CLIを提供することで、人間とAIアシスタントの両方が同じツールと規約でUIを構築できるように設計されています。

- 言語: TypeScript
- 今週のスター: 3165
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 150種類以上のアクセシブルなコンポーネント、ブランドレベルのテーマ、ダークモード、テンプレート、CLIを提供する（根拠: Overview）

- swizzle機能により、コンポーネントの完全なソースコードをプロジェクト内に取り込んでカスタマイズできる（根拠: Overview）

- CSSカスタムプロパティのオーバーライドによって、フォークせずにテーマをカスタマイズできる（根拠: Overview）


### 利用例

- 人間とAIアシスタントが同じ参照情報やCLIツールを使用して一貫したUIを構築する（README明記／根拠: Overview）

- 既存のプロジェクトのスタイルに合わせて、classNameやTailwind、CSS Modules等でコンポーネントを上書きする（README明記／根拠: Overview）

- CLIツールを使用してコンポーネントのドキュメントやテンプレート、テーマ、コーディモッドを利用する（README明記／根拠: Packages）


### 最初に試すこと

Astryxのコアパッケージ、中立テーマ、依存関係をインストールし、初期化コマンドを実行する

1. npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex

2. npm install -D @astryxdesign/cli

3. npx @astryxdesign/cli init


成功の目安: 初期化が完了し、AGENTS.mdまたはCLAUDE.mdにガイドが保存されること

未確認: 実験的コンポーネントである@astryxdesign/labの具体的な詳細／カナダ版として配信されている@astryxdesign/vegaおよび@astryxdesign/chartsの正式リリース時期


## 10. [pookjw/HermesEnabler](https://github.com/pookjw/HermesEnabler)

**概要:** HermesEnablerは、任意のApple Watchでエルメスの文字盤を使えるようにするためのツールです。macOSまたはWindows環境でサイドロードやXcodeを使ってインストールし、Apple Watch上のアプリから設定を行います。

- 言語: Objective-C
- 今週のスター: 390
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

- [コーディングエージェントが変えたOSS開発のプロセスと喜び](https://zenn.dev/cybergarage/articles/5ee7ac6b3b0565) — cybergarage

- [S3 Vectors は RAG のベクトルストアに使えるか（40問で検証＋ハイブリッド検索に関する追記）](https://zenn.dev/shino_i/articles/faeef70f08124c) — 伊佐眞皇(Shino Isa)

- [JSConf JP 2026に参加記録・初登壇の反省など](https://zenn.dev/igrep/articles/2026-11-jsconfjp) — YAMAMOTO Yuji

- [iOSエンジニアのための OAuth 2.0 + PKCE 入門 ― 仕組みを理解してから、Swiftで実装する](https://zenn.dev/mobile_app_tec/articles/ios-oauth2-pkce-native-app) — 小林　慎吾

- [【技術書典21】17人の開発者と作った合同誌『AI キャラクター開発 十人十色』、会場50部が完売しました！！！](https://zenn.dev/mei999/articles/33f2965b3c021c) — めい

- [Googleが実践するSTAMP/STPAとは何か？ 私たちのSREにも使えるのか](https://zenn.dev/maruloop/articles/7ff108e29741b5) — maru

- [JSConf JP 2026 公開資料・Xアカウントリンクまとめ](https://zenn.dev/h_yoshikawa0724/articles/2026-11-23-jsconf-jp-2026) — よし

- [著名なRust製OSSをLean 4で形式検証してみたら、めちゃめちゃバグが見つかった話](https://zenn.dev/koukyosyumei/articles/31c8fcf4da45b7) — Koukyosyumei

- [WolvCTF2026 - writeup](https://zenn.dev/gattoartz/articles/3f302189a1741a) — ちゃちゃまる / GattoArtz

- [箱入り娘ソルバーを約9,400倍高速化してもらった](https://zenn.dev/kaorun343/articles/klotski-solver-optimization) — kaorun343

- [Claude Code の mods を入れる前に調べたこと（備忘録）](https://zenn.dev/shogaku/articles/claude-code-mods-memo) — Ymori

- [ゲーム理論×シミュレーション: 囚人のジレンマにおける戦略と Rust による実装](https://zenn.dev/akitenkrad/articles/1zqjjioamhlyg2) — akitenkrad

- [AIがテストに合わせて実装していない？仕様テストを隠して確かめる](https://zenn.dev/h_aso/articles/isolated-spec-tests-claude-code) — H.Aso

- [Orca Botsが良さそう、何ができるのか](https://zenn.dev/kg_motors_mibot/articles/orca-bot-intro) — Sota Nakamura

- [【TLA+】AIにテストケースを書かせるな。ルールを書け](https://zenn.dev/karamage/articles/73027ee36796dc) — karamage

- [寝てる間に自動で動くAIエージェントを誰でも作れる：10分でわかる pstack 実践ガイド](https://zenn.dev/canly/articles/ca6875cd79539f) — haginota

- [自分の代わりに動くAgentへ。Claude CodeとCodexで作る自律改善ハーネス](https://zenn.dev/nttdata_tech/articles/9562962cc181a1) — Kazuma Yoshimoto | 吉本 和真

- [相次ぐOSSの脆弱性に、とりあえずクラウドWAF入れるだけでだいぶ違う話+Rootlessコンテナもいいぞ](https://zenn.dev/kusuke/articles/98e178e6824cac) — Yusuke Kawabata

- [なぜ今形式検証なのか](https://zenn.dev/ncdc/articles/dcec80b0c067b0) — senna

- [ローカルLLM入門](https://zenn.dev/port_inc/articles/ff974c7456f4db) — tesla


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。