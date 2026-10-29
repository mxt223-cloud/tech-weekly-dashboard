# Tech Daily — 2026-10-29

生成日時: 2026-10-29T10:09:58.808582+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

**概要:** cloudflare/security-audit-skillは、コーディングエージェントをセキュリティ監査人に変えるスキルリポジトリです。偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成という6つのフェーズで構造化されたセキュリティ監査を実行します。

- 言語: JavaScript
- 今週のスター: 16002
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




## 2. [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

**概要:** Claude Code上で動作する無料のオープンソースSEOプラグインであり、技術的SEO、コンテンツの品質、構造化データ、AI検索（GEO）、ローカル・ECサイトのSEO監査を並行エージェントで実行し、優先順位付きの行動計画を提供します。

- 言語: Python
- 今週のスター: 3516
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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


## 3. [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

**概要:** Andrej KarpathyのLLMコーディングにおける指摘をもとに作られた、Claude Codeの挙動を改善する単一のCLAUDE.mdファイルおよび関連ガイドラインです。

- 言語: 不明
- 今週のスター: 4293
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




## 4. [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

**概要:** anthropic/knowledge-work-pluginsは、Claudeを専門業務特化型のアシスタントに変えるためのオープンソースプラグイン集です。Claude CoworkおよびClaude Codeで利用でき、スキル、コネクター、スラッシュコマンド、サブエージェントをバンドルしてタスクを効率化します。

- 言語: Python
- 今週のスター: 2612
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


## 5. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

**概要:** TradingAgentsは、実際の証券会社のダイナミクスを模倣したマルチエージェント型の金融取引フレームワークです。ファンダメンタルズ分析、センチメント分析、ニュース分析、テクニカル分析などの専門的な役割を持つLLM駆動のエージェントが協力して市場状況を評価し、取引の意思決定を支援します。

- 言語: Python
- 今週のスター: 5322
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

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


## 6. [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

**概要:** コーディングエージェント向けのデザイン語彙および支援ツールであり、デザインの改善、レビュー、品質監査、AI特有のありふれたデザイン（AI slop）の検出を行います。

- 言語: Rust
- 今週のスター: 7283
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- bolderやquieterなどのコマンドでコードエージェントのデザイン指示を制御する。（根拠: Why）

- critiqueおよびauditコマンドでユーザビリティやアクセシビリティのレビューとスコア算出を行う。（根拠: Why）

- 決定論的ルールを用いたAI slopの検出を、エージェントフック、CLI、ブラウザ拡張機能で実行する。（根拠: Three ways to run the detector）


### 利用例

- AIが生成しがちなありふれたデザイン上の欠陥（AI slop）を事前に検出して防ぐ。（README明記／根拠: Why）

- コマンドを使用してUIのトーン調整やフォント、レイアウト、アクセシビリティの修正をエージェントに指示する。（README明記／根拠: 24 commands）

- CLIツールを使用してソースコードディレクトリやレンダリング済みページをスキャンし、問題点をレポートする。（README明記／根拠: Three ways to run the detector）


### 最初に試すこと

プロジェクトにImpeccableをインストールして初期化する。

1. npx impeccable install

2. コーディングツールをリロードする

3. エージェント内で /impeccable init を実行する


成功の目安: プロジェクトにImpeccableがインストールされ、初期化コマンドが実行できること。

未確認: 詳細な内部実装アルゴリズムや外部APIの通信仕様／商用利用における具体的なライセンス制限（Apache 2.0以外の条件）


## 7. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

**概要:** Graphify-Labs/graphifyは、コードベースやドキュメント、SQLスキーマ、設定、PDFなどを検索可能なナレッジグラフに変換するツールです。Claude Code、Cursor、Codex、Gemini CLIなどのAIコーディングアシスタントで/graphifyスキルとして利用でき、ローカルでの決定論的なAST解析とベクトルストアを使わないグラフ構造を提供します。

- 言語: Python
- 今週のスター: 6662
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


## 8. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

**概要:** Taste Skillは、コーディングエージェントにデザインの感性、実際の画像、実際のブラウザでの検証機能を与え、一般的なAIによるページではなく、高品質なウェブサイトやアプリ画面を設計できるようにするエージェントスキルです。

- 言語: JavaScript
- 今週のスター: 3940
- ライセンス: MIT
- AI分析状態: ok

### できること

- 独自のアートディレクションの提示、オープンアーカイブからの実写画像の利用、実際のブラウザでの自己検証を行う（根拠: README冒頭）

- ダッシュボードやアプリ画面向けに、実製品の画面研究に基づくスタイル適応、シェル、データ、チャート、テーブルの構築を行う（根拠: How v2 works）

- React、Vue、Svelte、プレーンなHTMLなど、フレームワークを問わずデザインのルールを適用できる（根拠: Common Questions）


### 利用例

- コーディングエージェントを使用して独自のこだわりを持ったランディングページを構築する（README明記／根拠: README冒頭）

- ダッシュボード、管理画面、設定画面などのアプリ画面を構築する（README明記／根拠: Common Questions）

- 既存のページを変更する前に実際のブラウザで監査する（README明記／根拠: Moved skills）


### 最初に試すこと

skills CLIを使用してdesign-taste-frontendスキルをインストールする

1. npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"


成功の目安: スキルが正常にインストールされること

未確認: 具体的なAIモデルの内部動作や詳細なトークン消費量の変動要因


