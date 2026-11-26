# Tech Daily — 2026-11-26

生成日時: 2026-11-26T12:42:56.284407+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

**概要:** Plannotatorは、AIコーディングエージェントと人間をつなぐローカルのブラウザベースのレビュー・アノテーションツールです。プラン、仕様書、HTML、コード差分などをレビューしてフィードバックをエージェントに送り返すことができます。

- 言語: TypeScript
- 今週のスター: 1764
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- プランや仕様書、メッセージ、HTMLなどをブラウザ上でアノテーションし、エージェントにフィードバックを送信できる。（根拠: Review documents, plans, and agent messages）

- ローカルの変更やリモートのプルリクエストのコードレビューを行い、差分へのコメントやコードの提案ができる。（根拠: Code Review）

- エージェントのメッセージや質問、ファイル、ガイド付きレビューを受け取るローカルのインボックス機能を提供する。（根拠: Plannotator Inbox）


### 利用例

- エージェントが作成したプランや提案に対してブラウザ上でコメントや承認・却下を行い、エージェントの次の動作に反映させる。（README明記／根拠: Plannotator）

- GitやGitHubなどのコード差分やプルリクエストに対してコメントやコードの提案を行う。（README明記／根拠: Code Review）

- ローカルで稼働しているサイトやレンダリングされたHTMLファイルをブラウザ経由で直接コメント・確認する。（README明記／根拠: Annotate HTML artifacts and live sites）


### 最初に試すこと

Plannotatorのインストーラーを使用してツールをセットアップする

1. curl -fsSL https://plannotator.ai/install.sh | bash


成功の目安: plannotatorバイナリがインストールされ、対応するエージェントの設定が自動で行われること




## 2. [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)

**概要:** Google Stitchサーバーと連携するためのエージェントスキルおよびプラグインのコレクションです。デザイン、ビルド、ユーティリティの各カテゴリに分かれた機能を提供します。

- 言語: TypeScript
- 今週のスター: 2616
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
- 今週のスター: 2309
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


## 4. [n8n-io/nod](https://github.com/n8n-io/nod)

**概要:** n8n-io/nod は、独自のコンピュータとブラウザを操作して各種タスクを自動実行できる、オープンソースのパーソナルAIエージェントです。ユーザーの選んだAIモデルと連携し、ローカル環境で動作します。

- 言語: TypeScript
- 今週のスター: 1008
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- Gmail、Calendar、Slack、Notion、およびWebを横断して作業を遂行します。（根拠: README冒頭）

- 独自のコンピュータとブラウザを持ち、タブやログイン、フォーム入力を伴う複雑な作業を完了させます。（根拠: hard-ones）

- OpenAI、Anthropic、Gemini、OpenRouterなど20種類以上のモデルや、自前のサーバーを利用できます。（根拠: your-rules）


### 利用例

- メッセージやカレンダー、最新ニュースから1ページのコールブリーフ（要約）を作成します。（README明記／根拠: README冒頭）

- 価格表などに基づいてSlackの返信を下書きし、ユーザーの承認を得てから送信します。（README明記／根拠: README冒頭）

- スケジュールに沿ってWebページを定期的にチェックし、変更があった場合のみ通知します。（README明記／根拠: README冒頭）


### 最初に試すこと

ソースコードからnodを起動する

1. git clone https://github.com/n8n-io/nod.git

2. cd nod

3. corepack enable

4. pnpm start


成功の目安: nodがローカル環境で起動し、動作を開始すること

未確認: 完全なビルドおよび実行の前提条件であるDockerやNode.jsの具体的な初期セットアップ手順の詳細／特定のマネージドホスティングや音声通話機能の具体的なリリース時期


## 5. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

**概要:** OpenCodeReviewは、確実な決定論的パイプラインとLLMエージェントを組み合わせたハイブリッドなアーキテクチャを持つ、AIを活用したコードレビューCLIツールです。

- 言語: Go
- 今週のスター: 2259
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

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


## 6. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

**概要:** Reddit、X、YouTube、Hacker News、Polymarket、Webなどから指定したトピックに関する直近30日間の情報をAIエージェントが並行して検索・統合し、要約を提供するツールです。

- 言語: Python
- 今週のスター: 5302
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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


## 7. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**概要:** chrome-devtools-mcpは、コーディングエージェントがライブのGoogle Chromeブラウザを制御および検査できるようにするModel-Context-Protocol（MCP）サーバーおよびCLIツールです。

- 言語: TypeScript
- 今週のスター: 1203
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- パフォーマンスインサイトの取得：Chrome DevToolsを使用してトレースを記録し、実用的なパフォーマンスインサイトを抽出します。（根拠: Key features）

- 高度なブラウザデバッグ：ネットワークリクエストの分析、スクリーンショットの撮影、ソースマップ付きのスタックトレースを含むブラウザコンソールメッセージの確認を行います。（根拠: Key features）

- 信頼性の高い自動化：puppeteerを使用してChrome内のアクションを自動化し、アクションの結果を自動的に待ちます。（根拠: Key features）


### 利用例

- AIコーディングアシスタントにChrome DevToolsの機能を与え、信頼性の高い自動化、高度なデバッグ、パフォーマンス分析を実行する。（README明記／根拠: README冒頭）

- ターミナルからMCPを使用せずにCLI経由でブラウザを操作する。（README明記／根拠: CLI）

