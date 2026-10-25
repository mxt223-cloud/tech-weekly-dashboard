# Tech Daily — 2026-10-26

生成日時: 2026-10-26T08:28:36.450746+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

**概要:** cloudflare/security-audit-skillは、コーディングエージェントをセキュリティ監査人に変えるスキルリポジトリです。偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成という6つのフェーズで構造化されたセキュリティ監査を実行します。

- 言語: JavaScript
- 今週のスター: 12680
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




## 2. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**概要:** ruvnet/rufloは、Claude CodeやCodexなどのモデルを拡張するエージェントメタハーネスです。100種類以上の専門エージェント、協調スウォーム、自己学習メモリ、ゼロトラスト型のエージェント間フェデレーション機能などを提供し、複数エージェントによる自律的なワークフローの構築や会話型AIシステムの開発を支援します。

- 言語: TypeScript
- 今週のスター: 3241
- ライセンス: MIT
- AI分析状態: ok

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




## 3. [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

**概要:** anthropic/knowledge-work-pluginsは、Claudeを専門業務特化型のアシスタントに変えるためのオープンソースプラグイン集です。Claude CoworkおよびClaude Codeで利用でき、スキル、コネクター、スラッシュコマンド、サブエージェントをバンドルしてタスクを効率化します。

- 言語: Python
- 今週のスター: 2631
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


## 4. [anomalyco/opencode](https://github.com/anomalyco/opencode)

**概要:** anomalyco/opencodeは、オープンソースのAIコーディングエージェントであり、ターミナルUIやデスクトップアプリを通じて開発作業やコードの探索を支援します。

- 言語: TypeScript
- 今週のスター: 6857
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- buildエージェントによる開発向けのフルアクセスなコーディング作業（根拠: Agents）

- planエージェントによるコードの分析や読み取り専用の探索（根拠: Agents）

- Tabキーによるエージェント間の切り替え（根拠: Agents）


### 利用例

- 不慣れなコードベースの探索や変更の計画（README明記／根拠: Agents）

- 開発作業におけるフルアクセスなコーディング支援の利用（README明記／根拠: Agents）

- @generalを使用した複雑な検索や複数ステップのタスクの実行（README明記／根拠: Agents）


### 最初に試すこと

CLI環境でopencodeをインストールして使い始める

1. curl -fsSL https://opencode.ai/v2/install | bash


成功の目安: インストールスクリプトが正常に実行され、opencodeが利用可能になること

未確認: 詳細な設定方法やAIモデルのバックエンドに関する具体的な仕様／コントリビューション手順の細かいルール


## 5. [stablyai/orca](https://github.com/stablyai/orca)

**概要:** Orcaは、複数のコーディングエージェント（Claude Code、Codexなど）を並行して実行・管理するためのAIオーケストレーターです。デスクトップ、モバイル、リモートランタイムに対応しており、複数のエージェントを独立したワークツリーで同時に動かすことができます。

- 言語: TypeScript
- 今週のスター: 9828
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 独立したgitワークツリー上で複数のAIエージェントを並行して実行し、結果を比較してマージできる（根拠: Features）

- モバイルアプリを使用して、エージェントの作業完了の通知受け取りやスマホからのフォローアップ指示ができる（根拠: Features）

- Chromiumウィンドウ上のUI要素をクリックして、HTMLやCSS、切り抜きスクリーンショットをエージェントのプロンプトに送信できる（根拠: Features）


### 利用例

- 1つのプロンプトを複数のエージェントに同時に処理させ、最も優れた結果をマージする（README明記／根拠: Features）

- 外出先やデスクから離れた場所からでも、モバイル端末でAIエージェントの進捗監視や指示出しを行う（README明記／根拠: Features）

- アプリ内でGitHubのプルリクエストやIssue、プロジェクトボードを確認し、文脈を切り替えることなくワークツリーを開いてレビューする（README明記／根拠: Features）


### 最初に試すこと

Orcaデスクトップアプリをインストールして起動する

