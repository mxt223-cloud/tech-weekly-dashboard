# Tech Daily — 2026-11-10

生成日時: 2026-11-10T12:44:33.344940+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)

**概要:** Auto Ontologyは、企業データのメタデータからセマンティックな知識グラフやオントロジーを構築し、AIエージェントの決定論的なクエリ生成やコンテキスト取得を支援するPythonフレームワークです。

- 言語: Python
- 今週のスター: 10159
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
- 今週のスター: 12120
- ライセンス: Apache-2.0
- AI分析状態: ok

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
- 今週のスター: 3796
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


## 4. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

**概要:** Worktrunkは、Gitのワークツリー管理を効率化し、複数のAIエージェントの並行ワークフローを支援するためのコマンドラインツールです。

- 言語: Rust
- 今週のスター: 2395
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




## 5. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

**概要:** OpenMausBotは、チャットアプリの形式で複数のAIボットと会話できるオープンソースのGrok Bot代替プロジェクトです。ローカルファーストで動作し、Claude、Codex、Grokなどのエージェントを利用して独自のコンピュータ環境やアプリで作業させることができます。

- 言語: TypeScript
- 今週のスター: 8325
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- 独自の個性やモデル、コンピュータ、接続済みアプリを持つ複数のAIボットとチャットアプリ形式でやり取りできる（根拠: README冒頭）

- 自身のマシンにインストールされたClaude、Codex、GrokのCLIを利用して追加のアカウント不要でボットを稼働させることができる（根拠: Why）

- ローカルファーストの設計により、トランスクリプトやキー、イベントをクラウドではなくローカル環境に保存する（根拠: Why）


### 利用例

- サイドバーに表示される複数のAIボットから好みのエージェントを選択し、連絡先のようにメッセージで指示を出す（README明記／根拠: README冒頭）

- 独自のクラウドLinuxデスクトップやローカルVMを活用し、AIボットに作業を代行させて進捗を確認する（README明記／根拠: Why）


### 最初に試すこと

ソースコードからローカル環境で開発サーバーとElectronアプリを起動する

1. git clone https://github.com/milind-soni/OpenMausBot && cd OpenMausBot

2. pnpm install

3. pnpm dev:server

4. pnpm dev

5. pnpm dev:desktop


成功の目安: ハーネスサーバーとアプリ、およびElectronシェルが正常に起動すること

未確認: Capabilitiesの3件目におけるプラットフォームの安全性境界に関する記述の詳細は、READMEの途中で文章が切れているため確認できません。


## 6. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

**概要:** claude-memは、AIコーディングエージェントのセッション間でコンテキストを永続化するためのツールです。エージェントの作業内容をバックグラウンドで記録・圧縮し、次回のセッション時に必要なコンテキストを自動的に注入することで、エージェントが過去の作業を引き継げるようにします。

- 言語: TypeScript
- 今週のスター: 5130
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- セッション中のエージェントの動作をバックグラウンドで記録し、AIで圧縮して次回のセッションにコンテキストを注入する。（根拠: README冒頭）

- 全文検索、タイムライン表示、詳細取得の3ステップによる効率的なメモリ検索機能を提供する。（根拠: MCP Search Tools）

- Claude CodeやOpenCodeなど複数の主要なAIエージェントやハーネスに対応している。（根拠: Quick Start）


### 利用例

- 前回のセッションで修正したバグや解決した内容を次のセッションに引き継ぎ、同じミスを繰り返さないようにする。（README明記／根拠: README冒頭）

- 自然言語を使用して過去のプロジェクト履歴を検索し、必要なコード修正の経緯や判断材料を見つける。（README明記／根拠: MCP Search Tools）


### 最初に試すこと

claude-memをインストールして動作を開始する

1. npx claude-mem install


成功の目安: インストーラーが起動し、お使いの環境にあるエージェントが検出されて設定が進められること

未確認: 商用利用における詳細なライセンスの境界条件や料金プランの全貌


## 7. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)

**概要:** Claude Codeをゲーム開発スタジオに変えるテンプレートであり、アイデアからプレイ可能なブラウザゲームのプロトタイプ作成や、チーム開発向けの多数のエージェントやスキル、ワークフローを備えています。

- 言語: Shell
- 今週のスター: 4324
- ライセンス: MIT
- AI分析状態: ok

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


## 8. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

**概要:** agent-browserは、AIエージェント向けのネイティブRust製ブラウザ自動化CLIツールです。シェルコマンドから1つずつブラウザを操作でき、ページをアクセシビリティツリーのコンパクトなテキストとしてスナップショット取得して要素の参照（ref）を返し、それに対してクリックなどの操作を行えます。

- 言語: Rust
- 今週のスター: 2994
- ライセンス: Apache-2.0
- AI分析状態: ok

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


## 9. [pingdotgg/t3code](https://github.com/pingdotgg/t3code)

**概要:** T3 Codeは、手元の開発用AIエージェントをモバイルアプリやWebアプリ、デスクトップアプリから一元的に操作・制御するためのコントロールサーフェスです。

- 言語: TypeScript
- 今週のスター: 13448
- ライセンス: MIT
- AI分析状態: ok

### できること

- iOS、Android、Web、Electronベースのデスクトップアプリからマシンの上のエージェントを制御できる（根拠: README冒頭）

- Claude Code、Codex、Cursor、Grok Build、OpenCode、Google Antigravity、fxなどのプロバイダーと連携できる（根拠: README冒頭）


### 利用例

- スマートフォンや別のマシンからリモートで開発用エージェントを操作する（README明記／根拠: README冒頭）


### 最初に試すこと

T3 Codeのサーバーを起動してローカルのWebアプリを開く