- アクセシビリティの監査や修正、クッキー・セッションのデバッグを行うためのスキルをエージェントに教え込む。（README明記／根拠: Skills）


### 最初に試すこと

MCPクライアント経由でブラウザのパフォーマンスを確認する

1. MCPクライアントに設定を追加する

2. MCPクライアントに「Check the performance of https://developers.chrome.com」というプロンプトを入力する


成功の目安: MCPクライアントがブラウザを起動し、パフォーマンスのトレースを記録すること

未確認: 対応ブラウザとしてGoogle ChromeとChrome for Testing以外で予期せぬ動作をする場合の具体的な回避策／各種ガイドに記載されている高度なパラメータの詳細な挙動


## 8. [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)

**概要:** tradermonty/claude-trading-skillsは、時間のない個人投資家向けにClaude Codeのスキルを活用した取引ワークフローツールキットです。売買の自動化ではなく、市場の確認やリスク管理、トレード計画、ジャーナル記録などの意思決定プロセスを構造化します。

- 言語: Python
- 今週のスター: 1422
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


## 9. [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)

**概要:** AG-UIは、AIエージェントとユーザー向けアプリケーションを接続するためのオープンで軽量なイベントベースのプロトコルです。フレームワークに依存せず、双方向のイベントストリームを用いてエージェントの出力をクライアントで描画できるようにします。

- 言語: TypeScript
- 今週のスター: 1421
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


## 10. [meta/astryx](https://github.com/meta/astryx)

**概要:** Metaで開発されたオープンソースのデザインシステムであり、150以上のアクセシブルなコンポーネント、テーマ機能、CLIを提供し、人間とAIアシスタントの両方が同じツールと規約でUIを構築できるように設計されています。

- 言語: TypeScript
- 今週のスター: 2635
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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



## Zenn

- [specは実装後に8割削除しよう](https://zenn.dev/ruri/articles/distill-specs-after-implementation) — atsushi ootani

- [アウトプットの「質」ってじゃあなんなんだよ](https://zenn.dev/watany/articles/1efe3adea67dd5) — watany

- [RustでFiberを用いたJob Systemを実装したらReleaseビルドでバグが発生した](https://zenn.dev/otinpan/articles/082f6178eb1472) — otinpan

- [結局「オントロジー」って何なのさ 〜概念と良さを4つのレイヤーで整理する〜](https://zenn.dev/algomatic/articles/ece749a7e3cb24) — ひさふる

- [AIを使った開発に「敵対的検証」を取り入れてみた](https://zenn.dev/visionarray/articles/26b316ff128513) — H.Murayama

- [【自動化】Muse のサイドチャットへ Webhook を届ける MuseKnock の仕組み](https://zenn.dev/codehex/articles/33bc6ee330b880) — codehex

- [AIエージェントのMemory設計 ― 会話履歴・業務データ・長期Memoryの使い分け](https://zenn.dev/taru_neko/articles/ai-agent-memory-architecture-2026) — 樽猫先生

- [Claude Code のセキュリティ、2026年11月時点のベストプラクティス（サンドボックス・権限・MCP）](https://zenn.dev/happy_elements/articles/27e14ff6754044) — ko.+

- [Personal Agent Protocol (Poppy) が解く問題と仕組み](https://zenn.dev/sierra_japan/articles/0b9ba590232345) — konippi

- [なんとなくgrill-meしている人に伝えたい、作者本人から学んだSkillsの使い方](https://zenn.dev/mediaforce/articles/27df1f22a00546) — Kosuke Ikeda

- [モデルの性能が出ないのは AI ゲートウェイのせいかもしれない](https://zenn.dev/google_cloud_jp/articles/7e29a9acf06557) — Kentaro Takiguchi

- [マーダーミステリーのシナリオを形式手法で検証しようとしたら、バグと曖昧さが見つかった](https://zenn.dev/henteko/articles/ed8d1458246d7a) — henteko

- [Gemini 4 Neon を API で叩いて Claude Code・Codex CLI と比べた：65万トークンの超長文、費用、失敗](https://zenn.dev/canly/articles/40e773759da8f8) — haginota

- [エンジニア20人の組織を、デザイナー1人と AI で支える仕組み](https://zenn.dev/rimo/articles/c25919207b1cde) — にしゃみー

- [Claude Code の /ship を図解する](https://zenn.dev/peoplex_blog/articles/claude-code-ship) — Aki 🚀 Product Engineer @ PeopleX

- [Claude Code を5〜8個並べても迷わないように、自分用のダッシュボードをバイブコーディングで作った](https://zenn.dev/nexta_/articles/a3ff76a9f98f1c) — bik

- [JSConf JP 2026 公開資料・Xアカウントリンクまとめ](https://zenn.dev/h_yoshikawa0724/articles/2026-11-23-jsconf-jp-2026) — よし

- [著名なRust製OSSをLean 4で形式検証してみたら、めちゃめちゃバグが見つかった話](https://zenn.dev/koukyosyumei/articles/31c8fcf4da45b7) — Koukyosyumei

- [プログラミング教育の功罪](https://zenn.dev/nobkz/articles/a8ed5591cd3e7d) — Nobkz

- [寝てる間に自動で動くAIエージェントを誰でも作れる：10分でわかる pstack 実践ガイド](https://zenn.dev/canly/articles/ca6875cd79539f) — haginota


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。