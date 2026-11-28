# Tech Daily — 2026-11-28

生成日時: 2026-11-28T12:27:12.025259+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

**概要:** Plannotatorは、AIコーディングエージェントと人間をつなぐローカルのブラウザベースのレビュー・アノテーションツールです。プラン、仕様書、HTML、コード差分などをレビューしてフィードバックをエージェントに送り返すことができます。

- 言語: TypeScript
- 今週のスター: 1596
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

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
- 今週のスター: 2008
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
- 今週のスター: 1424
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

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
- 今週のスター: 2335
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

**概要:** Reddit、X、YouTube、Hacker News、Polymarket、Webなどを横断してトピックを調査し、AIエージェントが根拠のある要約を生成する検索エンジンスキルです。

- 言語: Python
- 今週のスター: 5072
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- Reddit、X、YouTube、TikTok、Polymarket、GitHubなどの複数プラットフォームを並行して検索し、AIエージェントが要約を作成する（根拠: README冒頭）

- アップボート、いいね、実際の資金（Polymarketなど）のスコアに基づいて情報を評価する（根拠: README冒頭）


### 利用例

- ビジネスの直近30日間の動向を営業活動の前に調査する（README明記／根拠: Why this exists）

- ミーティングの前に相手の最近のツイートやポッドキャストのトランスクリプトを読み込む（README明記／根拠: Why this exists）

- 何かを構築する前に、人々が実際に直面している問題を確認する（README明記／根拠: Why this exists）


### 最初に試すこと

Claude Codeを使用してスキルをインストールし、検索を実行する

1. /plugin marketplace add mvanhorn/last30days-skill

2. /plugin install last30days

3. /last30days Peter Steinberger


成功の目安: 指定したトピックについての調査結果がAIエージェントによって要約されること

未確認: 具体的なAPIキーの設定画面や詳細な設定手順の全容／対応している全ホスト環境の完全なリスト


## 7. [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

**概要:** chrome-devtools-mcpは、コーディングエージェントがライブのGoogle Chromeブラウザを制御および検査できるようにするModel-Context-Protocol（MCP）サーバーおよびCLIツールです。信頼性の高い自動化、詳細なデバッグ、パフォーマンス分析を提供します。

- 言語: TypeScript
- 今週のスター: 1150
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- Chrome DevToolsを使用してトレースを記録し、パフォーマンスに関する洞察を抽出する（根拠: Key features）

- ネットワークリクエストの分析、スクリーンショットの撮影、ブラウザコンソールメッセージの確認を行う（根拠: Key features）

- puppeteerを使用してChrome内のアクションを自動化し、アクション結果を自動的に待機する（根拠: Key features）


### 利用例

- Webページのパフォーマンスを確認し、トレーシングデータを記録する（README明記／根拠: Getting started）

- コマンドラインからページを操作し、スクリーンショットを保存する（README明記／根拠: CLI）

- アクセシビリティの問題やクッキー、メモリリークなどのデバッグを行う（README明記／根拠: Skills）


### 最初に試すこと

MCPクライアントからブラウザを起動し、指定したURLのパフォーマンスを確認する

1. MCPクライアントに設定を追加する

2. MCPクライアントにプロンプト「Check the performance of https://developers.chrome.com」を入力する


成功の目安: MCPクライアントがブラウザを開き、パフォーマンスのトレースを記録すること




## 8. [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills)

**概要:** tradermonty/claude-trading-skills は、時間のない個人投資家向けに市場分析、リスク管理、取引計画、ジャーナル記録などを構造化するための Claude Skills ベースの取引ワークフローツールキットです。

- 言語: Python
- 今週のスター: 1332
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 15分間の日次市場チェック（市場の幅や上昇トレンドの分析など）を実行できる（根拠: Recommended Starting Path）

- 週次の長期ポートフォリオ見直しや配当モニタリングを行うことができる（根拠: Recommended Starting Path）

- リスクが許容される場合にのみスイング取引の候補を探すことができる（根拠: Recommended Starting Path）


### 利用例

- 日々の限られた時間の中で効率的に市場状況を確認したい（README明記／根拠: Recommended Starting Path）

- 長期投資や配当株・ETFを中心に据えつつ、規律あるスイング取引を行いたい（README明記／根拠: Claude Trading Skills）

- 取引の記録と振り返り（ジャーナル）を通じて意思決定プロセスを改善したい（README明記／根拠: Recommended Starting Path）


