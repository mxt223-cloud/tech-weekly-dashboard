# Tech Daily — 2026-10-19

生成日時: 2026-10-19T08:33:38.847463+09:00  
AI分析: 9/10件成功（gemini-3.5-flash-lite）


## 1. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、ネイティブバイナリ、アプリ、実行時の振る舞いなどをAIエージェントと連携してリバースエンジニアリングするためのModel Context Protocol（MCP）ツールです。ソースコードがない状態でもアプリを調査し、仕組みを解析して証拠とともに提示します。

- 言語: TypeScript
- 今週のスター: 239923
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- ネイティブバイナリ、JavaScript/Electronアプリ、.NETアセンブリ、ウェブサイトなどをエージェントのツールで検査し、解析結果を証拠付きで取得できます。（根拠: README冒頭）

- Hopper、Ghidra、IDAなどのネイティブ解析エンジンと連携し、擬似コードやアセンブリ、文字列などを取得できます。（根拠: What you can analyze）

- 抽出したJavaScriptやElectronアプリのディレクトリまたはASARを対象に、モジュール、インポート、Electron境界などの情報をJSON形式で取得できます。（根拠: Quick start）


### 利用例

- アプリに見つけた機能の仕組みを調査し、自分のプロジェクト用に同様の機能を構築する。（README明記／根拠: README冒頭）

- 抽出したJavaScript/Electronアプリのファイルパスを指定して、モジュールやインポート、Electron境界の情報を確認する。（README明記／根拠: Quick start）

- 対応するバイナリやアプリケーションをローカル環境で安全に静的・動的解析し、ソフトウェアの相互運用性や構造を調査する。（提案／根拠: Disclaimer）


### 最初に試すこと

REAのエージェント設定と最小限の動作確認を行うこと

1. npx rea-agents setup


成功の目安: エージェントを選択し、変更内容を確認して承認することで、REAのMCPサーバとワークフロー指示が登録されること

未確認: サポートされている全ての外部解析ツールの詳細なライセンス要件／特定の環境における例外的なエラーハンドリングの詳細


## 2. [storytold/artcraft](https://github.com/storytold/artcraft)

**概要:** ArtCraftは、アーティスト、デザイナー、映画制作のためのインタラクティブなAI画像および動画制作IDEです。2Dでの構成、3Dでのシーン配置、多彩なAIモデルの選択を組み合わせ、プロンプト入力を視覚的なクラフト作業へと変化させます。

- 言語: Rust
- 今週のスター: 18479
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- 3D空間内での背景、前景、プロップのレイヤー合成による奥行きのある構成（根拠: Show, Don't Tell: Advanced Crafting Features）

- 画像を3Dメッシュオブジェクトへ変換し、正確な位置調整や回転、フレーミングが可能（根拠: Show, Don't Tell: Advanced Crafting Features）

- テキストプロンプトからの画像生成および、描画・マスク・インペインティングを活用したキャンバス画像編集（根拠: Quick and Easy Prompting）


### 利用例

- 仮想の登場人物を一定の環境に配置し、同一の部屋で複数ショットを計画する（README明記／根拠: Show, Don't Tell: Advanced Crafting Features）

- 3Dアセットキットを組み合わせて、カメラアングルやオブジェクト配置、奥行きを制御するシーンブロッキングを行う（README明記／根拠: Show, Don't Tell: Advanced Crafting Features）

- 選択した動画モデルと生成コントロールを使用して画像をアニメーション化し、動画を作成する（README明記／根拠: Quick and Easy Prompting）


### 最初に試すこと

アプリケーションのダウンロードまたはソースからのビルドを行い、ArtCraftを起動して使い始める

1. 公式サイトやGitHub ReleasesからWindowsおよびmacOS向けの安定版をダウンロードしてインストールするか、_docs/dev_setup.mdを参照してソースからビルドする


成功の目安: ArtCraftが手元の環境で起動し、IDEインターフェースを利用できるようになること

未確認: 具体的なインストールコマンドや実行コマンドがREADME内に記載されていないため、CLI上での操作手順は不明です。


## 3. [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5)

**概要:** AnyPS5は、PS5の実行ファイルをLinuxおよびWindows向けに自動で移植するためのツールです。エミュレーションや独立したランタイムプロセスを使用せず、ネイティブ形式への変換やシステムライブラリの実装を行います。

- 言語: C++
- 今週のスター: 16250
- ライセンス: GPL-2.0
- AI分析状態: ok

### できること

- PS5の実行ファイルをLinuxおよびWindows向けに自動移植するリリンカーを含みます。（根拠: About）

- macOS（Appleシリコンを含む）でリリンカーのみのビルドを実行可能です。（根拠: About）

