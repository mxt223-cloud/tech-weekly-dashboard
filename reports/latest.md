# Tech Daily — 2026-10-30

生成日時: 2026-10-30T10:16:43.474253+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

**概要:** cloudflare/security-audit-skillは、コーディングエージェントをセキュリティ監査人に変えるスキルリポジトリです。偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成という6つのフェーズで構造化されたセキュリティ監査を実行します。

- 言語: JavaScript
- 今週のスター: 14320
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




## 2. [php/php-src](https://github.com/php/php-src)

**概要:** php/php-srcは、Web開発に特化した汎用スクリプト言語PHPのインタプリタのソースコードリポジトリです。

- 言語: C
- 今週のスター: 960
- ライセンス: BSD-3-Clause
- AI分析状態: ok

### できること

- PHPスクリプト言語のインタプリタとして機能する（根拠: README冒頭）

- ソースコードからのビルドやテストの実行が可能（根拠: Building PHP source code）

- 拡張機能による追加機能の提供に対応している（根拠: PHP extensions）


### 利用例

- Web開発のためのスクリプト言語の実行環境として利用する（README明記／根拠: README冒頭）

- ソースコードからPHPをビルドしてカスタム環境にインストールする（README明記／根拠: Building PHP source code）

- 付属のテストスイートを使用してPHPの品質や動作を確認する（README明記／根拠: Testing PHP source code）


### 最初に試すこと

ソースコードからPHPをビルドするための設定ファイルを生成する

1. ./buildconf


成功の目安: 設定スクリプトが正常に生成されること

未確認: 具体的なPHPの言語仕様や各関数の詳細な挙動／すべての拡張機能の完全な一覧と個別設定方法


## 3. [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

**概要:** Claude Code上で動作する無料のオープンソースSEOプラグインであり、技術的SEO、コンテンツの品質、構造化データ、AI検索（GEO）、ローカル・ECサイトのSEO監査を並行エージェントで実行し、優先順位付きの行動計画を提供します。

- 言語: Python
- 今週のスター: 4110
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


## 4. [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

**概要:** コーディングエージェント向けのデザイン語彙および支援ツールであり、デザインの改善、レビュー、品質監査、AI特有のありふれたデザイン（AI slop）の検出を行います。

- 言語: Rust
- 今週のスター: 9713
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

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


## 5. [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)

**概要:** Andrej KarpathyのLLMコーディングにおける指摘をもとに作られた、Claude Codeの挙動を改善する単一のCLAUDE.mdファイルおよび関連ガイドラインです。

- 言語: 不明
- 今週のスター: 4250
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




## 6. [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

**概要:** TradingAgentsは、実際の証券会社のダイナミクスを模倣したマルチエージェント型の金融取引フレームワークです。ファンダメンタルズ分析、センチメント分析、ニュース分析、テクニカル分析などの専門的な役割を持つLLM駆動のエージェントが協力して市場状況を評価し、取引の意思決定を支援します。

- 言語: Python
- 今週のスター: 5557
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


## 7. [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)

**概要:** hugohe3/ppt-masterは、PDF、DOCXファイル、ウェブページなどのソース資料やトピックから、ネイティブに編集可能なPowerPointのプレゼンテーション（.pptx）をAIによって自動生成するPythonツールです。フラットな画像ではなく、スライドマスター、図形、データに基づいたグラフやテーブル、トランジションやアニメーションを備えた実際のPowerPointファイルを出力します。

- 言語: Python
- 今週のスター: 4980
- ライセンス: MIT
- AI分析状態: ok

### できること

- PDF、DOCXファイル、ウェブページなどのソース資料から編集可能なPowerPointのプレゼンテーション（.pptx）を生成する（根拠: README冒頭）

- スライドマスター、ネイティブな図形、データに基づいたグラフやテーブルなど、PowerPointのネイティブオブジェクトを構築する（根拠: Product Positioning）

- 既存の.pptxファイルに新しいコンテンツを流し込みながらデザインを維持する機能を提供する（根拠: Product Positioning）


### 利用例

- PDFなどの資料をもとに、編集可能なPowerPointの発表資料をAIで自動作成する（README明記／根拠: README冒頭）

- 既存のブランド用テンプレートやデッキの構成を維持したまま、新しい内容でスライドを再構築する（README明記／根拠: Product Positioning）

- 完成したスライドに対して、ネイティブなトランジションやアニメーション、音声ナレーションを追加する（README明記／根拠: Product Positioning）


### 最初に試すこと

プロジェクトのソースコードをクローンし、依存関係をインストールした上で、エージェントを使ってPPTを生成する

1. git clone https://github.com/hugohe3/ppt-master.git

2. cd ppt-master

3. pip install -r requirements.txt


成功の目安: 依存関係のインストールが完了し、AIチャットまたはエージェントを通じてソース資料から.pptxファイルが正常に出力されること




## 8. [obra/superpowers](https://github.com/obra/superpowers)

**概要:** Superpowersは、AIコーディングエージェント向けのエージェントスキルフレームワークおよびソフトウェア開発方法論であり、ブレインストーミングやテスト駆動開発などのスキルを自動的に組み合わせて開発プロセスをサポートします。

