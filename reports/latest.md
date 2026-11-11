# Tech Daily — 2026-11-11

生成日時: 2026-11-11T10:25:02.444406+09:00  
AI分析: 9/10件成功（gemini-3.5-flash-lite）


## 1. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)

**概要:** Auto Ontologyは、企業データのメタデータからセマンティックな知識グラフやオントロジーを構築し、AIエージェントの決定論的なクエリ生成やコンテキスト取得を支援するPythonフレームワークです。

- 言語: Python
- 今週のスター: 9621
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- メタデータから企業向けオントロジーを生成し、知識グラフを構築する（根拠: README冒頭）

- 自然言語の質問をSQLに翻訳し、接続されたデータベースに対して実行する（根拠: Key Features）

- MCP、CLI、APIを通じて任意のAIエージェントにコンテキストを提供する（根拠: README冒頭）


### 利用例

- リレーショナルソース上のセマンティックカタログ層として利用し、データの意味や関係性をエージェントに与える（README明記／根拠: Key Features）

- Web UIのチャット、分析、データカタログ機能を通じてデータ分析や設定を行う（README明記／根拠: Key Features）

- MCPサーバーを用いて任意のMCPクライアントからオントロジーに対する読み取り専用ツールにアクセスする（README明記／根拠: Use it from your agent）


### 最初に試すこと

Docker Composeを使用してAuto-Ontologyをローカル環境で起動し、サンプルデータベースに対する質問応答を確認する

1. git clone https://github.com/NVIDIA/auto-ontology.git && cd auto-ontology

2. cp .env.example .env

3. docker compose up -d --wait postgres

4. git clone https://github.com/NVIDIA/auto-ontology-eval.git ../auto-ontology-eval

5. docker compose up -d --build


成功の目安: ブラウザで http://localhost:3000 を開き、ログイン後にセマンティックコンパイルが完了し、チャットで質問に対してSQLと回答が返ってくること

未確認: 外部からのプルリクエストの受け入れ可否（現在のREADMEでは非受付と記載されているが将来の変更可能性は不明）／KumoRFM以外の予測サービスの具体的な統合方法


## 2. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)

**概要:** agent-desktopは、AIエージェントがOSのアクセシビリティツリーを介してmacOS、Windows、Linux上のデスクトップアプリを視認・操作できるようにするコンピュータ操作用CLIおよびCライブラリです。

- 言語: Rust
- 今週のスター: 9502
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- スクリーンショットやピクセルマッチングを行わず、デスクトップアプリのアクセシビリティツリーを読み取ってJSONとして返す機能（根拠: README冒頭）

- CLIやCライブラリとして提供され、MCP（Model Context Protocol）ツールとしても各コマンドを提供してstdio経由で実行できる機能（根拠: MCP）

- スナップショット、要素へのクリックや文字入力、ウィンドウやアプリの管理、クリップボード操作など多数の運用コマンドを備えている機能（根拠: Commands）


### 利用例

- AIエージェントがデスクトップアプリのUI要素を認識してクリックや入力を実行し、結果を検証する自動化ループの構築（README明記／根拠: README冒頭）

- Model Context Protocol（MCP）に対応したAIエージェントのインフラやクライアントにデスクトップ操作機能を組み込むこと（提案／根拠: MCP）


### 最初に試すこと

デスクトップアプリの状態をスナップショットで取得し、対象の要素に対して操作を行うこと

1. agent-desktop snapshot --app Finder -i

2. agent-desktop click @s8f3k2p9:e8

3. agent-desktop snapshot --app Finder -i


成功の目安: コマンドがJSONエンベロープを出力し、UI要素の情報や操作結果が確認できること

未確認: READMEに記載されていない詳細な内部アーキテクチャや独自拡張機能の有無


## 3. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 5014
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


## 4. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

**概要:** OpenMausBotは、Grok Botにインスパイアされたオープンソースのチャットアプリ型AIボットプラットフォームです。ローカルで動作するClaudeやCodexなどのAIエージェントを、連絡先のようにチャット形式で管理・操作できます。