1. 公式サイト（onorca.dev/download）またはHomebrew（brew install --cask stablyai/orca/orca）などのパッケージマネージャーを使用してインストールする


成功の目安: Orcaデスクトップアプリが正常に起動すること

未確認: CONTRIBUTING.mdの詳細な開発手順／cloud/ディレクトリにあるリレーサーバーの具体的なセットアップ手順


## 6. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを決定論的なMP4動画に変換するためのオープンソースフレームワークです。CLIを用いたローカルでの操作や、AIコーディングエージェントからのスキル利用、ホスト型オーサリングワークフローのレンダリングコアとして機能します。

- 言語: TypeScript
- 今週のスター: 5633
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- HTMLとCSS、シーク可能なアニメーションを使用して動画を定義し、決定論的なMP4動画としてレンダリングする（根拠: How It Works）

- AIコーディングエージェント向けにスキルを提供し、エージェントから動画作成のワークループを実行できる（根拠: Quick Start）

- CLIを使用して、ローカルでのプロジェクトの初期化、ブラウザでのプレビュー、およびMP4へのレンダリングを行える（根拠: Quick Start）


### 利用例

- 製品のローンチ動画や機能紹介アニメーションの作成（README明記／根拠: What You Can Build）

- アニメーション付きのコード差分やナレーション、字幕を含むPRウォークスルーの作成（README明記／根拠: What You Can Build）

- データビジュアライゼーションやチャートレース、マップアニメーションの制作（README明記／根拠: What You Can Build）


### 最初に試すこと

HyperFramesを使用して新規プロジェクトを初期化し、ブラウザでプレビューした上でMP4にレンダリングする

1. npx hyperframes init my-video

2. cd my-video

3. npx hyperframes preview

4. npx hyperframes render


成功の目安: ブラウザでのライブリロードによるプレビュー確認と、MP4ファイルへのローカルレンダリングが成功すること

未確認: AWS Lambdaレンダリングの詳細な設定手順と内部アーキテクチャの具体的なコード実装


## 7. [android/skills](https://github.com/android/skills)

**概要:** Android開発向けのAI最適化されたモジュール式指示とリソースを提供するリポジトリです。LLMが苦手とするユースケースやワークフローを対象としています。

- 言語: Kotlin
- 今週のスター: 1317
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


## 8. [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

**概要:** Graphify-Labs/graphifyは、コードベースやドキュメント、SQLスキーマ、設定、PDFなどを検索可能なナレッジグラフに変換するツールです。Claude Code、Cursor、Codex、Gemini CLIなどのAIコーディングアシスタントで/graphifyスキルとして利用でき、ローカルでの決定論的なAST解析とベクトルストアを使わないグラフ構造を提供します。

- 言語: Python
- 今週のスター: 6868
- ライセンス: Apache-2.0
- AI分析状態: ok

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


## 9. [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

**概要:** ai-memoryは、複数のAIコーディングエージェント（Claude Code、Codex、Cursorなど）の間で長期的なコンテキストや作業の引き継ぎを共有するためのRust製ソリューションです。

- 言語: Rust
- 今週のスター: 3541
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


## 10. [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)

**概要:** ComfyUIは、グラフおよびノードインターフェースを備えた、強力でモジュール式の拡散モデル向けGUI、API、バックエンドです。

- 言語: Python
- 今週のスター: 4648
- ライセンス: GPL-3.0
- AI分析状態: ok（キャッシュ）

### できること

- 画像、動画、3Dモデル、音声などの生成や編集を行うための視覚的なノードグラフインターフェースを提供します。（根拠: Features）

- 非同期の重みストリーミング技術を使用して、一般的なコンシューマーハードウェア上で大規模なオープンソースモデルを実行できます。（根拠: README冒頭）

- 生成されたメディアのファイルから、使用されたシードや完全なワークフローを復元または読み込むことができます。（根拠: Features）


### 利用例

- ビジュアルプロフェッショナルがモデルやパラメーターを細部まで制御しながら画像や動画などのコンテンツを生成する。（README明記／根拠: README冒頭）

