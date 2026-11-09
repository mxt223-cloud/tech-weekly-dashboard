# Tech Daily — 2026-11-09

生成日時: 2026-11-09T10:08:39.457707+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)

**概要:** Auto Ontologyは、企業データのメタデータからセマンティックな知識グラフやオントロジーを構築し、AIエージェントの決定論的なクエリ生成やコンテキスト取得を支援するPythonフレームワークです。

- 言語: Python
- 今週のスター: 9327
- ライセンス: Apache-2.0
- AI分析状態: ok

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


## 2. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

**概要:** claude-memは、AIコーディングエージェント向けにセッション間でコンテキストを永続化するためのツールです。エージェントの作業を記録し、AIで圧縮した上で次回のセッションに関連するコンテキストを自動的に注入します。

- 言語: TypeScript
- 今週のスター: 6443
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- エージェントのセッション中の活動やツール呼び出しを記録し、観察結果として保存する（根拠: How It Works）

- 次回のセッション開始時に、過去の観察結果から重要なインデックスをコンパクトに注入する（根拠: What You Get）

- MCP検索ツールや mem-search スキルを使用してプロジェクトの履歴を効率的に検索できる（根拠: MCP Search Tools）


### 利用例

- エージェントが過去のセッションのコンテキストを引き継ぎ、同じ質問や修正を繰り返さないようにする（README明記／根拠: README冒頭）

- 機密情報を保護するために、特定のタグで囲んだ情報を保存対象外にする（README明記／根拠: What You Get）

- チーム間で作業履歴や知見を共有し、協力して開発を進める（README明記／根拠: What You Get）


### 最初に試すこと

claude-memをインストールしてプロジェクトでのセッション記憶を有効にする

1. npx claude-mem install を実行してインタラクティブなインストーラーを起動する

2. 画面の指示に従ってエージェントの設定やサインインを行う


成功の目安: インストーラーが正常に完了し、次回のセッションで過去のセッションのコンテキストが反映されること

未確認: サードパーティ製トークンであるCMEMの具体的なユーティリティや詳細なエコシステムの位置づけ


## 3. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

**概要:** Worktrunkは、Gitのワークツリー管理を効率化し、複数のAIエージェントの並行ワークフローを支援するためのコマンドラインツールです。

- 言語: Rust
- 今週のスター: 2313
- ライセンス: NOASSERTION
- AI分析状態: ok

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




## 4. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 3169
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


## 5. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)

**概要:** Claude Codeのセッションを本格的なゲーム開発スタジオに変えるためのツールキットです。49体のAIエージェント、74種類のワークフロー用スキル（スラッシュコマンド）、自動検証フック、パス別のコーディング規約を備えており、実際のスタジオ階層を模した協調システムを提供します。

- 言語: Shell
- 今週のスター: 5235
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- デザイン、プログラミング、アート、音声、ナラティブ、QA、プロダクションの各分野に特化した49体のサブエージェントを利用できる。（根拠: What's Included）

- プロジェクトのワークフロー段階を進めるための74種類のスラッシュコマンド（スキル）を実行できる。（根拠: Slash Commands）

- Godot 4、Unity、Unreal Engine 5の主要3エンジンに対応した専門家エージェントセットを選択できる。（根拠: Engine Specialists）


### 利用例

- Claude Codeのセッション内で複数のAIエージェントを組織化し、ブレインストーミングから機能実装、レビュー、リリースまでのゲーム開発プロセス全体を構造化する。（README明記／根拠: Why This Exists）

- プロジェクトの進捗度や厳格さのレベル（modes.rigor）に応じて、必要な設計ドキュメントの作成やQA検証の度合いを制御する。（README明記／根拠: Configuration）

- 開発中のコードやアセットの変更に対して自動バリデーションフックを実行し、ハードコードやルール違反を検知・防止する。（README明記／根拠: Automated Safety）


### 最初に試すこと

