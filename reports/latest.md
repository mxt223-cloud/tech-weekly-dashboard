# Tech Daily — 2026-10-27

生成日時: 2026-10-27T09:42:09.152570+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

**概要:** cloudflare/security-audit-skillは、コーディングエージェントをセキュリティ監査人に変えるスキルリポジトリです。偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成という6つのフェーズで構造化されたセキュリティ監査を実行します。

- 言語: JavaScript
- 今週のスター: 16593
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




## 2. [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

**概要:** anthropic/knowledge-work-pluginsは、Claudeを専門業務特化型のアシスタントに変えるためのオープンソースプラグイン集です。Claude CoworkおよびClaude Codeで利用でき、スキル、コネクター、スラッシュコマンド、サブエージェントをバンドルしてタスクを効率化します。

- 言語: Python
- 今週のスター: 2822
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- ロール、チーム、企業に合わせた専門的なプラグイン（生産性向上、営業、カスタマーサポート、製品管理、マーケティング、法務、財務、データ分析、エンタープライズ検索、バイオ研究、プラグイン管理など11種類）を提供する。（根拠: Plugin Marketplace）

- MCPサーバーを介してSlack、Notion、Asana、Snowflakeなどの外部ツールやデータソースと接続する。（根拠: How Plugins Work）

- マークダウンとJSONによるファイルベースの構造を採用し、コードやインフラストラクチャなしでカスタムプラグインの作成や既存プラグインのカスタマイズができる。（根拠: Making Them Yours）


### 利用例

- 営業活動において、見込み客の調査、コールの準備、パイプラインの確認、アウトリーチの下書き、競合バトルカードの作成を行う。（README明記／根拠: Plugin Marketplace）

- 財務業務において、仕訳の準備、勘定科目の消込、財務諸表の作成、差異分析、決算管理、監査支援を行う。（README明記／根拠: Plugin Marketplace）

- データ分析において、クエリの記述、可視化、データセットの解釈、統計分析、ダッシュボードの構築を行う。（README明記／根拠: Plugin Marketplace）


### 最初に試すこと

Claude Codeを使用してマーケットプレイスを追加し、特定のプラグインをインストールする

1. claude plugin marketplace add anthropics/knowledge-work-plugins

2. claude plugin install sales@knowledge-work-plugins


成功の目安: 指定したプラグインがClaude Code環境に正常にインストールされること

未確認: プラグインごとの詳細な内部実装コードや個別のコネクター設定の全詳細


## 3. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**概要:** ruvnet/rufloは、Claude CodeやCodexなどのモデルを拡張するエージェントメタハーネスです。100種類以上の専門エージェント、協調スウォーム、自己学習メモリ、ゼロトラスト型のエージェント間フェデレーション機能などを提供し、複数エージェントによる自律的なワークフローの構築や会話型AIシステムの開発を支援します。

- 言語: TypeScript
- 今週のスター: 2683
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 100種類以上の専門的なエージェントによるコーディング、テスト、セキュリティ、ドキュメント作成のサポート（根拠: What You Get）

- HNSWインデックス付きAgentDBやベクターRAG統合によるエージェントメモリと学習機能（根拠: What You Get）

- mTLSとed25519を用いたゼロトラスト型のエージェント間フェデレーションとPIIフィルタリング機能（根拠: Agent Federation — Slack for Agents）


### 利用例

- 複数エージェントを連携させた自律的な開発ワークフローの構築と協調処理（README明記／根拠: Get started with Ruflo）

- ベクトルメモリやRAGを活用した、コードベース全体の効率的な検索と知識管理（README明記／根拠: What You Get）

- 異なるマシンや組織間で機密情報を保護しながらエージェント同士でタスクを共有する協業（README明記／根拠: Agent Federation — Slack for Agents）


### 最初に試すこと

プロジェクトの初期設定ウィザードを実行する

1. プロジェクトのターミナルでセットアップウィザードを実行する


成功の目安: npx ruflo@latest init wizard コマンドが正常に実行され、初期設定が完了すること




## 4. [anomalyco/opencode](https://github.com/anomalyco/opencode)

**概要:** opencodeは、オープンソースのAIコーディングエージェントです。CLIやデスクトップアプリとして利用でき、開発向けのbuildエージェントや読み取り専用のplanエージェントなどを切り替えてコードの作成や探索が行えます。

- 言語: TypeScript
- 今週のスター: 5070
- ライセンス: MIT
- AI分析状態: ok

### できること

- buildエージェントによる開発作業向けの高権限な処理（根拠: Agents）

- planエージェントによるファイル編集の拒否や確認を伴う安全なコード探索（根拠: Agents）