- APIエンドポイントを使用して本番パイプラインへワークフローをシームレスに統合する。（README明記／根拠: README冒頭）

- カスタムノードを導入して機能を拡張する。（README明記／根拠: Features）


### 最初に試すこと

ComfyUIの依存関係をインストールして起動する

1. リポジトリをクローンする

2. ComfyUIフォルダ内でターミナルを開き、依存関係をインストールする: pip install -r requirements.txt

3. ComfyUIを起動する: python main.py


成功の目安: ComfyUIが正常に起動し、Webブラウザ等からアクセスできる状態になること

未確認: 詳細なパフォーマンス数値や具体的な動作速度の保証範囲



## Zenn

- [Pythonの基礎学習が終わったら、Pythonでスクレイピングを始めよう！](https://zenn.dev/momiji_ai/articles/67c7ce4c54fad3) — meihao550

- [AlphaEngine : 最適化編②](https://zenn.dev/reu/articles/0f77f6eb0940af) — みぞれに

- [ros_gzの終了時クラッシュとRange変換の不具合を修正した話](https://zenn.dev/yuu7/articles/ros2-gazebo-teardown-range-fixes) — Yuu

- [600人規模のイベント運営を支えたインカムを、学生1人で作った話](https://zenn.dev/kodak_20/articles/3b0ba74333b56c) — コダック

- [Flutter アプリを iPhone Duo の「縦帯」に対応させる](https://zenn.dev/yus1127/articles/flutter-iphone-duo-vertical-bar) — ゆう

- [AWSにデプロイせず、FastAPI製Lambdaのarm64実行をCIで検証する](https://zenn.dev/shingokumon/articles/4da5acb9697d56) — shingokumon

- [Xcode 27 で ＠State がマクロになった理由 ― 遅延評価は private だけ、＠StateObject との違い](https://zenn.dev/takehito/articles/50145459523321) — 小清水 健人

- [@napi-rs/canvas v1.0.12 で実質的な破壊的変更が入った話](https://zenn.dev/devuloper/articles/napi_rs_canvas_1_0_12_font_tofu) — otoneko.

- [VueFes Japan 2026に参加してきた](https://zenn.dev/krz_tech/articles/vuefes_japan_2026) — くらず / kurazu

- [prpr: Rust 向けのシンプルで高速な Parser generator](https://zenn.dev/tanakh/articles/prpr-packrat-parser) — Hideyuki Tanaka

- [「読みにくいDB」はAI開発のコストを1.9倍にする――Claude Codeで検証したDB設計の影響](https://zenn.dev/actbe_tech/articles/8b4a9991d5365d) — 北野

- [eMudhraの中間CA証明書の秘密鍵を求めてみる](https://zenn.dev/herumi/articles/search_bad_emudhra_key) — herumi

- [AI が実装してくれる時代こそ、自分の手で実装しよう](https://zenn.dev/loglass/articles/24b2a4776ce8d4) — Firas

- [脆弱性管理の仕組みを整えた](https://zenn.dev/dress_code/articles/be5550254695cd) — anizozina

- [仕組みを理解する動画を、Claude Codeに作らせると便利すぎる](https://zenn.dev/explaza/articles/c749042ecbe232) — musoukun

- [コードレビューをなくして見えたもの](https://zenn.dev/henteko/articles/b76b15922cdf72) — henteko

- [バイブコーディングを6週間続けたら、Mac の起動が20分かかるようになった](https://zenn.dev/singularity/articles/vibe-coding-mac-boot-20min) — Isamu

- [Oxlint + Oxfmt で規約をコード化するモノレポ運用](https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006) — Toshiki Okazaki

- [Claude Code で CI 待ち時間を 18 分から 4 分台に短縮する【GitHub Actions】](https://zenn.dev/edash_tech_blog/articles/5b90aa33bd8d49) — iakito

- [AI時代、配布するPythonコードをどう守るか: 難読化の実験と判断軸](https://zenn.dev/pksha/articles/0f9c11d1daea2e) — 山本隼輔


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。