- SDLマッピングされたゲームコントローラー（アナログスティックやトリガーを含む）をサポートし、キーボードとマウスは設定ファイルで構成可能です。（根拠: Input mapping）


### 利用例

- PS5の実行ファイルをLinuxやWindowsのネイティブ形式に変換する。（README明記／根拠: About）

- デバイス上でファイルを処理できるWebコンバーターを使用する。（README明記／根拠: About）

- ゲームコントローラーやキーボード・マウスの入力マッピングを設定して操作する。（README明記／根拠: Input mapping）


### 最初に試すこと

Webコンバーターを利用してファイルを処理する

1. Webコンバーターのページにアクセスする

2. ファイルがデバイス内に留まることを確認して変換作業を行う


成功の目安: ブラウザ上でコンバーター機能を利用できること

未確認: 具体的なコマンドライン引数やインストールコマンド


## 4. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**概要:** anthropic/claude-plugins-official は、Claude Code向けの高品質なプラグインを集めた公式ディレクトリです。Anthropicが管理する内部プラグインと、コミュニティやパートナーによる外部プラグインを提供しています。

- 言語: Python
- 今週のスター: 3581
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- Claude Codeのプラグインシステムを使用して、マーケットプレイスからプラグインを直接インストールできる機能（根拠: Installation）

- プラグインのメタデータ、MCPサーバー設定、スラッシュコマンド、エージェント、スキルなどを定義する標準構造を提供する機能（根拠: Plugin Structure）

- マニフェストファイルを持たないスキルバンドルリポジトリのスキル群を明示的な配列で宣言して公開できる機能（根拠: Skill-bundle plugins）


### 利用例

- Claude Codeに公式またはサードパーティの高品質なプラグインを追加して機能を拡張する（README明記／根拠: Claude Code Plugins Directory）

- 独自のプラグインを作成して公開・登録申請を行う（README明記／根拠: Contributing）


### 最初に試すこと

Claude Code上でプラグインをインストールする

1. Claude Code内で /plugin install {plugin-name}@claude-plugins-official を実行する、または /plugin > Discover からプラグインを探してインストールする


成功の目安: 指定したプラグインがClaude Codeに正常にインストールされること

未確認: 具体的な個別のプラグインが何を提供するのかという機能詳細


## 5. [mksglu/context-mode](https://github.com/mksglu/context-mode)

**概要:** Context Modeは、AIコーディングエージェントのコンテキストウィンドウを最適化するためのMCPサーバーです。ツール出力をサンドボックス化して削減し、SQLiteによるセッションメモリの永続化、コード実行によるコンテキスト節約、そして17のプラットフォームにわたるセキュリティ権限の強制を行います。

- 言語: TypeScript
- 今週のスター: 4438
- ライセンス: NOASSERTION
- AI分析状態: ok（キャッシュ）

### できること

- ツール出力をサンドボックス化し、コンテキストウィンドウの生データを削減する（根拠: How Context Mode Solves It）

- SQLiteを使用してファイル編集やgit操作などのセッション情報を追跡し、会話の圧縮後も関連情報を取得できるようにする（根拠: How Context Mode Solves It）

- LLMにスクリプトを書かせて実行させることで、大量のツール呼び出しによるコンテキスト消費を抑える（根拠: How Context Mode Solves It）


### 利用例

- PlaywrightのスナップショットやGitHubのIssue、アクセスログなどの大量の生データがコンテキストを圧迫する問題を解決する（README明記／根拠: The Problem）

- コードベースの解析や集計を行う際、ファイル群を直接読み込ませる代わりにスクリプトで処理して結果のみを出力させる（README明記／根拠: How Context Mode Solves It）

- sudoや機密ファイルへのアクセスなどの危険な操作をMCPサンドボックス内で制限する（README明記／根拠: Security）


### 最初に試すこと

セキュリティ権限設定を追加して権限ルールを適用する

1. プロジェクトの .claude/settings.json（またはグローバルの ~/.claude/settings.json）に権限設定のJSONを追加する


成功の目安: 設定ファイルにdenyやallowのルールが正しく記述され、セキュリティポリシーとして読み込まれる状態になること

未確認: 詳細なインストール手順や具体的なnpmコマンド等のクイックスタート手順／17のプラットフォームすべての個別設定方法


## 6. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

**概要:** diagram-designは、独立したHTMLおよびSVGファイルとしてブランドに合わせたダイアグラムを作成できるAIエージェント向けのスキルです。Claude Code、Cursor、GitHub Copilotなどの様々なエージェントスキルホストに対応し、多数のダイアグラムタイプを生成できます。