- 言語: TypeScript
- 今週のスター: 8951
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- ClaudeやCodex、GrokなどのAIエージェントCLIをローカル環境で直接利用できる（根拠: Why）

- macOS、Windows、Ubuntu向けのデスクトップアプリとしてビルド・実行できる（根拠: Quick start）

- 内蔵されたハーネスサーバーにより、追加のサーバー設定なしで動作する（根拠: Quick start）


### 利用例

- 複数のAIボットとチャットアプリのように会話しながら作業を進める（README明記／根拠: README冒頭）

- ローカルにインストールされたAIモデルやエージェントを活用してタスクを実行する（README明記／根拠: Why）


### 最初に試すこと

ソースコードから開発サーバーを起動してアプリを動作させる

1. git clone https://github.com/milind-soni/OpenMausBot && cd OpenMausBot

2. pnpm install

3. pnpm dev:server

4. pnpm dev


成功の目安: ハーネスサーバーおよびアプリが指定されたローカルアドレスで起動すること

未確認: Featuresセクションの具体的な詳細内容（途中で切れているため）／Tailscaleを用いたデスクトップ間コンパニオンモードの詳細な手順


## 5. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

**概要:** Worktrunkは、Gitのワークツリー管理を効率化し、複数のAIエージェントの並行ワークフローを支援するためのコマンドラインツールです。

- 言語: Rust
- 今週のスター: 2093
- ライセンス: NOASSERTION
- AI分析状態: ok（キャッシュ）

### できること

- ブランチ名を用いたワークツリーの切り替えや作成、削除などの基本操作を行える（根拠: README）

- フック機能によるワークツリー作成時やマージ前後のワークフロー自動化を行える（根拠: README）

- 差分からLLMを活用したコミットメッセージの生成を行える（根拠: README）


### 利用例

- Claude CodeなどのAIエージェントを複数のワークツリーで同時に稼働させ、並行してタスクを処理する（README明記／根拠: README）

- ワークツリーごとに固有のポート番号や開発サーバー割り当てを行い、環境競合を防ぐ（README明記／根拠: README）

- 複数ワークツリー間でビルドキャッシュを共有し、ディスク容量やビルド時間を節約する（README明記／根拠: README）


### 最初に試すこと

新しい機能用のワークツリーを作成して切り替える

1. wt switch --create feature-auth


成功の目安: 新しいブランチとワークツリーが作成され、そこに切り替わること




## 6. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

**概要:** agent-browserは、AIエージェント向けのネイティブRust製ブラウザ自動化CLIツールです。シェルコマンドから1つずつブラウザを操作でき、ページをアクセシビリティツリーのコンパクトなテキストとしてスナップショット取得して要素の参照（ref）を返し、それに対してクリックなどの操作を行えます。

- 言語: Rust
- 今週のスター: 3606
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


## 7. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)

**概要:** Claude Codeをゲーム開発スタジオに変えるテンプレートであり、アイデアからプレイ可能なブラウザゲームのプロトタイプ作成や、チーム開発向けの多数のエージェントやスキル、ワークフローを備えています。

- 言語: Shell
- 今週のスター: 3730
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- アイデアを元に質問を行い、1ページのゲーム企画書とプレイ可能なブラウザゲームを自動で構築する。（根拠: Make me a game）

- Web、Godot 4、Unity、Unreal Engine 5などの複数エンジンをサポートする。（根拠: Engines）

- 49体のAIエージェントと75種類のスキル（スラッシュコマンド）によるスタジオモードを提供する。（根拠: Studio Mode）


### 利用例

- テキストでアイデアを入力し、ブラウザゲームのプロトタイプをすばやく作成する。（README明記／根拠: Make me a game）

- 既存のブラウザゲームをインポートして変更や機能追加を行う。（README明記／根拠: Make me a game）