リポジトリをクローンしてClaude Codeを起動し、初期セットアップと開発開始のワークフローを呼び出す。

1. git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game

2. cd my-game

3. claude

4. /start


成功の目安: Claude Codeがプロジェクトのルートディレクトリで起動し、/startコマンドによって現在のプロジェクトの状態確認やワークフローのガイドが開始されること。

未確認: 実際のゲームプレイ映像の出力品質や、特定プロジェクトにおける生成ゲームの市場での成功確率


## 6. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

**概要:** OpenMausBotは、チャットアプリの形式で複数のAIボットと会話できるオープンソースのGrok Bot代替プロジェクトです。ローカルファーストで動作し、Claude、Codex、Grokなどのエージェントを利用して独自のコンピュータ環境やアプリで作業させることができます。

- 言語: TypeScript
- 今週のスター: 7621
- ライセンス: Apache-2.0
- AI分析状態: ok

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


## 7. [pingdotgg/t3code](https://github.com/pingdotgg/t3code)

**概要:** T3 Codeは、ローカル環境にあるClaude Code、Codex、Cursor、Grok Build、OpenCode、Google Antigravity、fxなどのAIエージェントを、モバイルアプリ、Webアプリ、Electron製デスクトップアプリから一元的にコントロールするためのエージェント制御インターフェースです。

- 言語: TypeScript
- 今週のスター: 15379
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- モバイルアプリ、Webアプリ、Electron製デスクトップアプリを使ったエージェントのコントロール（根拠: README冒頭）

- Claude Code、Codex、Cursor、Grok Build、OpenCode、Google Antigravity、fxなどのプロバイダーとの連携（根拠: Installation）

- コマンドラインでのサーバー起動やバックグラウンドサービスとしての常駐、更新機能（根拠: Command line）


### 利用例

- スマートフォンなどのリモート端末から、手元のマシンで動作するAIエージェントを遠隔操作する（README明記／根拠: README冒頭）

- デスクトップアプリやWebアプリを用いて、複数の異なるAIエージェントの開発環境を統合的に管理する（README明記／根拠: README冒頭）

- インストールせずに一時的にコマンドを実行して動作を試す（README明記／根拠: Command line）


### 最初に試すこと

インストールせずに一時的にT3 Codeを試す

1. npx t3@latest


成功の目安: サーバーが起動し、ローカルのWebアプリが開くこと

未確認: 詳細なエージェント連携時の内部動作やAPI仕様／コントリビューションの受け入れ条件の詳細


## 8. [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

**概要:** Nutlope/hallmarkは、Claude Code、Cursor、Codex、OpenCode向けの「AIっぽいデザイン」を避けるためのデザインスキルです。50種類のテーマやカスタムデザイン、ブラウザでの自動lint機能などを提供し、機械的でテンプレート感のある見た目を防ぎます。

- 言語: CSS
- 今週のスター: 6356
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 50種類のテーマから適切なものを選び、ページのレイアウトや構造を構築する機能（根拠: New in v2）

- 既存のページやアプリをURL、開発サーバー、ファイルパスから指定してスクリーンショットや監査を行う機能（根拠: New in v2）

- 既存のコンテンツや配線を維持したままリデザインを行う「/hallmark redesign」や監査を行う「/hallmark audit」機能（根拠: Redesign）


### 利用例

- AIが生成したような紋切り型のデザインを避け、人間が作ったような自然なWebページを構築したい場合（README明記／根拠: README冒頭）

- 既存のWebページやアプリケーションを指定して、コンテンツの配線を変えずにデザインのリメイクや監査を行いたい場合（README明記／根拠: New in v2）

- 予約ページやショップ、ニュースレター登録など、目的のジョブに合わせたページ構造を自動で配置したい場合（README明記／根拠: New in v2）


### 最初に試すこと

hallmarkをグローバルにインストールする

1. npx skills add nutlope/hallmark -g