- 言語: HTML
- 今週のスター: 8382
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 独立したHTMLおよびSVGファイル形式でダイアグラムを描画する（根拠: README冒頭）

- 45種類のダイアグラムタイプをサポートする（根拠: README冒頭）

- npx skills add cathrynlavery/diagram-design を使ってインストールできる（根拠: Install）


### 利用例

- アプリのアーキテクチャ図（フロントエンド、バックエンド、データベース、Redisキャッシュ）を作成する（README明記／根拠: README冒頭）

- 影響度と労力を軸にしたQ2プロジェクトの四象限図を作成する（README明記／根拠: README冒頭）

- 401エラー時のトークンリフレッシュを含むベアラーコールのシーケンス図を作成する（README明記／根拠: README冒頭）


### 最初に試すこと

diagram-designスキルをインストールして使い始める

1. npx skills add cathrynlavery/diagram-design を実行してインストールする


成功の目安: エージェントスキルホストにdiagram-designがインストールされること

未確認: Quickstartセクションの具体的な手順やコードブロックがREADMEの途中で途切れており詳細が不明


## 7. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

**概要:** Ghidraは、アメリカ国家安全保障局（NSA）が開発したソフトウェアリバースエンジニアリング（SRE）フレームワークです。コンパイルされたコードの解析を行うための逆アセンブル、アセンブル、逆コンパイル、グラフ化、スクリプト実行などの高度なツールを備えています。

- 言語: Java
- 今週のスター: 7608
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- 逆アセンブル、アセンブル、逆コンパイル、グラフ化、スクリプト実行などの機能（根拠: README冒頭）

- 多様なプロセッサ命令セットや実行ファイルフォーマットのサポート（根拠: README冒頭）

- ユーザーインタラクティブモードおよび自動化モードでの実行（根拠: README冒頭）


### 利用例

- 複雑なSRE作業におけるスケーリングやチーム作業の問題解決（README明記／根拠: README冒頭）

- マルウェアのコード分析とネットワークやシステムの脆弱性理解のための洞察生成（README明記／根拠: README冒頭）

- JavaやPythonを使用した独自の拡張コンポーネントやスクリプトの開発（README明記／根拠: README冒頭）


### 最初に試すこと

公式の事前ビルド版をインストールして起動する

1. JDK 25 64-bitをインストールする

2. Ghidraのリリースファイルをダウンロードして解凍する

3. ./ghidraRun (Windowsの場合はghidraRun.bat)を実行して起動する


成功の目安: Ghidraが正常に起動すること

未確認: 具体的な対応プロセッサ命令セットや実行ファイルフォーマットの全リスト／セキュリティアドバイザリの詳細な脆弱性内容


## 8. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを確定的なMP4動画に変換するためのオープンソースフレームワークです。AIコーディングエージェントとの統合や、CLI、ホスト型オーサリングのレンダリングコアとしての利用を想定して設計されています。

- 言語: TypeScript
- 今週のスター: 5639
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- HTMLとCSS、シーク可能なアニメーションを使用して確定的なMP4動画を生成する（根拠: README冒頭）

- GSAP、CSSアニメーション、Lottie、Three.js、Anime.js、WAAPIなどのアニメーションライブラリやランタイムに対応する（根拠: How It Works）

- CLIやAWS Lambdaを用いたローカルおよび分散レンダリングに対応する（根拠: HyperFrames Stack）


### 利用例

- 製品発表動画や機能紹介動画の作成（README明記／根拠: What You Can Build）

- アニメーション付きコード差分、ナレーション、字幕を含むPRウォークスルーの作成（README明記／根拠: What You Can Build）

- データビュジュアライゼーション、チャートレース、マップアニメーションの制作（README明記／根拠: What You Can Build）


### 最初に試すこと

ローカル環境で動画プロジェクトを初期化し、プレビューおよびレンダリングを実行する

1. npx hyperframes init my-video

2. cd my-video

3. npx hyperframes preview

4. npx hyperframes render


成功の目安: ブラウザでのライブリロードによるプレビュー確認と、MP4形式へのレンダリングが成功すること




## 9. [cursor/plugins](https://github.com/cursor/plugins)

**概要:** Cursor plugin specification and official plugins

- 言語: TypeScript
- 今週のスター: 1536
- ライセンス: 不明
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



## 10. [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)

**概要:** ai-job-searchは、Claude Codeをベースにしたローカル実行型のAI求職・応募フレームワークです。求人情報の評価、履歴書の調整、カバーレターの作成、面接対策を自動化します。

- 言語: Python
- 今週のスター: 4200
- ライセンス: MIT
- AI分析状態: ok

### できること

- 求人情報の検索や評価、適合度のスコアリングを行う（根拠: What this is）

