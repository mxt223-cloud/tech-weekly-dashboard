# Tech Daily — 2026-11-19

生成日時: 2026-11-19T11:44:40.183841+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

**概要:** モダンなWebプラットフォームの専門知識やベストプラクティスをコーディングエージェントに組み込むためのスキルとドキュメントを提供するソースリポジトリです。古いパターンを避け、最新のWebプラットフォームの機能を活用した解決策へと導きます。

- 言語: TypeScript
- 今週のスター: 7257
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
- 今週のスター: 3290
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




## 3. [meta/astryx](https://github.com/meta/astryx)

**概要:** Astryxは、Metaで社内開発されオープンソース化された、カスタマイズ可能でAIエージェントの利用にも対応したオープンソースのデザインシステムです。150以上のアクセシブルなコンポーネント、テーマ機能、ダークモード、テンプレート、CLIを提供します。

- 言語: TypeScript
- 今週のスター: 6250
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
- 今週のスター: 3866
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


## 5. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

**概要:** OpenCodeReviewは、確定的パイプラインとLLMエージェントを組み合わせたハイブリッドなアーキテクチャを持つAIコードレビューツールです。Gitの差分や全体ファイルのスキャンを対象に、行単位の正確なレビューコメントや組込みの多言語ルールセットによるチェックを提供します。

- 言語: Go
- 今週のスター: 4383
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- Git差分の読取りと、設定可能なLLMを使用したツール機能付きエージェントによる行単位の正確な構造化レビューコメントの生成（根拠: What is Open Code Review?）

- 差分だけでなく、意味のある差分がないコードベースやディレクトリ全体を監査するための全ファイルスキャン機能（ocr scan）（根拠: What is Open Code Review?）

- OpenAIやAnthropic互換のプロバイダー設定と、ネイティブモードまたはデリゲーションモードの実行選択（根拠: How to Use）


### 利用例

- プロジェクトのGit差分（ステージ済み、未ステージ、未追跡の変更）をレビューする（README明記／根拠: How to Use）

- Gitの履歴がない状態や、変更履歴に依存せずにコードベースやディレクトリ全体をスキャンして監査する（README明記／根拠: How to Use）

- 独自のAPIキーを使用せず、ホストとなるAIコーディングエージェントの認証やサブスクリプションを利用してレビューを行う（README明記／根拠: How to Use）


### 最初に試すこと

CLIツールをインストールしてモデルを設定し、プロジェクトのレビューを実行する

1. npm install -g @alibaba-group/open-code-review

2. ocr config provider

3. ocr config model

4. cd your-project

5. ocr review


成功の目安: OCRのレビューが実行され、結果が出力されること

未確認: サポートされている具体的な全モデルの詳細なリスト／商用利用時における詳細な料金体系やAPI制限


## 6. [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)

**概要:** Google Stitchサーバーと連携するためのエージェントスキルおよびプラグインのコレクションです。デザイン、ビルド、ユーティリティの各カテゴリに分かれた機能を提供します。

- 言語: TypeScript
- 今週のスター: 1567
- ライセンス: Apache-2.0
- AI分析状態: ok

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


## 7. [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)

**概要:** tradermonty/claude-trading-skillsは、時間のない個人投資家向けにClaude Codeのスキルを活用した取引ワークフローツールキットです。売買の自動化ではなく、市場の確認やリスク管理、トレード計画、ジャーナル記録などの意思決定プロセスを構造化します。

- 言語: Python
- 今週のスター: 3242
- ライセンス: MIT
- AI分析状態: ok

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


## 8. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**概要:** chrome-devtools-mcpは、コーディングエージェントがライブのChromeブラウザを制御・検査できるようにするモデルコンテキストプロトコル(MCP)サーバーおよびCLIツールです。

- 言語: TypeScript
- 今週のスター: 3143
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




## 9. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 4381
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


## 10. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

**概要:** ZhuLinsen/daily_stock_analysisは、AI大模型を活用した多市場向けの株式自動分析・予測システムです。複数市場のデータやニュース、リアルタイムの情報を集約し、AIが分析した結果をダッシュボードや多様な通知チャネルを通じて自動配信します。

- 言語: Python
- 今週のスター: 3566
- ライセンス: MIT
- AI分析状態: ok

### できること

- AIによる決算やトレンド、売買ポイント、リスク警報を含む詳細な意思決定レポートの生成（根拠: ✨ 功能特性）

- A株、港株、美株、日株、韓株、台株などの複数市場のデータやニュース、テクニカル指標の集約（根拠: ✨ 功能特性）