- Tabキーによるエージェント間の切り替え機能（根拠: Agents）


### 利用例

- 開発作業におけるコード作成やエージェントを活用した実装（README明記／根拠: Agents）

- 不慣れなコードベースの探索や変更計画の立案（README明記／根拠: Agents）

- デスクトップアプリケーションを利用したAIコーディング作業（README明記／根拠: Desktop App (BETA)）


### 最初に試すこと

CLI環境でopencodeをインストールする

1. curl -fsSL https://opencode.ai/v2/install | bash


成功の目安: opencodeがインストールされ、利用可能になること

未確認: 詳細な設定オプションや対応しているAIモデルの全リスト


## 5. [stablyai/orca](https://github.com/stablyai/orca)

**概要:** Orcaは、複数のAIコーディングエージェント（Claude Code、Codex、Grokなど）を並行して実行・管理するためのAIオーケストレータおよびデスクトップ/モバイル環境です。

- 言語: TypeScript
- 今週のスター: 9241
- ライセンス: MIT
- AI分析状態: ok

### できること

- モバイルアプリを使用して、外出先からエージェントの監視、通知の受け取り、フォローアップの送信ができる。（根拠: Features）

- 1つのプロンプトを複数のエージェントへ同時に送信し、それぞれ独立したGitワークツリーで実行・比較できる。（根拠: Features）

- ターミナル分割やデザインモード、SSHワークツリー、GitHub・Linearのネイティブ統合などの機能を提供する。（根拠: Features）


### 利用例

- 複数の異なるAIエージェントを並行して走らせ、それぞれの結果を比較して最適なものをマージする。（README明記／根拠: Features）

- デスクトップで実行中のエージェントの状況をスマートフォンのモバイルコンパニオンアプリから遠隔監視する。（README明記／根拠: Features）

- SSH接続したリモートの強力なマシン上でAIエージェントを実行し、ファイル編集やターミナル操作を行う。（README明記／根拠: Features）


### 最初に試すこと

デスクトップアプリまたはパッケージマネージャーを使用してOrcaをインストールする

1. 公式サイト（onorca.dev/download）からインストーラーをダウンロードするか、macOSの場合は「brew install --cask stablyai/orca/orca」、Arch Linuxの場合は「yay -S stably-orca-bin」を実行する。


成功の目安: Orcaがシステムにインストールされ、起動できるようになること。

未確認: CONTRIBUTING.mdに記載されている具体的な開発セットアップ手順の詳細／cloud/ディレクトリにあるリレーサーバーの具体的な設定手順


## 6. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

**概要:** Graphify-Labs/graphifyは、コードベースやドキュメント、SQLスキーマ、設定、PDFなどを検索可能なナレッジグラフに変換するツールです。Claude Code、Cursor、Codex、Gemini CLIなどのAIコーディングアシスタントで/graphifyスキルとして利用でき、ローカルでの決定論的なAST解析とベクトルストアを使わないグラフ構造を提供します。

- 言語: Python
- 今週のスター: 7183
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- コードベースをtree-sitter ASTによりローカルで決定論的に解析し、完全ローカルでコードマップを作成する（根拠: README冒頭）

- ドキュメント、PDF、画像、ビデオをアシスタントのモデルや設定済みAPIキーを使用してセマンティックパスとして処理する（根拠: README冒頭）

- 各接続（エッジ）をソースに明示された「EXTRACTED」とgraphifyによって解決された「INFERRED」にタグ付けして説明する（根拠: README冒頭）


### 利用例

- AIコーディングアシスタント内で/graphifyと入力し、プロジェクト全体をファイル内検索（grep）の代わりにクエリ可能なナレッジグラフとしてマッピングする（README明記／根拠: README冒頭）


### 最初に試すこと

/graphifyスキルをAIコーディングアシスタントで実行してプロジェクトのマッピングを開始する

1. Claude Code、Cursor、Codex、またはGemini CLIなどの対応するAIコーディングアシスタントを開く

2. チャット欄やプロンプトに「/graphify」と入力して実行する


成功の目安: プロジェクトがナレッジグラフとしてマッピングされ、ファイル検索の代わりにクエリできるようになること

未確認: 詳細なインストールコマンドやQuick Startの具体的な実行手順コード／ローカル実行以外のGraphify Cloudの具体的な連携機能の全容


## 7. [android/skills](https://github.com/android/skills)

**概要:** Android開発向けのAI最適化されたモジュール式指示とリソースを提供するリポジトリです。LLMが苦手とするユースケースやワークフローを対象としています。