- プロジェクトの進行度や規模に応じて開発プロセスの厳格さを設定する。（README明記／根拠: Configuration）


### 最初に試すこと

リポジトリをクローンしてClaude Codeを起動し、プロトタイプ作成コマンドを実行する

1. git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game

2. cd my-game

3. claude

4. /prototype a fishing game where the rare fish only bite at dusk


成功の目安: Claude Codeが起動し、ゲームのプロトタイプ作成プロセスが開始されること

未確認: macOSやLinux環境におけるデスクトップ通知機能の動作詳細


## 8. [mattpocock/skills](https://github.com/mattpocock/skills)

**概要:** mattpocock/skillsは、Claude Code、Codex、GitHub CopilotなどのAIコーディングエージェント向けに設計された、小型で拡張可能なエージェントスキルのコレクションです。要件定義の精緻化、共有言語の構築、テスト駆動開発（TDD）、コードベースのアーキテクチャ改善など、実際のソフトウェアエンジニアリングを支援する様々なスキルを提供します。

- 言語: Shell
- 今週のスター: 9872
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- Claude Code、Codex、GitHub Copilot、Gemini CLIなど、様々なエージェント環境へのプラグインとしてインストール可能。（根拠: Installation (30-second setup)）

- エージェントに詳細な質問をさせることで認識のズレを防ぐ、要件確認セッション機能。（根拠: Why These Skills Exist）

- コードベースのアーキテクチャ改善機会をスキャンし、視覚的なHTMLレポートとして提示する機能。（根拠: Engineering）


### 利用例

- 実装前にエージェントから詳細な質問を引き出し、作りたいものへの認識を合わせる。（README明記／根拠: Why These Skills Exist）

- テスト駆動開発（TDD）の赤-緑-リファクターループをエージェントに実践させ、高品質なコードを維持する。（README明記／根拠: Why These Skills Exist）

- プロジェクト固有の専門用語や用語集（GLOSSARY.md）をエージェントと共有し、冗長な説明を減らしてコンテキスト理解を効率化する。（README明記／根拠: Why These Skills Exist）


### 最初に試すこと

リポジトリの初期設定を行い、エンジニアリングスキルを利用可能な状態にする

1. エージェント向けにスキルをインストールする（例: npx skills@latest add mattpocock/skills）

2. エージェント内で /setup-matt-pocock-skills を実行する


成功の目安: イシュートラッカーやトリアージラベル、ドキュメントの保存先を設定するプロンプトが正常に完了すること

未確認: 具体的なスキルの内部実装の詳細や、AIモデルごとの挙動の差異


## 9. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

**概要:** cloudflare/security-audit-skillは、コーディングエージェントをセキュリティ監査人に変えるスキルリポジトリです。偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成という6つのフェーズで構造化されたセキュリティ監査を実行します。

- 言語: JavaScript
- 今週のスター: 10967
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 6つのフェーズ（偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成）で構造化されたセキュリティ監査を実行する。（根拠: What it does）

- findings.jsonやcoverage-ledger.jsonなどの出力を検証するためのバリデーター（validate-findings.cjs、validate-coverage-ledger.cjs）を提供する。（根拠: Files）

- 同じリポジトリに対する複数回の実行で結果が加算的になり、ギャップのターゲット設定や変更されたソースの再検証を行う。（根拠: What it does）


### 利用例

- コードベース全体のセキュリティ監査をエージェントに実行させる。（README明記／根拠: Usage）

- 指定したディレクトリ（./srcなど）内のセキュリティ脆弱性を発見する。（README明記／根拠: Usage）

- セキュリティレビューを実施し、特定の結果を指定の出力先に出力する。（README明記／根拠: Usage）


### 最初に試すこと

Skills CLIを使用してsecurity-auditスキルをインストールする

1. npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit


成功の目安: スキルが正常にインストールされること




## 10. [The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent)

**概要:** 🚀 PR Agent: The Original Open-Source PR Reviewer. This project is not the Qodo free tier.

