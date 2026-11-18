# Tech Daily — 2026-11-18

生成日時: 2026-11-18T12:04:18.379882+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

**概要:** モダンなWebプラットフォームの専門知識やベストプラクティスをコーディングエージェントに組み込むためのスキルとドキュメントを提供するソースリポジトリです。古いパターンを避け、最新のWebプラットフォームの機能を活用した解決策へと導きます。

- 言語: TypeScript
- 今週のスター: 7015
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- 対話型ウィザードを使用したモダンWebガイダンスのインストール機能（根拠: Quickstart）

- 関連するガイドの検索、IDによるガイドの取得、コードベースのレガシーパターンのスキャンを行うCLI機能（根拠: Quickstart）

- ユーザーエクスペリエンス、CSSレイアウト、パフォーマンスに関する最新のWebプラットフォーム機能やガイドの提供（根拠: What's Included?）


### 利用例

- コーディングエージェントが古いコードや冗長なJavaScriptを生成するのを防ぎ、最新のネイティブなWebプラットフォームソリューションを活用させる（README明記／根拠: Why?）

- プロジェクトのコードベースをスキャンしてレガシーパターンを検出し、モダン化するためのガイドを適用する（README明記／根拠: Quickstart）


### 最初に試すこと

インストールせずにCLIを使用して関連ガイドを検索する

1. npx modern-web-guidance@latest search "animate a dialog modal backdrop"


成功の目安: ダイアログモーダルの背景アニメーションに関連するガイドの検索結果が表示されること

未確認: 代替のインストール方法の詳細な手順


## 2. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

**概要:** Plannotatorは、AIコーディングエージェントと人間の間のレビューを仲介するローカルのブラウザベースのツールです。エージェントの計画、仕様、HTML、コード差分などをブラウザ上でアノテーションやコメント、コードレビューを行い、そのフィードバックをワンクリックでエージェントに送り返すことができます。

- 言語: TypeScript
- 今週のスター: 2926
- ライセンス: Apache-2.0
- AI分析状態: ok

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




## 3. [meta/astryx](https://github.com/meta/astryx)

**概要:** Astryxは、Metaで社内開発されオープンソース化された、カスタマイズ可能でAIエージェントの利用にも対応したオープンソースのデザインシステムです。150以上のアクセシブルなコンポーネント、テーマ機能、ダークモード、テンプレート、CLIを提供します。

- 言語: TypeScript
- 今週のスター: 8700
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 150以上のアクセシブルなReactコンポーネントと完全なTypeScriptサポートを提供します。（根拠: Overview）

- ブランドレベルのテーマ機能、ダークモード、すぐに使えるテンプレートを備えています。（根拠: Overview）

- コンポーネントのソースコードをプロジェクトに取り込んで直接編集できる「swizzle」機能を持ちます。（根拠: Overview）


### 利用例

- 人手とAIアシスタントの両方で同じツールやAPIを用いてUIを構築する。（README明記／根拠: Overview）

- Tailwind CSSやCSSモジュール、通常のCSSなど既存のプロジェクトのスタイリング方法で上書きして利用する。（README明記／根拠: Overview）

- CLIツールを活用したコンポーネントのドキュメント参照やテンプレート、スキャホーディング、テーマ管理を行う。（README明記／根拠: Packages）


### 最初に試すこと

npmを使用して、Astryxのコアパッケージ、中立テーマ、依存関係、およびCLIをインストールする。

1. npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex

2. npm install -D @astryxdesign/cli


成功の目安: エラーなくパッケージのインストールが完了し、プロジェクトの依存関係に追加されること。

未確認: 具体的なNext.jsやVite、Tailwindなどの詳細な統合手順（パッケージ内の外部ドキュメントを参照する必要があるため）


## 4. [we-promise/sure](https://github.com/we-promise/sure)

**概要:** we-promise/sure は、開発が終了した Maybe Finance プロジェクトのコミュニティ主導によるフォーク版であり、すべての人のための個人財務・資産管理アプリケーションです。Dockerによるセルフホストやブラウザ、デスクトップアプリ、モバイルアプリなどからのアクセスをサポートしています。

- 言語: Ruby
- 今週のスター: 4786
- ライセンス: AGPL-3.0
- AI分析状態: ok（キャッシュ）

### できること

