# Tech Daily — 2026-11-08

生成日時: 2026-11-08T09:52:19.596787+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

**概要:** claude-memは、AIコーディングエージェントのセッション間で永続的なコンテキストを維持するためのツールです。エージェントの作業内容をキャプチャしてAIで圧縮し、次回のセッションに適切なコンテキストを自動で注入します。Claude Codeやその他の主要なエージェントに対応しています。

- 言語: TypeScript
- 今週のスター: 7482
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- セッション間の自動記憶：エージェントの作業内容を記録し、次のセッションの開始時に必要なコンテキストを注入する。（根拠: What You Get）

- MCP検索ツールによるプロジェクト履歴の検索：インデックス、タイムライン、詳細の3段階で効率的な検索を行う。（根拠: MCP Search Tools）

- プライバシー保護機能：<private>タグで囲んだ内容を保存対象外にできる。（根拠: What You Get）


### 利用例

- 過去のセッションで解決した修正内容や進捗を次のセッションへ引き継ぎ、ゼロからやり直す手間を省く。（README明記／根拠: What You Get）

- 自然言語を用いたプロジェクト履歴の検索により、過去の作業内容やバグ修正の経緯を効率的に見つける。（README明記／根拠: MCP Search Tools）

- シークレット情報を秘匿した状態でエージェントに安全に作業を記憶させる。（README明記／根拠: What You Get）


### 最初に試すこと

claude-memをインストールしてプロジェクトの記憶機能を開始する

1. npx claude-mem install


成功の目安: インストーラーが起動し、使用するエージェントの選択やセットアップが完了すること

未確認: セッションの記録や圧縮に利用される具体的なAIモデルの内部仕様の詳細


## 2. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

**概要:** Worktrunkは、Gitワークツリーの管理を効率化し、複数のAIエージェントを並行して実行しやすくするためのコマンドラインツールです。

- 言語: Rust
- 今週のスター: 2292
- ライセンス: NOASSERTION
- AI分析状態: ok（キャッシュ）

### できること

- ブランチ名を指定してワークツリーの切り替えや作成、削除を行える（根拠: Worktrunk makes git worktrees as easy as branches）

- ワークツリーの一覧をステータス付きで表示できる（根拠: Worktrunk makes git worktrees as easy as branches）

- フック機能によるワークフローの自動化や、LLMを活用したコミットメッセージの生成が行える（根拠: Worktrunk makes git worktrees as easy as branches）


### 利用例

- 複数のAIエージェントにそれぞれ独立した作業用ディレクトリを割り当てて並行作業させる（README明記／根拠: Context: git worktrees）

- ワークツリーを作成すると同時にClaudeなどのエージェントを起動して開発を始める（README明記／根拠: Worktrunk makes git worktrees as easy as branches）

- 作業が完了したワークツリーをマージして不要になったブランチとともに一括で削除する（README明記／根拠: Quick start）


### 最初に試すこと

新しい機能用のワークツリーを作成して切り替える

1. wt switch --create feature-auth


成功の目安: 新しいブランチとワークツリーが作成され、そこに切り替わっていること

未確認: 詳細な設定ファイルやフックのカスタムスクリプトの全仕様


## 3. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)

**概要:** Claude Codeのセッションを本格的なゲーム開発スタジオに変えるためのツールキットです。49体のAIエージェント、74種類のワークフロー用スキル（スラッシュコマンド）、自動検証フック、パス別のコーディング規約を備えており、実際のスタジオ階層を模した協調システムを提供します。

- 言語: Shell
- 今週のスター: 5719
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


## 4. [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu)

**概要:** GitHubリポジトリ「Renhuai123/ziwei-doushu」は、倪海厦氏の『天纪』体系に基づいたTypeScript製のオープンソースの紫微斗数排盘（命盤作成）エンジンです。完全な排盘アルゴリズム、四化システム、格局知識庫、古籍原文データ、さらに数百万件規模の解读データセットを含みます。

- 言語: TypeScript
- 今週のスター: 4906
- ライセンス: MIT
- AI分析状態: ok

### できること

- 真太陽時校正（経度差と均時差の計算）に対応しています。（根拠: 四排盘引擎）

- 1986年から1991年までの中国夏令時（サマータイム）の判定機能を備えています。（根拠: 四排盘引擎）

- 紫府同宫や日月并明などのクラシックな格局の判定規則を含む1100行以上の格局知識庫を提供します。（根拠: 四排盘引擎）


### 利用例

- 小規模言語モデル（LLM）の微調整（Fine-tuning）の学習用コーパスとして活用できます。（README明記／根拠: 二、51.8 万命盘样本数据集）