- 言語: Python
- 今週のスター: 1591
- ライセンス: MIT
- AI分析状態: api_error

### できること

- READMEから確認できませんでした。


### 利用例

- READMEから確認できませんでした。


### 最初に試すこと

未確認


成功の目安: 未確認

未確認: Gemini API HTTP 503: {
  "error": {
    "code": 503,
    "message": "This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.",
    "status": "UNAVAILABLE"
  }
}




## Zenn

- [HAC125DX 用の無線カメラを Pi Zero 2 W で作って、ライブスタックしてみた](https://zenn.dev/tsukitsukiss/articles/livestack-hac125dx-wireless-camera) — tsuki

- [LiteLLM Adaptive Routerを検証する（後編）：学習シグナルと運用上の注意](https://zenn.dev/aws_japan/articles/4399262cf00559) — Hiroki Tsuji

- [LiteLLM Adaptive Router を検証する（前編）：モデル選択と学習の仕組み](https://zenn.dev/aws_japan/articles/ac9ae548d57323) — Hiroki Tsuji

- [Clojureのマクロによるメタプログラミングで業務ルールのDSLを作る](https://zenn.dev/pksha/articles/b7e4c1a9d38f52) — Hyuga Yamaguchi

- [JaCoCoはどうやってカバレッジを測っているのか](https://zenn.dev/chikina/articles/jacoco-coverage-bytecode) — ちきな

- [AI ネイティブなデータ分析基盤を作った話（後編）](https://zenn.dev/pksha/articles/laplace-build-guide) — Shogun

- [AIでテストカバレッジを23%から84%に引き上げた方法](https://zenn.dev/litalico/articles/20261029-test-with-ai) — eggc

- [GitHub rulesetのON/OFFで「マージ禁止期間」を作る](https://zenn.dev/yesodco/articles/yesod-github-ruleset-merge-freeze) — ik-fib

- [退屈なCoding AgentはMuseにやらせよう](https://zenn.dev/watany/articles/342b9815dd0553) — watany

- [NVIDIAの「長文コンテキスト不要」論文](https://zenn.dev/knowledgesense/articles/bd917ed6829121) — Atsushi Kadowaki

- [「漏洩された側」は何ができるのか？ 相次ぐインシデントから考えるエンドユーザーの防衛策](https://zenn.dev/nttdata_tech/articles/a68fc15144b2d8) — Rikita Koshiba

- [Claude Codeで最近使っているTips【2026/11】](https://zenn.dev/oikon/articles/claude-code-recipe) — Oikon

- [脆弱性問題を解決するためにRustに移行するべきなのか？](https://zenn.dev/garasubo/articles/72340052cdd871) — ガラスボー

- [JAWS FESTA 2026 in AKITA 懇親会を振り返ってみる](https://zenn.dev/k_suzuki_pnx/articles/411e236ab4f2c7) — 鈴木 健斗

- [なぜ mixi2 は iPhone Duo の発売初日から最適化できたのか？](https://zenn.dev/mixi/articles/b0ea64fded9503) — kuno

- [AIですぐに作れる時代に、何と向き合うか](https://zenn.dev/peoplex_blog/articles/2611-what-to-face-when-ai-builds-fast) — サカツ | PeopleX AIプロダクトエンジニア

- [個性を磨くUI観点](https://zenn.dev/silverbirder/books/ui-craft-techniques) — silverbirder

- [週間制限に3日で到達していたClaudeが、ModelとEffortの使い分けで5日持つようになった話](https://zenn.dev/sun_asterisk/articles/1d1c65b1fe409a) — Asutin

- [AWSから4.3億円の課金が...バグと思われる高額請求された際にまずすること](https://zenn.dev/tsumita7/articles/aoss-intelligent-ingestion-billing-202610) — Yuki Tsumita

- [[破壊的変更] 明治時代の開始日が変更になって単体テストが失敗した件](https://zenn.dev/xin9le/articles/9a1cf8e10494d6) — xin9le


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。