- LaTeXなどを用いて履歴書やカバーレターをカスタマイズして作成する（根拠: What this is）

- レビュアーエージェントによる批判的検証と修正を行う（根拠: What this is）


### 利用例

- 自身のプロフィールを設定して求人情報を効率よく探索する（README明記／根拠: What this is）

- 特定の求人URLに対して応募書類のドラフトを作成する（README明記／根拠: What this is）

- 面接に向けた準備や対策を行う（README明記／根拠: AI Job Search）


### 最初に試すこと

前提条件を確認し、セットアップの準備をする

1. Claude Code CLI、Python 3.10+、Bun、LaTeX環境がインストールされていることを確認する


成功の目安: 必要な前提ソフトウェアとツールがすべて用意されていること

未確認: Quick startセクションの具体的なインストール・実行コマンドのコードブロックが途中で途切れているため詳細なコマンド不明



## Zenn

- [インライン編集UIを拡張性が高い形で実装した](https://zenn.dev/numa_san/articles/50b847c58f0854) — ぬまさん

- [アプリケーションの自動テストとデプロイをCircleCIからGitHub Actionsに移行した](https://zenn.dev/tsukulink/articles/fea41a6e4113cf) — oieioi

- [読書メモ『入門 継続的デリバリー』](https://zenn.dev/95nm/articles/article_reading_cd) — ブルハツ

- [リトルの法則で考える障害時のキャパシティプランニング](https://zenn.dev/rea9r/articles/littles-law-capacity-planning) — rea9r

- [AI エージェントに個人の記憶を任せるときの、書かせない・漏らさない仕組み](https://zenn.dev/ketoranger/articles/agent-memory-security) — K-etoranger

- [ClaudeにiOSシミュレーターのスクリーンショットを読ませるのをやめて、操作で増えるコンテキストを43%削減した](https://zenn.dev/eai/articles/dont-let-agents-see-the-ios-sim-screen) — y.takahashi

- [AFM（Apple Foundation Models）を活用したテキストアドベンチャーゲームの開発【第2回】自由入力を台本の選択肢につなぐ](https://zenn.dev/gritchbreed/articles/ced633f449178f) — Hiroshi Arakane

- [MPC（モデル予測制御）専用ソルバーの歴史 ― プラントの分単位からマイクロ秒の組込み制御まで](https://zenn.dev/takuya_fukatsu/articles/d66e570b929d19) — 株式会社 Proxima Technology

- [日本語の個人情報を Bedrock Guardrails, SDP, Presidio でマスキングして比較する](https://zenn.dev/fusic/articles/a77ba348115364) — omiya

- [生産計画を手を動かして学ぶ ― OSS の frePPLe で MRP・需要予測・CP-SAT まで](https://zenn.dev/rkawajiri/books/frepple-tutorial-ja) — Ryoma Kawajiri

- [LLMエージェント基盤のシステム設計 #1 エージェントランタイム（Harness）](https://zenn.dev/acntechjp/articles/2246165a4098c5) — Yuuichi Eguchi

- [ポートフォリオをVoidで作り直したので、Voidの来歴と中身を整理する](https://zenn.dev/nkzn/articles/my-first-void) — Nkzn

- [コネクタも API も無いサービスを、Claude Code に操作させる](https://zenn.dev/edash_tech_blog/articles/6250fc61ccf009) — じょーじ

- [LLMにとって書きやすい構文とは何か：`end` と `end func foo` を1,000回以上比べてみた](https://zenn.dev/nextbeat/articles/2026-10-syntax-locality-llm) — kmizu

- [技術書を年に数冊しか買わない自分に、O'Reillyのサブスク年$150は割に合うか（ACM経由で契約してMCPまで）](https://zenn.dev/sonicmoov/articles/oreilly-subscription-acm) — m.okamura

- [ベクトルDBを使わない「階層ナビゲーション型RAG」を作って、ベクトルDB版RAGと比較してみた](https://zenn.dev/aiforall/articles/8e1803396534de) — nishina

- [有名 OSS が PR を閉じはじめた。何が起きていて、どう向き合うか](https://zenn.dev/hand_dot/articles/ecb391d4322330) — Kyohei Fukuda

- [国産モデル sarashina3-mini は日本語の推敲で何を変えるのか？](https://zenn.dev/algoartis/articles/03ca12150ccbee) — 大賀愛一郎（oga_aiichiro）

- [改めて考える、AIエンジニアリングの今](https://zenn.dev/r_kaga/articles/2fd185c50cea7c) — r.kagaya

- [『現場で役立つシステム設計の原則』を読んで学んだこと、実践したこと、これからやりたいこと](https://zenn.dev/wwwave/articles/38b8284f96bd9e) — 塚本


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。