- Dockerを使用して個人財務アプリをセルフホストできる（根拠: Hosting Sure）

- ブラウザ、macOSデスクトップアプリ、モバイルアプリ、APIクライアント、LLMエージェントからアクセス可能（根拠: Hosting Sure）

- 開発環境向けにデモデータをロードする機能を持つ（根拠: Local Development Setup）


### 利用例

- 個人や家族の資産管理・財務状況の把握のためにアプリを自前でホストして利用する（README明記／根拠: Hosting Sure）

- 開発者がローカル環境でアプリのソースコードを実行し、貢献やカスタマイズを行う（README明記／根拠: Local Development Setup）


### 最初に試すこと

ローカル環境でアプリケーションを起動し、動作を確認する

1. cd sure

2. cp .env.local.example .env.local

3. bin/setup

4. bin/dev

5. rake demo_data:default


成功の目安: http://localhost:3000 にアクセスしてアプリケーションが閲覧でき、デモデータの資格情報でログインできること

未確認: Maybe Financeからのフォーク以降に追加された具体的な新機能の全容／LLMエージェントやモバイルアプリとの連携の詳細な設定手順


## 5. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

**概要:** ZhuLinsen/daily_stock_analysisは、LLMを活用して複数市場（A株、香港株、米国株、日本株、韓国株、台湾株）の株式を自動分析し、決定ダッシュボードをチャットツールやメールにプッシュ通知するシステムです。

- 言語: Python
- 今週のスター: 3653
- ライセンス: MIT
- AI分析状態: ok

### できること

- 核心結論、スコア、トレンド、売買ポイント、リスクアラートなどのAI決定レポートの生成（根拠: ✨ 功能特性）

- 複数市場（A株、香港株、米国株、日本株、韓国株、台湾株、ETF）のデータ集約（根拠: ✨ 功能特性）

- Webおよびデスクトップワークスペースによる手動分析、タスク進捗、履歴レポート管理（根拠: ✨ 功能特性）


### 利用例

- 毎日の株式市場の分析結果を企業微信、飛書、Telegram、Discord、Slack、メールへ自動通知する（README明記／根拠: README冒頭）

- 複数市場のリアルタイムニュースや基本面データを活用して投資判断の参考情報を作成する（README明記／根拠: ✨ 功能特性）

- GitHub ActionsやDockerを用いてサーバーレスで定期的に株価分析を実行する（README明記／根拠: 🚀 快速开始）


### 最初に試すこと

リポジトリをクローンしてローカル環境で分析を実行する

1. git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

2. pip install -r requirements.txt

3. cp .env.example .env && vim .env

4. python main.py


成功の目安: main.pyがエラーなく実行され、分析結果が出力されること

未確認: 有料APIキーを利用しない場合の具体的な無料枠の制限詳細／一部のデータソースにおける詳細な取得エラー時の挙動


## 6. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 4847
- ライセンス: 不明
- AI分析状態: ok（キャッシュ）

### できること

- Claudeが特殊なタスクを繰り返し完了できるように、指示、スクリプト、リソースのフォルダを動的に読み込ませる（根拠: Skills）

- Claude Codeのプラグインマーケットプレイスとしてこのリポジトリを登録し、プラグインをインストールして使用できるようにする（根拠: Claude Code）

- YAMLフロントマッターと指示を含むSKILL.mdファイルを持つフォルダを作成し、カスタムスキルを定義する（根拠: Creating a Basic Skill）


### 利用例

- 会社のブランドガイドラインに沿ったドキュメントの作成（README明記／根拠: Skills）

- 組織固有のワークフローを使用したデータの分析（README明記／根拠: Skills）

- PDFファイルのフォームフィールドの抽出などのドキュメント処理（README明記／根拠: Claude Code）


### 最初に試すこと

Claude Codeでリポジトリをプラグインマーケットプレイスとして登録する

1. Claude Codeを開く

2. 以下のコマンドを実行する: /plugin marketplace add anthropics/skills


成功の目安: リポジトリがClaude Codeのプラグインマーケットプレイスとして登録されること

未確認: カスタムスキルの詳細なAPIリクエストの実装コード／各スキルが内部で行う処理の詳細なロジック


## 7. [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter)