成功の目安: Node 18以降の環境で、パッケージが正常にインストールされること




## 9. [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu)

**概要:** GitHubリポジトリ「Renhuai123/ziwei-doushu」は、倪海厦氏の『天纪』体系に基づくTypeScript製のオープンソースの紫微斗数（中国の伝統的命理学）の命盤計算エンジンおよびデータセットです。完全な排盤アルゴリズム、四化システム、格局知識庫、古籍原文データ、大規模な解读データセットを含んでいます。

- 言語: TypeScript
- 今週のスター: 4191
- ライセンス: MIT
- AI分析状態: ok

### できること

- 真太陽時校正（経度差と均時差）や中国の夏令時判定、閏月の複数口径、晚子時換日機能を持つ完全な紫微斗数排盤エンジンを提供します。（根拠: 四排盘引擎）

- 1100行を超える規則ライブラリに基づいた紫府同宫や日月并明などの格局判定を行います。（根拠: 四排盘引擎）

- 公历1950年から2026年までの命盤をカバーする13次元解説データセットv4.0（約67.5万枚の命盤、877万段以上の解説）を利用可能です。（根拠: 二·新、13 维解读数据集 v4.0（2026-10-15））


### 利用例

- 紫微斗数の排盤アルゴリズムや伝統的な命理学の研究、およびデータ分析。（README明記／根拠: 二、51.8 万命盘样本数据集）

- 小規模なAIモデルのトレーニングコーパスや、AI対話のためのRAG（検索拡張生成）のデータソースとしての利用。（README明記／根拠: 二、51.8 万命盘样本数据集）

- 独自の紫微斗数Webアプリケーションやサービスを構築するためのオープンソースのバックエンドエンジンとしての活用。（提案／根拠: 三快速开始）


### 最初に試すこと

リポジトリをクローンして依存関係をインストールし、開発サーバーを起動してTypeScriptの型チェックとテストを実行する

1. git clone https://github.com/Renhuai123/ziwei-doushu.git

2. cd ziwei-doushu

3. npm install

4. cp .env.example .env.local

5. npm run dev

6. npm run typecheck

7. npm test


成功の目安: 開発サーバーが起動し、型チェックと排盤エンジンの回帰テスト（npm test）が正常に完了すること

未確認: オンラインの商用版フロントエンド界面や商用版の断語ライブラリ、およびバックエンドAPI（/api/interpretなど）の実装詳細／AI解釈プロンプトの具体的な内容


## 10. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**概要:** Scraplingは、高速なHTTPリクエスト、ステルスブラウザ、強力な解析機能、並行クロールを1つのライブラリに統合したPythonのWebスクレイピングフレームワークです。

- 言語: Python
- 今週のスター: 8342
- ライセンス: BSD-3-Clause
- AI分析状態: ok

### できること

- 高速なHTTPリクエスト、ステルスブラウザ、JavaScriptレンダリング、Cloudflare対策などのフェッチ機能を提供します。（根拠: What you can do with Scrapling）

- CSS、XPath、テキスト・正規表現検索、アダプティブ要素追跡などの解析・抽出機能を提供します。（根拠: What you can do with Scrapling）

- MCPサーバーやAgent SkillによるAI連携や、LLM向けにページをクリーンなMarkdownに変換する機能を提供します。（根拠: AI Features）


### 利用例

- 静的ページのスクレイピング、JavaScriptのレンダリング、Webサイトの操作、API呼び出しからのデータ抽出を行います。（README明記／根拠: README冒頭）

- 再利用可能なセッション、プロキシローテーション、自動リトライ、一時停止・再開を備えたクローラーを構築します。（README明記／根拠: README冒頭）

- Webページの内容をクリーンなMarkdownに変換し、RAGシステム向けにWebサイト全体をコーパス化します。（README明記／根拠: AI Features）


### 最初に試すこと

Scraplingをインストールして基本的なセッション付きHTTPリクエストを実行する