## 9. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**概要:** RufloはClaude CodeやCodexなどのモデルを対象としたエージェント用メタハーネスです。100以上の専門エージェント、協調スウォーム、自己学習型メモリ、ゼロトラストなエージェント間フェデレーション、ベクトルRAG統合などの機能を提供し、マルチエージェントシステムの構築や自律的なワークフローの制御を可能にします。

- 言語: TypeScript
- 今週のスター: 1930
- ライセンス: MIT
- AI分析状態: ok

### できること

- 100以上の特殊化されたエージェントによるコーディング、テスト、セキュリティ、ドキュメント生成などのサポート（根拠: What You Get）

- エージェント間でのゼロトラストなセキュア通信とワークスペース共有を実現するフェデレーション機能（根拠: Agent Federation — Slack for Agents）

- HNSWインデックス付きAgentDBを用いた高速なベクトルメモリと自己学習メカニズム（根拠: What You Get）


### 利用例

- 複数のAIエージェントをチームとして連携させ、自律的なワークフローやコーディングタスクを調整する（README明記／根拠: Get started with Ruflo）

- 異なるマシンや組織間でエージェント同士を接続し、プライバシーを保護しながらデータを共有して協調作業を行う（README明記／根拠: Agent Federation — Slack for Agents）

- プロジェクトのコード品質検査やテストケースの自動生成、セキュリティ脆弱性のスキャンを実行する（README明記／根拠: Quick Start）


### 最初に試すこと

プロジェクトの初期化またはCLIセットアップウィザードの実行

1. npx ruflo@latest init wizard


成功の目安: セットアップウィザードが起動し、プロジェクトの初期化が行われること

未確認: 具体的な商用利用における大規模運用でのパフォーマンス詳細／すべてのプラグインの個別詳細な動作仕様


## 10. [anomalyco/opencode](https://github.com/anomalyco/opencode)

**概要:** opencodeは、オープンソースのAIコーディングエージェントです。CLIやデスクトップアプリとして利用でき、開発向けのbuildエージェントや読み取り専用のplanエージェントなどを切り替えてコードの作成や探索が行えます。

- 言語: TypeScript
- 今週のスター: 3498
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



## Zenn

- [いいから休め - Black October が終わる今、セキュリティエンジニアがやるべきこと](https://zenn.dev/nayuta/articles/aec9ab2e11a7b7) — nayuta

- [人間が見るのは設計書だけ ― PdM不在・バグ修正中心のチームで、AI-DLCを開発フローごと作り直した話](https://zenn.dev/canly/articles/85dc645c252832) — kszk103

- [業務マスタの新規登録をSeleniumで連続化したら、「新規」の判定を2回直すことになった【Python】](https://zenn.dev/cutlet_of_pork/articles/selenium-rpa-new-entry-key-definition) — とんのかつ

- [RustからDynamoDBを型安全に扱うためのraiden-dynamoを作った](https://zenn.dev/fraim/articles/50908c30561af5) — bokuweb

- [公表資料から読む2026年秋の情報漏えい18件：侵入経路はどこだったのか](https://zenn.dev/shirochan/articles/f579ce70b08dc3) — しろちゃん

- [Auto mode時代のClaude Codeを守る。検証済み10キットで始めるセキュリティ対策【全員・チーム・組織別】](https://zenn.dev/sonicmoov/articles/67aaeb49be69ec) — azarashi

- [図で理解する Dagster on ECS の構成と、失敗に気づく仕組み](https://zenn.dev/safie_inc/articles/dagster_on_ecs) — ワタナベ

- [Flutter やめました。電話アプリを Native にした理由](https://zenn.dev/ivry/articles/d155267331a3ca) — tsutou

- [S3 Tables + Snowflake を使用した Lakehouse 統合](https://zenn.dev/eversteel_tech/articles/e4771af8952421) — keeeeen

- [AIエージェントに設計書レビューを任せたらレビュワーは楽になった。でも現場は？？](https://zenn.dev/nttdata_tech/articles/6a06f484ebfab7) — kazuma sugiyama

- [【Rails】焼きなまし法で会議室予約アプリに空き時間最適化機能を実装してみた](https://zenn.dev/port_inc/articles/eaf460ff291c97) — koyu5000

- [Claude Codeで半年分のレビュー指摘を分類してみた](https://zenn.dev/port_inc/articles/a4bc3b39f44459) — なお

- [コードを読まずにマージするために必要なこと](https://zenn.dev/nrs/articles/c777388530aa84) — nrs

- [Go で動く新世代の補完プラグイン goda-cmp.vim](https://zenn.dev/shougo/articles/goda-cmp-vim-beta) — Shougo

- [学生2人で日本語音声LLMを作り、FT-LLM 2026 自由形タスクで1位を獲得した話](https://zenn.dev/ayutaso/articles/ftllm2026-ja-speech-llm) — Atotti

- [AI の謎な説明文を直すスキル](https://zenn.dev/microsoft/articles/explain-before-shorten) — Kazuki Ota

- [最近の E2E 戦略（2026 年 10 月現在）](https://zenn.dev/polyco/articles/26624b38c951b5) — Tatsunori Nakano

- [600人規模のイベント運営を支えたインカムを、学生1人で作った話](https://zenn.dev/kodak_20/articles/3b0ba74333b56c) — コダック

- [2026年の国内情報漏えい71件を侵入経路で分類してみた](https://zenn.dev/blackleg/articles/e9ed8b038bcf48) — blackleg

- [eMudhraの中間CA証明書の秘密鍵を求めてみる](https://zenn.dev/herumi/articles/search_bad_emudhra_key) — herumi


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。