**概要:** Claude-BugHunterは、バグハンティングや外部レッドチーム作業を支援するClaude Code用スキルバンドルであり、脆弱性クラスや攻撃マトリクス、検証ツールを提供します。

- 言語: Python
- 今週のスター: 2508
- ライセンス: MIT
- AI分析状態: ok

### できること

- トピックに応じて自動ロードされる83個のスキルと15個のスラッシュコマンドを提供します。（根拠: What is this?）

- Webアプリケーション脆弱性や企業の境界防御に対する攻撃パターン、チェーンテンプレートを含みます。（根拠: What is this?）

- Claude Codeだけでなく、OpenAI Codex CLIやHermes Agentなどの複数のエージェントハーネスに対応しています。（根拠: Runs on multiple agent harnesses）


### 利用例

- バグバウンティハンティングにおけるWebアプリ、API、GraphQL、OAuthなどの脆弱性調査を行います。（README明記／根拠: Scope — what this bundle is for, and what it isn't）

- インターネット公開された企業のインフラストラクチャやクラウドIAMに対する外部レッドチーム評価を実施します。（README明記／根拠: Scope — what this bundle is for, and what it isn't）

- 検出された脆弱性の検証や証拠の管理、レポーティング作業をサポートします。（README明記／根拠: Scope — what this bundle is for, and what it isn't）


### 最初に試すこと

Claude Codeのプラグインとしてclaude-bughunterをインストールして機能を利用する

1. /plugin marketplace add elementalsouls/Claude-BugHunter

2. /plugin install claude-bughunter@elementalsouls


成功の目安: 83個のスキルと15個のコマンドが名前空間付きでロードされ利用可能になること




## 8. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

**概要:** Alibabaが開発したオープンソースのAIコードレビューCLIツールです。決定論的パイプラインとLLMエージェントを組み合わせたハイブリッドアーキテクチャを採用しており、Gitの差分やファイル全体を正確に行単位でレビューします。

- 言語: Go
- 今週のスター: 3675
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- Gitの差分を読み込み、変更されたファイルをAIエージェントに送信して行単位の正確なレビューコメントを生成する（根拠: What is Open Code Review?）

- 差分だけでなく、ファイル全体をスキャンして未知のコードベースやディレクトリの監査を行うことができる（根拠: What is Open Code Review?）

- ネイティブモードとデリゲーションモードの2つのレビューモードをサポートしている（根拠: Agent Skills）


### 利用例

- ワークスペース内のステージング、未ステージング、および追跡されていないすべての変更をレビューする（README明記／根拠: Quick Start）

- フィーチャーブランチの変更をメインブランチとの分岐点からレビューする（README明記／根拠: Quick Start）

- Gitの履歴がないコードベースやディレクトリに対して、ファイル全体のフルスキャンを実行してレビューする（README明記／根拠: Quick Start）


### 最初に試すこと

ツールをグローバルにインストールし、LLMプロバイダーを設定して最初のレビューを実行する

1. npm install -g @alibaba-group/open-code-review

2. ocr config provider

3. ocr config model

4. cd your-project

5. ocr review


成功の目安: プロジェクトのコード変更に対するレビュー結果が出力されること

未確認: 対応しているすべてのLLMプロバイダーの完全なリスト／具体的なCI/CDパイプラインとの統合設定の全詳細


## 9. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

**概要:** agent-browserは、AIエージェント向けのネイティブRust製ブラウザ自動化CLIツールです。シェルコマンドから1つずつブラウザを操作でき、ページをアクセシビリティツリーのコンパクトなテキストとしてスナップショット取得して要素の参照（ref）を返し、それに対してクリックなどの操作を行えます。

- 言語: Rust
- 今週のスター: 3429
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- ページをコンパクトなテキスト（アクセシビリティツリー）としてスナップショット取得し、各要素にrefを割り当てる機能（根拠: README冒頭）

- クリック、入力、スクロール、待機、スクリーンショット撮影などの豊富なブラウザ操作コマンドの提供（根拠: Commands）

- エージェント向けのスキル取得機能やMCPサーバーとしての起動機能（根拠: For AI agents）


### 利用例

- シェルからAIエージェントにWebページを開かせ、要素を指定してクリックや入力を行わせるブラウザ自動化（README明記／根拠: Quick start）

- AIエージェントにスキルやMCPサーバー機能を組み込んで、インタラクティブなWeb操作ワークフローを実行させる（README明記／根拠: For AI agents）