1. curl -fsSL https://t3.codes/install.sh | sh を実行してインストールする

2. t3 を実行してサーバーを起動し、ローカルのWebアプリを開く


成功の目安: t3コマンドを実行してサーバーが起動し、ローカルのWebアプリが開くこと

未確認: ソースコードの内部構造や詳細な機能についての詳細なドキュメントの内容


## 10. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**概要:** Scraplingは、高速なHTTPリクエスト、ステルスブラウザ、強力な解析、並行クロールを1つのライブラリに統合したPythonのWebスクレイピングフレームワークです。

- 言語: Python
- 今週のスター: 8226
- ライセンス: BSD-3-Clause
- AI分析状態: ok

### できること

- 高速なHTTPリクエストやステルスブラウザ、JavaScriptレンダリング、Cloudflare対策などのフェッチ機能（根拠: What you can do with Scrapling）

- CSS、XPath、テキストおよび正規表現検索、類似要素マッチングによる柔軟な解析と抽出機能（根拠: What you can do with Scrapling）

- AIチャットボットやエージェントから利用できるMCPサーバー機能およびRAG向けMarkdown変換機能（根拠: AI Features）


### 利用例

- 静的なページのスクレイピングからJavaScriptのレンダリング、API呼び出しデータの抽出（README明記／根拠: README冒頭）

- AIエージェントやLLMを活用したRAGシステム向けのクリーンなMarkdown形式への変換（README明記／根拠: AI Features）

- セッション管理やプロキシローテーション、自動リトライを伴う大規模なWebクロールの構築（README明記／根拠: README冒頭）


### 最初に試すこと

Scraplingをインストールして基本的なHTTPリクエストと解析を行う

1. pip install scrapling


成功の目安: パッケージがエラーなくインストールされること

未確認: フェッチ機能やスパイダー機能を利用する際の追加依存関係の具体的なインストールコマンド



## Zenn

- [少年団の役員向けRAGを作った — 条文単位に切り直しただけで正答52%→72%、ハイブリッド検索は効かなかった](https://zenn.dev/mappy55/articles/rulebook-rag-01) — mappy

- [ゼロから作ったMamba3言語モデルを日本語で話せる全二重音声対話モデルに拡張するまで](https://zenn.dev/taaroo/articles/47f8d1ac55d4af) — Taro

- [2 つのエージェントで異なる方向性から検証を行う](https://zenn.dev/kokagex/articles/75f89df3b007cc) — こかげ

- [JAWS FESTA 2026 in AKITA 懇親会を振り返ってみる](https://zenn.dev/k_suzuki_pnx/articles/411e236ab4f2c7) — 鈴木 健斗

- [ホロ1グランプリで宙科そぴあさんが使ってたサイエンスメソッドを最適化の視点で深掘りしてみた](https://zenn.dev/akira5kitaoka/articles/holo1gp_sopias_science_method) — Akira Kitaoka

- [なぜ mixi2 は iPhone Duo の発売初日から最適化できたのか？](https://zenn.dev/mixi/articles/b0ea64fded9503) — kuno

- [AIですぐに作れる時代に、何と向き合うか](https://zenn.dev/peoplex_blog/articles/2611-what-to-face-when-ai-builds-fast) — サカツ | PeopleX AIプロダクトエンジニア

- [LLM アプリケーションのプロンプトをどこで管理するか](https://zenn.dev/painter/articles/663816c3195cec) — Keita Ichihashi

- [閉域網でも AI を使いこなす: ローカル LLM × GitLab DAP（GitLab Epic Tour Japan 2026 登壇）](https://zenn.dev/fixstars/articles/gitlab-epic-tour-2026-local-llm) — Yoshiki Matsuda

- [ShopifyのReact Native→ネイティブ移行を支える「Reflex」をSwiftとKotlinで試す](https://zenn.dev/tellernovel_inc/articles/reflex-native-swift-kotlin) — kazutoyo@TellerNovel

- [Anthropicから毎月もらえるAPIクレジットで、AIペンテストツールShannonを回してみた](https://zenn.dev/arm_techblog/articles/9c5a29e37d1522) — Kyosuke Takayama

- [個性を磨くUI観点](https://zenn.dev/silverbirder/books/ui-craft-techniques) — silverbirder

- [週間制限に3日で到達していたClaudeが、ModelとEffortの使い分けで5日持つようになった話](https://zenn.dev/sun_asterisk/articles/1d1c65b1fe409a) — Asutin

- [Herdr.app と hc の上で Claude Code の司令塔を回している](https://zenn.dev/hoshinotsuyoshi/articles/c994c29833f36c) — hoshinotsuyoshi

- [AWSから4.3億円の課金が...バグと思われる高額請求された際にまずすること](https://zenn.dev/tsumita7/articles/aoss-intelligent-ingestion-billing-202610) — Yuki Tsumita

- [SELECTしかしていないのに、PostgreSQLのマイグレーションがロック待ちで失敗した話](https://zenn.dev/naokisuzuki27/articles/cb1a5ac0e23763) — naoki

- [ISUCON2026 ソロ参加記：自作ハーネスで Claude Code をほぼ無人運転した](https://zenn.dev/5alt_nacl/articles/isucon2026-solo-ai-agent) — NaCl_5alt

- [Weight-Space Programming やってみた(やらせてみた)](https://zenn.dev/nwn/articles/cf9fe78aa33861) — ヨ

- [[破壊的変更] 明治時代の開始日が変更になって単体テストが失敗した件](https://zenn.dev/xin9le/articles/9a1cf8e10494d6) — xin9le

- [タスク管理までAIエージェントに任せたら、確認待ちに答えるだけになった](https://zenn.dev/rescuenow/articles/4c03a548cd6589) — しもち


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。