- AI対話のためのRAG（検索拡張生成）の検索ソースとして利用できます。（README明記／根拠: 二、51.8 万命盘样本数据集）

- 独自の紫微斗数アプリケーションの開発において、オープンソースの排盤エンジンやデータベースとして組み込むことができます。（提案／根拠: 三、快速开始）


### 最初に試すこと

リポジトリをクローンして依存関係をインストールし、開発サーバーを起動してローカル環境でエンジンを動作させること。

1. git clone https://github.com/Renhuai123/ziwei-doushu.git

2. cd ziwei-doushu

3. npm install

4. npm run dev


成功の目安: 開発サーバーが正常に起動し、ローカル環境で排盤アプリのインターフェースを確認できること。

未確認: AI解読（/api/interpret）や合算AI分析（/api/heming）の具体的なAPI内部実装の全容／商用版オンラインプラットフォームの詳細なフロントエンドコード


## 5. [pingdotgg/t3code](https://github.com/pingdotgg/t3code)

**概要:** T3 Codeは、ローカル環境にあるClaude Code、Codex、Cursor、Grok Build、OpenCode、Google Antigravity、fxなどのAIエージェントを、モバイルアプリ、Webアプリ、Electron製デスクトップアプリから一元的にコントロールするためのエージェント制御インターフェースです。

- 言語: TypeScript
- 今週のスター: 17100
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


## 6. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 2796
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


## 7. [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

**概要:** Nutlope/hallmarkは、Claude Code、Cursor、Codex、OpenCode向けの「AIっぽいデザイン」を避けるためのデザインスキルです。50種類のテーマやカスタムデザイン、ブラウザでの自動lint機能などを提供し、機械的でテンプレート感のある見た目を防ぎます。

- 言語: CSS
- 今週のスター: 6624
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




## 8. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

**概要:** OpenMausBotは、Grok BotにインスパイアされたオープンソースのAIチャットアプリです。ClaudeやCodexなどのAIエージェントとメッセージアプリのように会話でき、ローカルファーストで動作します。

- 言語: TypeScript
- 今週のスター: 7077
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- ClaudeやCodex、GrokのCLIを利用したAIエージェントの実行（根拠: Why）

- ローカルファーストでのデータ管理（トランスクリプトやキーなどが~/.openmausbotに保存される）（根拠: Why）

- ElectronベースのデスクトップアプリとしてmacOS、Windows、Ubuntuで動作（根拠: Quick start）


### 利用例

- サイドバーにいる複数のAIボットとチャットアプリ感覚で会話する（README明記／根拠: README冒頭）

- 既存のローカル環境のサブスクリプションやログイン情報をそのまま用いてAIエージェントを動かす（README明記／根拠: Why）


### 最初に試すこと

ソースコードから開発環境サーバーおよびデスクトップシェルを起動する

1. git clone https://github.com/milind-soni/OpenMausBot && cd OpenMausBot

2. pnpm install

3. pnpm dev:server

4. pnpm dev

5. pnpm dev:desktop


成功の目安: ハーネスサーバーやElectronシェルが起動し、アプリケーションが動作すること

未確認: Featuresセクション以降のコンテンツがREADME内で途中で途切れているため、機能の詳細の一部


## 9. [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)

**概要:** Scraplingは、高速なHTTPリクエスト、ステルスブラウザ、強力な解析機能、並行クローリングを1つに統合したPythonのWebスクレイピングフレームワークです。

- 言語: Python
- 今週のスター: 8712
- ライセンス: BSD-3-Clause
- AI分析状態: ok

### できること

- 高速なHTTPリクエストやステルスブラウザ、JavaScriptレンダリング、Cloudflare対策などのフェッチ機能を提供します。（根拠: What you can do with Scrapling）

- CSS、XPath、テキスト・正規表現検索による柔軟なデータ抽出が可能です。（根拠: What you can do with Scrapling）

- AIエージェント向けのMCPサーバーやAgent Skill、LLM向けのMarkdown変換機能を備えています。（根拠: AI Features）


### 利用例

- 静的ページのスクレイピングやJavaScriptのレンダリング、API呼び出しからのデータ抽出。（README明記／根拠: README冒頭）

- プロキシローテーションや自動リトライ、一時停止・再開機能を備えたクローラーの構築。（README明記／根拠: README冒頭）

- WebページをLLMやRAG向けにクリーンなMarkdown形式に変換すること。（README明記／根拠: AI Features）


### 最初に試すこと

Scraplingをインストールして動作を確認する

1. pip install scrapling


成功の目安: エラーなくパッケージがインストールされること

未確認: fetchersやspidersを使用する場合の具体的な追加インストールコマンド


## 10. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

