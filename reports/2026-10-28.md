# Tech Daily — 2026-10-28

生成日時: 2026-10-28T09:40:32.986387+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

**概要:** cloudflare/security-audit-skillは、コーディングエージェントをセキュリティ監査人に変えるスキルリポジトリです。偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成という6つのフェーズで構造化されたセキュリティ監査を実行します。

- 言語: JavaScript
- 今週のスター: 16388
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
- 今週のスター: 2789
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


## 3. [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

**概要:** Claude Code上で動作する無料のオープンソースSEOプラグインであり、技術的SEO、コンテンツの品質、構造化データ、AI検索（GEO）、ローカル・ECサイトのSEO監査を並行エージェントで実行し、優先順位付きの行動計画を提供します。

- 言語: Python
- 今週のスター: 3081
- ライセンス: MIT
- AI分析状態: ok

### できること

- 技術的SEO監査として、クロール可能性、インデックス登録、サイトマップ、robots.txt、リダイレクト、ページ速度、Core Web Vitalsをチェックします。（根拠: README冒頭）

- 構造化データの検出、検証、およびリッチリザルト向けのSchema.orgマークアップの作成を行います。（根拠: README冒頭）

- AI検索（GEO）において、Google AI Overviews、AI Mode、ChatGPT、Perplexity、GeminiなどのAI検索エンジンにページが引用される可能性を評価します。（根拠: README冒頭）


### 利用例

- SEOエージェンシーがクライアント向けに四半期ごとではなく毎週の監査を行い、問題の変化をモニタリングする。（README明記／根拠: Meet the team）

- SaaS、メディア、EC企業の社内SEOチームが、AI検索への対応を含めて記事やレビュー公開前のダブルチェックを行う。（README明記／根拠: Meet the team）

- フリーランスのSEOコンサルタントが初回の打ち合わせ時に監査を実行し、提案書を書く前に実際のスコアと主な修正点を示す。（README明記／根拠: Meet the team）


### 最初に試すこと

Claude Code内でClaude SEOをセットアップし、ウェブサイトのフル監査を実行する

1. /plugin marketplace add AgriciDaniel/claude-seo

2. /plugin install claude-seo@agricidaniel-claude-seo

3. /seo setup

4. /seo audit https://example.com


成功の目安: Claude SEOのセットアップが完了し、指定したURLのフルサイト監査と優先順位付きプランが出力されること

未確認: オプショナルな拡張機能（Live data、image-gen、seranking、profound、bing、unlighthouse）の具体的な導入手順やAPIキー設定の詳細／AI Marketing Hub Pro会員向けプライベートバージョンのすべての詳細な機能差異


## 4. [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

**概要:** Andrej KarpathyのLLMコーディングにおける指摘をもとに作られた、Claude Codeの挙動を改善する単一のCLAUDE.mdファイルおよび関連ガイドラインです。

- 言語: 不明
- 今週のスター: 4039
- ライセンス: 不明
- AI分析状態: ok（キャッシュ）

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




## 5. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

**概要:** TradingAgentsは、実際の証券会社のダイナミクスを模倣したマルチエージェント型の金融取引フレームワークです。ファンダメンタルズ分析、センチメント分析、ニュース分析、テクニカル分析などの専門的な役割を持つLLM駆動のエージェントが協力して市場状況を評価し、取引の意思決定を支援します。

- 言語: Python
- 今週のスター: 4882
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- ファンダメンタルズアナリスト、センチメントアナリスト、ニュースアナリスト、テクニカルアナリストなどの専門的な役割を持つLLMエージェントが協調して市場を評価する（根拠: TradingAgents Framework）

- OpenAI、Google、Anthropic、DeepSeek、Ollamaなどの複数のLLMプロバイダーや、自身のChatGPT Plus/Proプランを利用できる（根拠: Installation and CLI）

- LangGraphによるチェックポイントの再開機能や、決定事項の記憶ログを記録・維持する機能を持つ（根拠: Persistence and Recovery）