- 言語: Kotlin
- 今週のスター: 823
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- Android CLIを使用して特定のスキルをカレントディレクトリにインストールする（根拠: Install Android skills）

- Android CLIを使用してすべてのAndroidスキルを検出されたすべてのエージェント向けにインストールする（根拠: Install Android skills）

- プラグインとしてClaude CodeやCodexにインストールする（根拠: Install as an agent plugin）


### 利用例

- LLMのエージェントに特定のスキルをインストールして、Android開発のベストプラクティスやパターンを実行させる（README明記／根拠: Android skills）

- エージェントが自動的に関連するスキルを有効化し、アプリUIをエッジツーエッジにするなどのタスクを実行させる（README明記／根拠: Activate skills）


### 最初に試すこと

Android CLIを使用して特定のスキルをインストールする

1. android skills add r8-analyzer --project=.


成功の目安: 指定したスキルがプロジェクトにインストールされること

未確認: リポジトリ内に含まれる個別のスキルの全一覧や詳細な種類


## 8. [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

**概要:** ai-memoryは、複数のAIコーディングエージェント（Claude Code、Codex、Cursorなど）の間で長期的なコンテキストや作業の引き継ぎを共有するためのRust製ソリューションです。

- 言語: Rust
- 今週のスター: 2838
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 複数のAIエージェント間で共有メモリと引き継ぎプロトコルを利用できる。（根拠: Why ai-memory）

- 保存されるデータはプレーンなMarkdownのGitバックアップwikiであり、検索や手動編集が可能。（根拠: Why ai-memory）

- ライフサイクルHookによって作業内容を自動で静かに記録し、デフォルトではLLMの呼び出しを必要としない。（根拠: Why ai-memory）


### 利用例

- Claude Codeで作業を途中で中断し、同じディレクトリでOpenAI Codexを起動して説明なしに作業を引き継ぐ。（README明記／根拠: Why ai-memory）

- パッケージマネージャやテストレイアウトなど、自身の開発スタイルに関するプロファイルを新しいリポジトリでのセッション開始時に反映させる。（README明記／根拠: Why ai-memory）

- チームメンバー全員で1つのサーバーを参照し、ある人のセッションから得た知識を他のメンバーのAIエージェントで共有する。（README明記／根拠: Why ai-memory）


### 最初に試すこと

クイックスタートの実施


成功の目安: クイックスタート手順の完了

未確認: 具体的なインストールコマンドや実行コマンドの詳細な手順はREADMEのQuick startセクションが空のため不明です。


## 9. [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

**概要:** Andrej KarpathyのLLMコーディングにおける指摘をもとに作られた、Claude Codeの挙動を改善する単一のCLAUDE.mdファイルおよび関連ガイドラインです。

- 言語: 不明
- 今週のスター: 3286
- ライセンス: 不明
- AI分析状態: ok

### できること

- Claude Codeのプラグインとしてインストールし、スキルをすべてのプロジェクトで利用できるようにする。（根拠: Install）

- プロジェクト固有のCLAUDE.mdにガイドラインを追加、または新規作成する。（根拠: Install）

- Cursorプロジェクトルールとして設定し、Cursorでも同様のガイドラインを適用する。（根拠: Using with Cursor）


### 利用例

- Claude Codeを使用してコーディングを行う際に、勝手な仮定や複雑化を防ぎ、シンプルで正確なコード変更を行わせる。（README明記／根拠: The Solution）

- Cursorなどのエディタでプロジェクトを開いた際に、Karpathyのガイドラインをルールとして適用する。（README明記／根拠: Using with Cursor）


### 最初に試すこと

Claude Codeプラグインとしてガイドラインをインストールする

1. /plugin marketplace add forrestchang/andrej-karpathy-skills

2. /plugin install andrej-karpathy-skills@karpathy-skills


成功の目安: プラグインが正しくインストールされ、Claude Code内でスキルが利用可能になること




## 10. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

**概要:** TradingAgentsは、実際の金融取引会社の動きを模した、マルチエージェント型のLLM金融取引フレームワークです。ファンダメンタルズ分析、センチメント分析、テクニカル分析などの専門エージェントが協調して市場状況を評価し、取引判断を行います。

- 言語: Python
- 今週のスター: 3437
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- ファンダメンタルズ分析、センチメント分析、ニュース分析、テクニカル分析を担当する専門エージェントによる並行分析（根拠: Analyst Team）

- 複数のLLMプロバイダー（OpenAI、Google、Anthropicなど）およびDocker、ローカル環境での実行をサポート（根拠: Installation and CLI）