### 最初に試すこと

プロバイダーのキーなしでフィクションのレポートとNavigatorを確認する

1. Offline Quick Start (docs/en/offline-quickstart.md) を参照する


成功の目安: プロバイダーキーなしでフィクションのレポートとNavigatorを確認できること

未確認: 具体的なインストールコマンドや具体的なセットアップ手順の詳細／利用可能なすべてのAPIキーの全リストやその設定コマンド


## 9. [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)

**概要:** AG-UIは、AIエージェントとユーザー向けアプリケーションを接続するためのオープンで軽量なイベントベースのプロトコルです。フレームワークに依存せず、双方向のイベントストリームを用いてエージェントの出力をクライアントで描画できるようにします。

- 言語: TypeScript
- 今週のスター: 1185
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
- 今週のスター: 2306
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

- [Leanで安全制約を書くと、ハザード候補がビルドエラーとして見つかる](https://zenn.dev/kokeshim0chi/articles/lean-safety-constraint-build-error) — kokeshiM0chi

- [GitHub ActionsからPATもGitHub App Private Keyも駆逐する](https://zenn.dev/tmknom/articles/github-app-token-exchange-system) — tmknom

- [禁止しても止まらないClaudeの「欲」を飼いならしてみる](https://zenn.dev/rescuenow/articles/9d1e89a941f4f1) — しもち

- [止められないDBをAWS DMSで移行してハマったこと（RDS for Oracle）](https://zenn.dev/kiri0728/articles/c8d5f349b047dd) — Takuma Kiritoshi

- [日本語のFull-duplex音声対話モデルを実際に動かしてみた話](https://zenn.dev/knowledgework/articles/12a80d8cd4b21f) — mine

- [自宅PCを格安ファイルサーバーとして構築してみた](https://zenn.dev/nextbeat/articles/7c820845a91d7d) — HiCurl

- [AIエージェントにWebのファイルを取得させるリスクについて考える](https://zenn.dev/layerx/articles/65b4828efcaee2) — Tomoya Kudo

- [迷惑メール対策をしているのに、なぜ詐欺メールは届くのか](https://zenn.dev/akagumi/articles/catch-all-phishing-invisible-chars) — えだまめ

- [自動運転の予測軌跡の可視化動画を誰でも高速に作れるようにする](https://zenn.dev/turing_motors/articles/cbf9872ca90166) — studio_graph

- [作業を止めずに進めるClaude Codeの/btw・/fork・/rewindなどの使い分け](https://zenn.dev/nextbeat/articles/b0ccca979da06b) — sato222

- [アウトプットの「質」ってじゃあなんなんだよ](https://zenn.dev/watany/articles/1efe3adea67dd5) — watany

- [結局「オントロジー」って何なのさ 〜概念と良さを4つのレイヤーで整理する〜](https://zenn.dev/algomatic/articles/ece749a7e3cb24) — ひさふる

- [【自動化】Muse のサイドチャットへ Webhook を届ける MuseKnock の仕組み](https://zenn.dev/codehex/articles/33bc6ee330b880) — codehex

- [Claude Code のセキュリティ、2026年11月時点のベストプラクティス（サンドボックス・権限・MCP）](https://zenn.dev/happy_elements/articles/27e14ff6754044) — ko.+

- [なんとなくgrill-meしている人に伝えたい、作者本人から学んだSkillsの使い方](https://zenn.dev/mediaforce/articles/27df1f22a00546) — Kosuke Ikeda

- [モデルの性能が出ないのは AI ゲートウェイのせいかもしれない](https://zenn.dev/google_cloud_jp/articles/7e29a9acf06557) — Kentaro Takiguchi

- [Claude Code の /ship を図解する](https://zenn.dev/peoplex_blog/articles/claude-code-ship) — Aki 🚀 Product Engineer @ PeopleX

- [Claude Code を5〜8個並べても迷わないように、自分用のダッシュボードをバイブコーディングで作った](https://zenn.dev/nexta_/articles/a3ff76a9f98f1c) — bik

- [JSConf JP 2026 公開資料・Xアカウントリンクまとめ](https://zenn.dev/h_yoshikawa0724/articles/2026-11-23-jsconf-jp-2026) — よし

- [著名なRust製OSSをLean 4で形式検証してみたら、めちゃめちゃバグが見つかった話](https://zenn.dev/koukyosyumei/articles/31c8fcf4da45b7) — Koukyosyumei


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。