1. pip install scrapling

2. PythonスクリプトでFetcherSessionとimpersonate='chrome'を使用してページを取得する


成功の目安: 指定したURLからデータが正常に取得でき、セレクタによる要素の抽出ができること

未確認: 詳細な全依存関係パッケージのインストール方法／すべてのCLIコマンドの具体的使用方法



## Zenn

- [古代のグラボ（GTX 1080）でも動くローカルLLMを動かしてみた](https://zenn.dev/koheidisney/articles/729394f8be42c5) — kohei

- [自宅サーバーにClaude Codeを常駐させ、スマホから24時間指示を出す（Remote Control＋systemd）](https://zenn.dev/samurai_works/articles/114a5e654ca295) — TAKA

- [AWSから4.3億円の課金が...バグと思われる高額請求された際にまずすること](https://zenn.dev/tsumita7/articles/aoss-intelligent-ingestion-billing-202610) — Yuki Tsumita

- [SELECTしかしていないのに、PostgreSQLのマイグレーションがロック待ちで失敗した話](https://zenn.dev/naokisuzuki27/articles/cb1a5ac0e23763) — naoki

- [正規性検定による正規性チェック後の統計的仮説検定について](https://zenn.dev/tomoshige_n/articles/22e19d310acf88) — T. N.

- [Go の defer の動きをちょっと調べてみた](https://zenn.dev/wakame_atsushi/articles/8c45ac07bac534) — わかめ

- [ISUCON2026 ソロ参加記：自作ハーネスで Claude Code をほぼ無人運転した](https://zenn.dev/5alt_nacl/articles/isucon2026-solo-ai-agent) — NaCl_5alt

- [Cloudflare Zero Wire × GitHub Actions × Claude で公開サーバーの脆弱性チェックを自動化](https://zenn.dev/tomipetit/articles/zero-wire-github-actions) — tomi

- [Weight-Space Programming やってみた(やらせてみた)](https://zenn.dev/nwn/articles/cf9fe78aa33861) — ヨ

- [[破壊的変更] 明治時代の開始日が変更になって単体テストが失敗した件](https://zenn.dev/xin9le/articles/9a1cf8e10494d6) — xin9le

- [タスク管理までAIエージェントに任せたら、確認待ちに答えるだけになった](https://zenn.dev/rescuenow/articles/4c03a548cd6589) — しもち

- [米津玄師に学ぶ：一人で全部作れる時代に、なぜ人と作るのか](https://zenn.dev/tokium_dev/articles/yonezu-kenshi-why-create-with-others) — タケノコご飯

- [AI駆動文章作成において俺が意識しているテクニック集](https://zenn.dev/ntk221/articles/34ad88a9225364) — ntk

- [.NET にも build.cs 欲しいんじゃーーー](https://zenn.dev/sator_imaging/articles/c10d8da7685308) — サトー™ @sator_imaging

- [[TypeScript] パスエイリアスには Subpath Imports を使いたい](https://zenn.dev/mediba/articles/167e2a3f663889) — mdbr92

- [コードを読まずにバイブコーディングしたら、Claude Codeは分かっていてスルーしていた](https://zenn.dev/nexta_/articles/42a828ca2b8a02) — bik

- [OpenCode+Docker+GitHub Actionsで全自動AIペネトレーションテストはじめました](https://zenn.dev/team_zenn/articles/opencode-docker-actions-ai-pentest) — dyoshikawa

- [ADRをregoでlintする](https://zenn.dev/babarot/articles/regomark-adr-checker) — babarot

- [ISUCON2026 で優勝しました（当日編）](https://zenn.dev/luvtechno/articles/isucon2026-competition-day) — Yoshinori Kawasaki

- [AIが書く「読みづらいADR」に発狂しかけたので、ADRのガイドラインを作った](https://zenn.dev/tokium_dev/articles/adr-authoring-guideline) — にしこりさぶろ〜 | TOKIUM


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。