- 過去の決定に対する報酬の追跡や過去の教訓の引き継ぎを行うメモリログ機能（根拠: Memory log）


### 利用例

- 世界各国の市場や暗号資産の銘柄に対し、エージェントを活用したシミュレーションや取引判断の評価を行う（README明記／根拠: Markets and tickers）

- バックテスト機能を用いて特定の期間や複数の銘柄における取引戦略の評価を行う（README明記／根拠: Evaluating decisions over time）

- 自身の保有ポートフォリオ情報を入力し、実際のアカウント状況に基づいたリスク評価や取引提案を受ける（README明記／根拠: Current holdings）


### 最初に試すこと

リポジトリをクローンし、必要な環境構築とパッケージのインストールを行ってCLIを起動する

1. git clone https://github.com/TauricResearch/TradingAgents.git

2. cd TradingAgents

3. pip install .


成功の目安: パッケージのインストールが完了し、CLIコマンドが利用できるようになること

未確認: 実際の商用環境での運用における正確な収益性やパフォーマンス



## Zenn

- [昨今のセキュリティ情勢を踏まえて、Azure のセキュリティ系新資格 SC-500 を受けてみた【合格体験記】](https://zenn.dev/microsoft/articles/112ff28ccc30e3) — Naoki Matsumoto

- [学生2人で日本語音声LLMを作り、FT-LLM 2026 自由形タスクで1位を獲得した話](https://zenn.dev/ayutaso/articles/ftllm2026-ja-speech-llm) — Atotti

- [OpenWrt 25.12のadblock 4.5に豆腐フィルタを適用する（ruleの書式が変わった）](https://zenn.dev/yotan/articles/openwrt-25-adblock-tofu-filter) — よたん

- [Vue Fes Japan 2026 「 Vite+への貢献と、Team Memberになって見えてきた風景」スピーカーノート](https://zenn.dev/comm_vue_nuxt/articles/33f8491afbc66d) — Naoki Haba

- [AI時代のアーキテクチャ：実装を任せるために、詳細設計を自分のものにする](https://zenn.dev/simplex/articles/f2b41d3367e9c7) — Simplex テックブログ運営

- [AI の謎な説明文を直すスキル](https://zenn.dev/microsoft/articles/explain-before-shorten) — Kazuki Ota

- [Node.js の Brotli 脆弱性 CVE-2026-111497 を読む](https://zenn.dev/chot/articles/79e6c94e27782d) — k1350

- [最近の E2E 戦略（2026 年 10 月現在）](https://zenn.dev/polyco/articles/26624b38c951b5) — Tatsunori Nakano

- [AIネイティブなインターン生を受け入れて考えた、これからの開発エンジニア](https://zenn.dev/tokium_dev/articles/internship-mentoring-2026) — おかもり

- [S3のParquet、そのままSnowflakeで分析しても遅くない？Parquet Directを検証](https://zenn.dev/snowflakejp/articles/parquet-direct-pruning-benchmark) — rniki

- [スタックトレースを読むとヒープが約1,470 MB増えていた話](https://zenn.dev/dress_code/articles/f2a51226c9ec6f) — かわうそ

- [育休復帰のキャッチアップをAI に手伝ってもらった話](https://zenn.dev/nextbeat/articles/862dd45c304c13) — iidadaiti

- [私が5種類のコーディングエージェントを使い分ける理由](https://zenn.dev/rimon/articles/45c1fd2f015af8) — ミモ  フォワードCTO・CPO

- [600人規模のイベント運営を支えたインカムを、学生1人で作った話](https://zenn.dev/kodak_20/articles/3b0ba74333b56c) — コダック

- [2026年の国内情報漏えい71件を侵入経路で分類してみた](https://zenn.dev/blackleg/articles/e9ed8b038bcf48) — blackleg

- [prpr: Rust 向けのシンプルで高速な Parser generator](https://zenn.dev/tanakh/articles/prpr-packrat-parser) — Hideyuki Tanaka

- [eMudhra 中間 CA 漏洩、OS もブラウザも最新なのにコンテナ 9 個と Python 環境 16 個が偽の証明書を信じていた](https://zenn.dev/nanora/articles/20261024-emudhra-ca-own-bundles) — nanora

- [eMudhraの中間CA証明書の秘密鍵を求めてみる](https://zenn.dev/herumi/articles/search_bad_emudhra_key) — herumi

- [脆弱性管理の仕組みを整えた](https://zenn.dev/dress_code/articles/be5550254695cd) — anizozina

- [仕組みを理解する動画を、Claude Codeに作らせると便利すぎる](https://zenn.dev/explaza/articles/c749042ecbe232) — musoukun


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。