- 言語: Shell
- 今週のスター: 4894
- ライセンス: MIT
- AI分析状態: ok

### できること

- コードを書く前に意図や仕様を引き出すブレインストーミング機能（根拠: The Basic Workflow）

- 仕様に基づいた詳細な実装計画の作成機能（根拠: The Basic Workflow）

- テスト駆動開発（TDD）の強制とサブエージェントによる開発進行（根拠: The Basic Workflow）


### 利用例

- コーディングエージェントに自動で要件定義や設計を行わせる（README明記／根拠: How it works）

- AIエージェントにテスト駆動開発を実施させて品質を保つ（README明記／根拠: The Basic Workflow）

- 複数タスクをサブエージェントに自律的に処理させる（README明記／根拠: How it works）


### 最初に試すこと

Antigravity環境にSuperpowersプラグインをインストールする

1. agy plugin install https://github.com/obra/superpowers


成功の目安: プラグインがインストールされ、using-superpowersスキルによって会話の最初でスキルが読み込まれること




## 9. [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

**概要:** anthropic/knowledge-work-pluginsは、Claudeを専門業務特化型のアシスタントに変えるためのオープンソースプラグイン集です。Claude CoworkおよびClaude Codeで利用でき、スキル、コネクター、スラッシュコマンド、サブエージェントをバンドルしてタスクを効率化します。

- 言語: Python
- 今週のスター: 2504
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


## 10. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

**概要:** Taste Skillは、コーディングエージェントにデザインの感性、実際の画像、実際のブラウザでの検証機能を与え、一般的なAIによるページではなく、高品質なウェブサイトやアプリ画面を設計できるようにするエージェントスキルです。

- 言語: JavaScript
- 今週のスター: 4359
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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



## Zenn

- [元フロントエンドエンジニアがプロダクトエンジニアとして強制成長した1年](https://zenn.dev/dress_code/articles/bbc5159fefbd2c) — もず

- [Claude Codeで「QAチーム」を組んだら、効いたのは「捨てる仕組み」だった ― AIだけが見つけた不具合・見逃しは？](https://zenn.dev/sre_holdings/articles/d4acb079680a79) — SNabe

- [GitHub Actions で checkout@v7 のようなバージョン指定を書くのはやめよう！ 時代は actions.lock！](https://zenn.dev/progate/articles/24b1140180300c) — 横江（よこえ）

- [Expo アプリを iPhone Duo に対応させる](https://zenn.dev/chot/articles/5718685fde3626) — yoshino

- [KaniによるVerylコンパイラの形式検証](https://zenn.dev/dalance/articles/44a8f80ea0cfa1) — dalance

- [Claude Codeを褒めちぎってみた](https://zenn.dev/devlog/articles/abc194ecf04dfc) — Sato Kotaro

- [OpenSearchのLLM-as-a-Judgeを日本語の商品検索で動かして、人手ラベルと比べてみた](https://zenn.dev/nextbeat/articles/c22b45b1d784b0) — nkhr

- [PHP5.4 から PHP8.5へ](https://zenn.dev/ctrlzr/articles/5a88eb939b3bfd) — ctrlzr

- [いいから休め - Black October が終わる今、セキュリティエンジニアがやるべきこと](https://zenn.dev/nayuta/articles/aec9ab2e11a7b7) — nayuta

- [人間が見るのは設計書だけ ― PdM不在・バグ修正中心のチームで、AI-DLCを開発フローごと作り直した話](https://zenn.dev/canly/articles/85dc645c252832) — kszk103

- [公表資料から読む2026年秋の情報漏えい18件：侵入経路はどこだったのか](https://zenn.dev/shirochan/articles/f579ce70b08dc3) — しろちゃん

- [Auto mode時代のClaude Codeを守る。検証済み10キットで始めるセキュリティ対策【全員・チーム・組織別】](https://zenn.dev/sonicmoov/articles/67aaeb49be69ec) — azarashi

- [Flutter やめました。電話アプリを Native にした理由](https://zenn.dev/ivry/articles/d155267331a3ca) — tsutou

- [AIエージェントに設計書レビューを任せたらレビュワーは楽になった。でも現場は？？](https://zenn.dev/nttdata_tech/articles/6a06f484ebfab7) — kazuma sugiyama

- [【Rails】焼きなまし法で会議室予約アプリに空き時間最適化機能を実装してみた](https://zenn.dev/port_inc/articles/eaf460ff291c97) — koyu5000

- [Claude Codeで半年分のレビュー指摘を分類してみた](https://zenn.dev/port_inc/articles/a4bc3b39f44459) — なお

- [コードを読まずにマージするために必要なこと](https://zenn.dev/nrs/articles/c777388530aa84) — nrs

- [学生2人で日本語音声LLMを作り、FT-LLM 2026 自由形タスクで1位を獲得した話](https://zenn.dev/ayutaso/articles/ftllm2026-ja-speech-llm) — Atotti

- [AI の謎な説明文を直すスキル](https://zenn.dev/microsoft/articles/explain-before-shorten) — Kazuki Ota

- [最近の E2E 戦略（2026 年 10 月現在）](https://zenn.dev/polyco/articles/26624b38c951b5) — Tatsunori Nakano


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。