### 利用例

- 銘柄コードと日付を指定して、AIエージェントによる取引判断や分析レポートを生成する（README明記／根拠: CLI Usage）

- 過去の日付や複数銘柄のグリッドに対してバックテストを実行し、意思決定のパフォーマンスを評価する（README明記／根拠: Evaluating decisions over time）

- 保有する資産ポートフォリオを渡して、自身の実際の手持ち状況に合わせた取引の提案やリスク評価を行う（README明記／根拠: Current holdings）


### 最初に試すこと

リポジトリをクローンしてパッケージをインストールし、CLIまたはPythonコードからTradingAgentsを実行する

1. git clone https://github.com/TauricResearch/TradingAgents.git

2. cd TradingAgents

3. pip install .


成功の目安: パッケージのインストールが完了し、CLIコマンドまたはPythonのTradingAgentsGraphによる実行結果が得られること

未確認: デフォルトで推奨されているモデル（GPT-6やClaude Sonnet 5など、標準的なAPI以外における実際の挙動や利用制限の詳細は実際の環境に依存する）


## 6. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

**概要:** Graphify-Labs/graphifyは、コードベースやドキュメント、SQLスキーマ、設定、PDFなどを検索可能なナレッジグラフに変換するツールです。Claude Code、Cursor、Codex、Gemini CLIなどのAIコーディングアシスタントで/graphifyスキルとして利用でき、ローカルでの決定論的なAST解析とベクトルストアを使わないグラフ構造を提供します。

- 言語: Python
- 今週のスター: 7268
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


## 7. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**概要:** ruvnet/rufloは、Claude CodeやCodexなどのモデルを拡張して、複数のAIエージェントによるチームや自律的なワークフローを構築・管理するためのエージェントメタハーネス（実行層）です。

- 言語: TypeScript
- 今週のスター: 2296
- ライセンス: MIT
- AI分析状態: ok

### できること

- 100以上の専門エージェントによるコーディング、テスト、セキュリティ、ドキュメント作成の支援（根拠: What You Get）

- HNSWインデックス付きのAgentDBを利用したベクトルメモリおよびセッション横断の記憶維持（根拠: What You Get）

- mTLSとed25519によるゼロトラストセキュリティを用いた、異なるマシン間での安全なエージェントフェデレーション（協調）（根拠: Agent Federation — Slack for Agents）


### 利用例

- 複数のエージェントを協調させて自律的な開発ワークフローを実行する（README明記／根拠: Get started with Ruflo）

- ベクトルメモリやRAG統合を活用してエージェントの過去の成功パターンや知識を学習・共有する（README明記／根拠: What You Get）

- セキュリティ監査やコードの脆弱性スキャン、CVEの対策を自動化する（README明記／根拠: What You Get）


### 最初に試すこと

Claude Code環境でRufloの基本機能とプラグインを導入する

1. /plugin marketplace add ruvnet/ruflo

2. /plugin install ruflo-core@ruflo

3. /plugin install ruflo-console@ruflo

4. /plugin install ruflo-mods@ruflo

5. /reload-plugins

6. /ruflo


成功の目安: Claude Code内でプラグインが有効化され、/rufloコマンドを実行してコンソールやツールを利用できること

未確認: 本番環境における大規模運用時の具体的なパフォーマンス数値／外部連携する各LLMプロバイダーごとの詳細な挙動と制限


## 8. [anomalyco/opencode](https://github.com/anomalyco/opencode)

**概要:** opencodeは、オープンソースのAIコーディングエージェントです。CLIやデスクトップアプリとして利用でき、開発向けのbuildエージェントや読み取り専用のplanエージェントなどを切り替えてコードの作成や探索が行えます。

- 言語: TypeScript
- 今週のスター: 4334
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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


## 9. [stablyai/orca](https://github.com/stablyai/orca)