**概要:** OpenMontageは、AIコーディングアシスタントを動画制作スタジオに変えるオープンソースのエージェント型動画制作システムです。自然言語による指示で、調査、台本作成、素材生成、編集、最終合成までのプロセスを自動化します。

- 言語: Python
- 今週のスター: 4369
- ライセンス: AGPL-3.0
- AI分析状態: ok

### できること

- 12の制作パイプライン、100以上のツール、700以上のエージェントスキルおよび制作知識ファイルを搭載しています。（根拠: README冒頭）

- 無料のストック映像やオープンアーカイブから実際の動画クリップを収集し、タイムラインに編集してレンダリングする本格的な動画制作が可能です。（根拠: README冒頭）


### 利用例

- AIコーディングアシスタントを活用して、自然言語の指示から動画の調査、台本、編集、最終合成までを一貫して行う。（README明記／根拠: README冒頭）


### 最初に試すこと

クイックスタートの確認


成功の目安: クイックスタート手順が完了し、動作が確認できること。

未確認: 具体的なインストールコマンドや実行コマンドはREADMEの途中で切れているため未確認です。



## Zenn

- [Cloudflare Zero Wire × GitHub Actions × Claude で公開サーバーの脆弱性チェックを自動化](https://zenn.dev/tomipetit/articles/zero-wire-github-actions) — tomi

- [goda-pm.vim: goda.vim のためのプラグインマネージャー](https://zenn.dev/shougo/articles/goda-pm-vim-beta) — Shougo

- [Weight-Space Programming やってみた(やらせてみた)](https://zenn.dev/nwn/articles/cf9fe78aa33861) — ヨ

- [[破壊的変更] 明治時代の開始日が変更になって単体テストが失敗した件](https://zenn.dev/xin9le/articles/9a1cf8e10494d6) — xin9le

- [Web 標準動向 2026年10月版](https://zenn.dev/cybozu_frontend/articles/web-standards-trends-202610) — kuracchi

- [タスク管理までAIエージェントに任せたら、確認待ちに答えるだけになった](https://zenn.dev/rescuenow/articles/4c03a548cd6589) — しもち

- [Claudeを使いこなす人に、MagicPodは要るのか。知らないアプリでPlaywrightと比べた記録](https://zenn.dev/genda_jp/articles/7b423bcd20b532) — ikenyal

- [米津玄師に学ぶ：一人で全部作れる時代に、なぜ人と作るのか](https://zenn.dev/tokium_dev/articles/yonezu-kenshi-why-create-with-others) — タケノコご飯

- [【.NET/Unity】C# の型制約とボックス化をハックする — IL と手動スタック配置](https://zenn.dev/aakei/articles/csharp-stack-box) — akeit0

- [Security Hub の SBOM インベントリで、Athena を使わずに組織全体のソフトウェアを調べてみた](https://zenn.dev/cscloud_blog/articles/securityhub-sbom-inventory) — 平木 佳介

- [AI駆動文章作成において俺が意識しているテクニック集](https://zenn.dev/ntk221/articles/34ad88a9225364) — ntk

- [.NET にも build.cs 欲しいんじゃーーー](https://zenn.dev/sator_imaging/articles/c10d8da7685308) — サトー™ @sator_imaging

- [[TypeScript] パスエイリアスには Subpath Imports を使いたい](https://zenn.dev/mediba/articles/167e2a3f663889) — mdbr92

- [集約をどこまで機械的に導けるか――形式手法をベースとしたドメインモデリング](https://zenn.dev/nrs/articles/33ba79c8b2542e) — nrs

- [コードを読まずにバイブコーディングしたら、Claude Codeは分かっていてスルーしていた](https://zenn.dev/nexta_/articles/42a828ca2b8a02) — bik

- [OpenCode+Docker+GitHub Actionsで全自動AIペネトレーションテストはじめました](https://zenn.dev/team_zenn/articles/opencode-docker-actions-ai-pentest) — dyoshikawa

- [ADRをregoでlintする](https://zenn.dev/babarot/articles/regomark-adr-checker) — babarot

- [バイブコーディングで機能を継ぎ足していて見えてきたClaudeCodeの実装のクセ](https://zenn.dev/uguisu_blog/articles/45d1f446ece415) — ぴよ

- [ISUCON2026 で優勝しました（当日編）](https://zenn.dev/luvtechno/articles/isucon2026-competition-day) — Yoshinori Kawasaki

- [AIが書く「読みづらいADR」に発狂しかけたので、ADRのガイドラインを作った](https://zenn.dev/tokium_dev/articles/adr-authoring-guideline) — にしこりさぶろ〜 | TOKIUM


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。