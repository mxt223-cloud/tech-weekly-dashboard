# Tech Daily — 2026-11-22

生成日時: 2026-11-22T10:29:29.745639+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

**概要:** Plannotatorは、AIコーディングエージェントと人間の間のレビューを仲介するローカルのブラウザベースのツールです。エージェントの計画、仕様、HTML、コード差分などをブラウザ上でアノテーションやコメント、コードレビューを行い、そのフィードバックをワンクリックでエージェントに送り返すことができます。

- 言語: TypeScript
- 今週のスター: 3396
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
- 今週のスター: 2431
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

**概要:** GoogleChrome/modern-web-guidance-srcは、コーディングエージェント向けに最新のウェブプラットフォームの専門知識、ベストプラクティス、ブラウザ互換性データを提供するスキルセットおよびそのソースリポジトリです。レガシーなパターンの生成を防ぎ、最新のウェブ機能を活用した実装へと導きます。

- 言語: TypeScript
- 今週のスター: 4400
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- インタラクティブウィザードを使用したModern Web Guidanceのインストール（根拠: Quickstart）

- 関連するガイドの検索、IDによるガイドの取得、コードベース内のレガシーパターンのスキャン（根拠: Quickstart）

- 最新のブラウザAPI、パフォーマンスとアクセシビリティ、責任あるフォールバックに関するガイドラインの提供（根拠: Why?）


### 利用例

- コーディングエージェントに最新のウェブのベストプラクティスを組み込み、レガシーパターンを避けた実装を行わせる（README明記／根拠: README冒頭）

- CLIツールを用いて特定のUI実装に関連するガイドを検索し、エージェントのコンテキストウィンドウに提供する（README明記／根拠: Quickstart）

- 既存のコードベースをスキャンしてモダン化が必要なレガシーパターンを検出する（README明記／根拠: Quickstart）


### 最初に試すこと

インストールせずにコマンドを使用して関連ガイドを検索する

1. npx modern-web-guidance@latest search "animate a dialog modal backdrop"


成功の目安: 関連するガイドの検索結果が表示されること

未確認: 詳細な内部実装アルゴリズムや評価ダッシュボードの具体的な仕組み／対応しているすべてのガイドの網羅的な詳細


## 4. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

**概要:** OpenCodeReviewは、確定的パイプラインとLLMエージェントを組み合わせたハイブリッドなアーキテクチャを持つAIコードレビューツールです。Gitの差分や全体ファイルのスキャンを対象に、行単位の正確なレビューコメントや組込みの多言語ルールセットによるチェックを提供します。

- 言語: Go
- 今週のスター: 4032
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

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


## 5. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

**概要:** Reddit、X、YouTube、Hacker News、Polymarket、Webなど複数のプラットフォームを横断して直近30日間の情報を並行検索し、AIエージェントが評価・要約する検索エンジンツールです。

- 言語: Python
- 今週のスター: 4198
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- Reddit、X、YouTube、Hacker News、Polymarket、Webなどの複数プラットフォームを並行して横断検索する（根拠: README冒頭）

- AIエージェントの判定により、実際のエンゲージメントや投票、資金などの評価に基づいて情報を合成する（根拠: README冒頭）


### 利用例

- 商談の前に企業の直近30日間の動向や実態を把握する（README明記／根拠: Why this exists）

- ミーティングの前に相手の最近のツイートやポッドキャストの文字起こしを読み込む（README明記／根拠: Why this exists）

- 新しいものを構築する前に、人々が実際に直面している問題を確認する（README明記／根拠: Why this exists）


### 最初に試すこと

Claude Codeを使用してlast30daysスキルをインストールし、実行する

1. /plugin marketplace add mvanhorn/last30days-skill

2. /plugin install last30days

3. /last30days Peter Steinberger


成功の目安: 指定したトピックについて直近30日間の情報が要約されて出力されること

未確認: 詳細なインストール以外のすべての機能やCLIコマンドの詳細な網羅／対応している全ソースの完全な一覧とそれぞれの詳細な動作仕様


## 6. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**概要:** chrome-devtools-mcpは、コーディングエージェントがライブのChromeブラウザを制御・検査できるようにするモデルコンテキストプロトコル(MCP)サーバーおよびCLIツールです。

- 言語: TypeScript
- 今週のスター: 2795
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
- 今週のスター: 3113
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
- 今週のスター: 3792
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

**概要:** Metaで開発されたオープンソースのデザインシステムであり、人間とAIアシスタントの両方が同じツールやリファレンスで開発を行えるように設計されています。150以上のアクセシブルなコンポーネント、テーマ機能、ダークモード、CLIなどを提供しています。

- 言語: TypeScript
- 今週のスター: 3967
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 150種類以上のアクセシブルなReactコンポーネントを提供し、TypeScriptを完全にサポートしています。（根拠: Overview）

- コンポーネントのソースコードをプロジェクト内に展開して独自にカスタマイズできるswizzle機能を備えています。（根拠: Overview）