**概要:** Orcaは、複数のAIコーディングエージェント（Claude Code、Codex、Grokなど）を並行して実行・管理するためのAIオーケストレータおよびデスクトップ/モバイル環境です。

- 言語: TypeScript
- 今週のスター: 8802
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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


## 10. [android/skills](https://github.com/android/skills)

**概要:** Android開発向けのAI最適化されたモジュール式指示とリソースを提供するリポジトリです。LLMが苦手とするユースケースやワークフローを対象としています。

- 言語: Kotlin
- 今週のスター: 873
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



## Zenn

- [コードを読まずにマージするために必要なこと](https://zenn.dev/nrs/articles/c777388530aa84) — nrs

- [Go で動く新世代の補完プラグイン goda-cmp.vim](https://zenn.dev/shougo/articles/goda-cmp-vim-beta) — Shougo

- [AAIF に加わった Open Responses を Amazon Bedrock で試す](https://zenn.dev/exwzd/articles/20261023-open-responses) — 伊賀 裕展

- [Kiro から Backlog・Chat・ドライブを横断検索できるようにしてみた（公式MCP）](https://zenn.dev/senuma/articles/588fb50a8f56ce) — 瀬沼

- [Vue Fes Japan 2026 に参加してきました！](https://zenn.dev/koutyuke/articles/vuefes-japan-2026) — こうちゅけ

- [Jevに問い合わせメッセージを仕分けてもらう](https://zenn.dev/chot/articles/980c44e5a19736) — Akira Tempaku

- [GASで素のJSを埋め込むと < がエスケープされて動かない：getContent() の落とし穴と直し方](https://zenn.dev/kimura0314/articles/gas-htmloutput-getcontent-escapes-lt) — kimura

- [Chromium(V8)のArray.prototype.lastIndexOfを最大約26000倍高速化した](https://zenn.dev/dinii/articles/2f66b147007cf8) — Riya Amemiya

- [Dockerのビルドを遅くしたコミットをGrafana Tempoのトレースで見つける](https://zenn.dev/ymotongpoo/articles/20261027-buildkit-traces-tempo) — Yoshi Yamaguchi

- [新卒エンジニアが初めてのインターン受け入れでマネジメントに奮闘した話](https://zenn.dev/tokium_dev/articles/summer-intern-first-team-management) — ちっち

- [HPA は kubectl scale の台数を守らない](https://zenn.dev/shinagawa_web/articles/hpa-reverts-manual-scale) — shinagawa

- [Dockerfileのビルドとコンテナの中の確認](https://zenn.dev/mutsu_zenn/articles/62895d07e7ef23) — mutsu

- [学生2人で日本語音声LLMを作り、FT-LLM 2026 自由形タスクで1位を獲得した話](https://zenn.dev/ayutaso/articles/ftllm2026-ja-speech-llm) — Atotti

- [AI の謎な説明文を直すスキル](https://zenn.dev/microsoft/articles/explain-before-shorten) — Kazuki Ota

- [Node.js の Brotli 脆弱性 CVE-2026-111497 を読む](https://zenn.dev/chot/articles/79e6c94e27782d) — k1350

- [最近の E2E 戦略（2026 年 10 月現在）](https://zenn.dev/polyco/articles/26624b38c951b5) — Tatsunori Nakano

- [私が5種類のコーディングエージェントを使い分ける理由](https://zenn.dev/rimon/articles/45c1fd2f015af8) — ミモ  フォワードCTO・CPO

- [600人規模のイベント運営を支えたインカムを、学生1人で作った話](https://zenn.dev/kodak_20/articles/3b0ba74333b56c) — コダック

- [2026年の国内情報漏えい71件を侵入経路で分類してみた](https://zenn.dev/blackleg/articles/e9ed8b038bcf48) — blackleg

- [eMudhraの中間CA証明書の秘密鍵を求めてみる](https://zenn.dev/herumi/articles/search_bad_emudhra_key) — herumi


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。