- GitHub Actions、Docker、ローカル環境での定期実行および企業微信、飛書、Telegram、Discord、Slack、メールへの自動通知（根拠: ✨ 功能特性）


### 利用例

- 毎日の取引時間終了後に各市場の自選股（お気に入り銘柄）の分析レポートを自動で受け取り、投資判断に役立てる（README明記／根拠: 🚀 快速开始）

- Webインターフェースやチャットを通じて、AIエージェントに戦略的な銘柄の質問や過去データの確認を行う（README明記／根拠: 🤖 Agent 策略问股）

- ローカル環境やDockerを活用して、外部サーバーに依存せず独自に株式分析パイプラインを運用する（提案／根拠: 🚀 快速开始）


### 最初に試すこと

リポジトリをクローンして依存関係をインストールし、ローカル環境で分析を実行する

1. git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

2. pip install -r requirements.txt

3. cp .env.example .env && vim .env

4. python main.py


成功の目安: エラーなくプログラムが実行され、株価分析処理が完了すること

未確認: 実際にデプロイした際の使用するAIモデルの応答速度やコストの詳細／無料のデータソースが上游の制限を受けた場合の具体的なフォールバック挙動の全容



## Zenn

- [tsrs を導入したら oxlint の type-aware linting と typecheck が爆速になった話](https://zenn.dev/dress_code/articles/6c179ae5129131) — ぷーじ

- [QA効率化におけるAI活用事例](https://zenn.dev/applibot_tech/articles/6b8ec8d196634b) — tanaka_shuntaro

- [Odin に賭けたい人向けの Odin 言語入門ガイド](https://zenn.dev/mizchi/articles/odin-introduction-guide) — mizchi

- [Snowflake の managed access schema で COPY GRANTS 付き CLONE がなぜか初回だけ失敗した話](https://zenn.dev/finatext/articles/snowflake-managed-access-copy-grants) — okashunnn

- [ESLint から oxlint へ。lint が 50 倍速くなるまでの移行の記録](https://zenn.dev/rimo/articles/12d6a7b1c58fcd) — t.kuriyama

- [おい、 Mutation Test をやれ。テスト品質を、測るために](https://zenn.dev/mizchi/articles/mutation-test-quality) — mizchi

- [Go Conference 2026実行委員を終えて](https://zenn.dev/mire0726/articles/1f3f118662a0f5) — Suu

- [ローカルLLM入門](https://zenn.dev/port_inc/articles/ff974c7456f4db) — tesla

- [Claude Desktop 開発のすゝめ](https://zenn.dev/peoplex_blog/articles/vscode-to-claude-desktop) — Aki 🚀 Product Engineer @ PeopleX

- [毎月6,000 AI Agentsを捌くためにキーボードを捨てた話](https://zenn.dev/andoshin11/articles/ba68b39ef9a8ce) — Andy

- [mise + gh skill で、dotfiles から Agent Skills を管理する](https://zenn.dev/dress_code/articles/30bd78e1a67f87) — ぷーじ

- [フロントエンドの logic と UI は、エージェントの責任範囲で分けられるのか](https://zenn.dev/xtm_blog/articles/20261116-fd1702b0ba06cd) — mizumoto

- [最近、コードを真面目に読まなくなった](https://zenn.dev/hiromoo/articles/reading-less-preparing-more) — むた

- [最適化プロダクトにおけるUX](https://zenn.dev/ctenopoma/books/optimization_ux) — クテノポマ

- [QA生産性を爆上げさせるためのQA AIプラットフォーム構築](https://zenn.dev/gatechnologies/articles/8bdea59269eb10) — akki

- [物理世界とAIをつなぐ：可視化で学ぶカメラ・座標系・運動制御入門](https://zenn.dev/turing_motors/articles/cea9e3c85611b2) — ymg_aq

- [CSS では書きにくいアニメーションを Web Animations API で書く](https://zenn.dev/omu_tryangle/articles/b5817393592229) — hyakutake

- [Claude Codeが書いたコードを読む代わりにやっていること](https://zenn.dev/linkedge/articles/claude-code-instead-of-reading-code) — Misugi Takeru

- [mizchi/mutator を入れてみた](https://zenn.dev/polyco/articles/e05cb28c569801) — Tatsunori Nakano

- [GitHub IssueにArtifactとしてHTMLとMarkdownを添付できるようになった](https://zenn.dev/kesin11/articles/20261114_github_issue_artifact) — Kesin11


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。