- コンポーネントのドキュメント作成、テンプレート、スキャッフォールディング、テーマ、コードモッドを実行できるCLIツールを提供しています。（根拠: Packages）


### 利用例

- 人間とAIアシスタントが同じ一貫したデザインシステムを用いてWebアプリケーションのUIを構築する。（README明記／根拠: Overview）

- Tailwind CSSやCSS Modulesなど、プロジェクト既存のスタイル手法と組み合わせてコンポーネントのスタイルを上書きする。（README明記／根拠: Overview）

- 7種類用意されたカスタマイズ可能なテーマパッケージを利用してブランド独自の配色を適用する。（README明記／根拠: Packages）


### 最初に試すこと

コアパッケージ、テーマ、CLI、および依存関係をインストールし、初期化セットアップを実行する

1. npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex

2. npm install -D @astryxdesign/cli

3. npx @astryxdesign/cli init


成功の目安: 初期化コマンドが正常に実行され、ガイドや設定ファイルが適切に保存されること

未確認: 実験的コンポーネントである@astryxdesign/labの詳細な公開スケジュールや安定版のリリース時期／@astryxdesign/vegaおよび@astryxdesign/chartsの正式な安定版リリース時期


## 10. [pookjw/HermesEnabler](https://github.com/pookjw/HermesEnabler)

**概要:** HermesEnablerは、任意のApple Watchでエルメスの文字盤を使えるようにするためのツールです。macOSまたはWindows環境でサイドロードやXcodeを使ってインストールし、Apple Watch上のアプリから設定を行います。

- 言語: Objective-C
- 今週のスター: 524
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

- [【TLA+】AIにテストケースを書かせるな。ルールを書け](https://zenn.dev/karamage/articles/73027ee36796dc) — karamage

- [自宅サーバー上のアプリケーションを Cloudflare Tunnel + Access で安全に公開する](https://zenn.dev/bisque/articles/home-server-cloudflare-tunnel-access) — bisque

- [日本のレシートを自宅PCでOCRする：15構成を実レシート11枚で比べた](https://zenn.dev/chaki/articles/4545be3475fdb4) — chaki

- [CDKからTerraformへ：所有権移譲による本番インフラ無停止のIaC移行](https://zenn.dev/levtech/articles/14befd8e727f32) — ナカジー

- [CLAUDE.md や SKILL.md のルールを Turtle で書き、ルールの書き間違いや矛盾を lint で検査してみた話](https://zenn.dev/hma2moto/articles/turtle-agent-rules-pros-cons) — hma2moto

- [自分の代わりに動くAgentへ。Claude CodeとCodexで作る自律改善ハーネス](https://zenn.dev/nttdata_tech/articles/9562962cc181a1) — Kazuma Yoshimoto | 吉本 和真

- [AIが爆速で開発する時代の、自動テストとの向き合い方](https://zenn.dev/daiaoki/articles/webterm-ai-era-testing) — Dai

- [pstack 完全ガイド ─AIエージェントに雑なコード     を書かせない技術─](https://zenn.dev/karamage/books/50c18e52e7d19e) — karamage

- [相次ぐOSSの脆弱性に、とりあえずクラウドWAF入れるだけでだいぶ違う話+Rootlessコンテナもいいぞ](https://zenn.dev/kusuke/articles/98e178e6824cac) — Yusuke Kawabata

- [tsrs を導入したら oxlint の type-aware linting と typecheck が爆速になった話](https://zenn.dev/dress_code/articles/6c179ae5129131) — ぷーじ

- [正しいUIデザインと、意図のあるUIデザイン](https://zenn.dev/praha/articles/08568310684aa3) — ゲントク

- [おい、 Mutation Test をやれ。テスト品質を、測るために](https://zenn.dev/mizchi/articles/mutation-test-quality) — mizchi

- [ローカルLLM入門](https://zenn.dev/port_inc/articles/ff974c7456f4db) — tesla

- [Claude Desktop 開発のすゝめ](https://zenn.dev/peoplex_blog/articles/vscode-to-claude-desktop) — Aki 🚀 Product Engineer @ PeopleX

- [毎月6,000 AI Agentsを捌くためにキーボードを捨てた話](https://zenn.dev/andoshin11/articles/ba68b39ef9a8ce) — Andy

- [最近、コードを真面目に読まなくなった](https://zenn.dev/hiromoo/articles/reading-less-preparing-more) — むた

- [QA生産性を爆上げさせるためのQA AIプラットフォーム構築](https://zenn.dev/gatechnologies/articles/8bdea59269eb10) — akki

- [物理世界とAIをつなぐ：可視化で学ぶカメラ・座標系・運動制御入門](https://zenn.dev/turing_motors/articles/cea9e3c85611b2) — ymg_aq

- [CSS では書きにくいアニメーションを Web Animations API で書く](https://zenn.dev/omu_tryangle/articles/b5817393592229) — hyakutake

- [mizchi/mutator を入れてみた](https://zenn.dev/polyco/articles/e05cb28c569801) — Tatsunori Nakano


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。