### 最初に試すこと

ブラウザを開いてページのインタラクティブな要素のスナップショットを取得し、要素をクリックして結果を確認する

1. agent-browser open example.com

2. agent-browser snapshot -i

3. agent-browser click @e1

4. agent-browser get url

5. agent-browser close


成功の目安: コマンドが正常に実行され、指定したURLのページ操作結果が取得できること

未確認: 詳細な設定ファイルや環境変数によるカスタマイズの全容／LightpandaやObscuraなど特定エンジン・プロバイダの具体的な設定・接続手順


## 10. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**概要:** chrome-devtools-mcpは、コーディングエージェントがライブのChromeブラウザを制御・検査できるようにするモデルコンテキストプロトコル(MCP)サーバーおよびCLIツールです。

- 言語: TypeScript
- 今週のスター: 2948
- ライセンス: Apache-2.0
- AI分析状態: ok

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





## Zenn

- [L40S 1台で社内RAGは何人まで使えるか](https://zenn.dev/epicai_techblog/articles/29b509117755af) — a_shinohara

- [おい、 Mutation Test をやれ。テスト品質を、測るために](https://zenn.dev/mizchi/articles/mutation-test-quality) — mizchi

- [Go Conference 2026実行委員を終えて](https://zenn.dev/mire0726/articles/1f3f118662a0f5) — Suu

- [ローカルLLM入門](https://zenn.dev/port_inc/articles/ff974c7456f4db) — tesla

- [LTを盛り上げよう！AWSサービス応援うちわ制作裏話](https://zenn.dev/namiki64/articles/7aab23e02d1dc4) — なみき

- [Claude Desktop 開発のすゝめ](https://zenn.dev/peoplex_blog/articles/vscode-to-claude-desktop) — Aki 🚀 Product Engineer @ PeopleX

- [毎月6,000 AI Agentsを捌くためにキーボードを捨てた話](https://zenn.dev/andoshin11/articles/ba68b39ef9a8ce) — Andy

- [mise + gh skill で、dotfiles から Agent Skills を管理する](https://zenn.dev/dress_code/articles/30bd78e1a67f87) — ぷーじ

- [OpenTelemetry×Cloudflareで組織のClaude Code利用ログを収集する](https://zenn.dev/gemcook/articles/claude-code-otel-cloudflare) — soso

- [お問い合わせの8割を、AIボットが解決するようになった話](https://zenn.dev/rimo/articles/701d18b7764669) — soliste

- [スマホ内蔵のセンサーを使って周辺光取得を試す](https://zenn.dev/aldagram_tech/articles/f7b57935e31070) — KSND

- [フロントエンドの logic と UI は、エージェントの責任範囲で分けられるのか](https://zenn.dev/xtm_blog/articles/20261116-fd1702b0ba06cd) — mizumoto

- [QA生産性を爆上げさせるためのQA AIプラットフォーム構築](https://zenn.dev/gatechnologies/articles/8bdea59269eb10) — akki

- [物理世界とAIをつなぐ：可視化で学ぶカメラ・座標系・運動制御入門](https://zenn.dev/turing_motors/articles/cea9e3c85611b2) — ymg_aq

- [Claude Codeが書いたコードを読む代わりにやっていること](https://zenn.dev/linkedge/articles/claude-code-instead-of-reading-code) — Misugi Takeru

- [mizchi/mutator を入れてみた](https://zenn.dev/polyco/articles/e05cb28c569801) — Tatsunori Nakano

- [GitHub IssueにArtifactとしてHTMLとMarkdownを添付できるようになった](https://zenn.dev/kesin11/articles/20261114_github_issue_artifact) — Kesin11

- [フロントエンドのフレームワークを、安全に段階的に入れ替える](https://zenn.dev/yasuakiomokawa/articles/de83bb4c4ea928) — Yasuaki Omokawa

- [【pstack】AIに敵対的レビューをさせるな。トークンは検証に使え](https://zenn.dev/karamage/articles/5c3f8370b2b370) — karamage

- [Software Factoryの先へ：全社の仕事をAI-NativeにするUbieの内製クラウドエージェント基盤](https://zenn.dev/ubie_dev/articles/45501469c9c044) — Yuku Kotani


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。