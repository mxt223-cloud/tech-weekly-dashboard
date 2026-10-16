# Tech Daily — 2026-10-17

生成日時: 2026-10-17T08:47:03.392463+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、ネイティブバイナリ、アプリ、ランタイム動作などをエージェント経由でリバースエンジニアリングするためのModel Context Protocol（MCP）ツールです。ソースコードがないアプリの調査、仕組みの解説、証拠の提示、プロジェクトへの機能実装支援などをローカル環境で実行できます。

- 言語: TypeScript
- 今週のスター: 239477
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- ネイティブバイナリの擬似コード、アセンブリ、文字列、シンボル、呼び出し、参照の検査（根拠: What you can analyze）

- JavaScriptやElectronアプリケーションのモジュール、インポート、ソースマップ、ルート、IPC、ネイティブアドオン関係の復元（根拠: What you can analyze）

- Claude Code、Codex、Cursor、Gemini CLI、Grok BuildなどのエージェントへのMCPサーバー登録とワークフローインストールのセットアップ（根拠: Quick start）


### 利用例

- アプリに見つけた機能の仕組みをエージェントに調査させ、根拠となる証拠を確認した上で、自分のプロジェクト向けに同様の機能を構築する（README明記／根拠: README冒頭）

- 抽出したJavaScriptやElectronアプリのディレクトリまたはASARファイルを対象に、モジュールやインポート、Electronの境界などの情報をJSON形式で取得する（README明記／根拠: Quick start）

- 対応する逆アセンブラや解析エンジンと連携し、バイナリの内部構造や難解な処理のロジックを静的解析してコードの再構築に役立てる（提案／根拠: What you can analyze）


### 最初に試すこと

エージェントにREAの初期セットアップを行い、機能調査の指示を出すこと

1. Node.jsとnpmがインストールされた環境で `npx rea-agents setup` を実行する

2. 使用するエージェントを選択し、変更内容を確認して承認する

3. エージェントを再起動する

4. 「Notesアプリの検索機能の仕組みを理解し、証拠を示し、私のプロジェクト用に似た機能をビルドしてください」のようにエージェントに依頼する


成功の目安: エージェントがREAのMCPサーバー経由でターゲットアプリの調査を行い、その仕組みの解説や証拠、実装の提案を返すこと

未確認: 対応しているすべてのエージェントの詳細な内部動作仕様／サポートされるサードパーティ製逆アセンブラのすべてのライセンス検証メカニズムの詳細


## 2. [storytold/artcraft](https://github.com/storytold/artcraft)

**概要:** ArtCraftは、アーティスト、デザイナー、映画制作のためのインタラクティブなAI画像および動画制作IDEです。2Dでの構成、3Dでのシーン配置、多彩なAIモデルの選択を組み合わせ、プロンプト入力を視覚的なクラフト作業へと変化させます。

- 言語: Rust
- 今週のスター: 22319
- ライセンス: Apache-2.0
- AI分析状態: ok

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

**概要:** AnyPS5は、PS5の実行ファイルをLinuxおよびWindows向けに自動移植するためのツールです。エミュレーションや別プロセスの実行を行わず、ネイティブ形式への変換やシステムライブラリの実装を提供します。

- 言語: C++
- 今週のスター: 25174
- ライセンス: GPL-2.0
- AI分析状態: ok（キャッシュ）

### できること

- 実行ファイルをターゲットシステムのネイティブ形式に変換するrelinkerが含まれています。（根拠: About）

- 動的リンクに適したシステムprxライブラリの実装が含まれています。（根拠: About）

- シェーダーrecompilerによりSPIR-Vを生成できます。（根拠: About）


### 利用例

- PS5の実行ファイルをLinuxおよびWindowsへ自動移植する（README明記／根拠: About）

- SDLマッピングされたゲームコントローラーやキーボード・マウスによる操作設定を行う（README明記／根拠: Input mapping）


### 最初に試すこと

Webコンバーターを使用してファイルを変換する

1. Web converterのページにアクセスする


成功の目安: ファイルがデバイス内に保持された状態でコンバーターを利用できること

未確認: 具体的なビルドコマンドやインストール手順のコードブロックはREADMEに含まれていないため不明


## 4. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

**概要:** diagram-designは、独立したHTMLおよびSVGファイルとしてブランドに合わせたダイアグラムを作成できるAIエージェント向けのスキルです。Claude Code、Cursor、GitHub Copilotなどの様々なエージェントスキルホストに対応し、多数のダイアグラムタイプを生成できます。

- 言語: HTML
- 今週のスター: 10237
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


## 5. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを確定的なMP4動画に変換するためのオープンソースフレームワークです。AIコーディングエージェントとの統合や、CLI、ホスト型オーサリングのレンダリングコアとしての利用を想定して設計されています。

- 言語: TypeScript
- 今週のスター: 5318
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




## 6. [mattpocock/skills](https://github.com/mattpocock/skills)

**概要:** mattpocock/skillsは、Claude Code、Codex、GitHub CopilotなどのAIコーディングエージェント向けに設計された、小型で拡張可能なエージェントスキルのコレクションです。要件定義の精緻化、共有言語の構築、テスト駆動開発（TDD）、コードベースのアーキテクチャ改善など、実際のソフトウェアエンジニアリングを支援する様々なスキルを提供します。

- 言語: Shell
- 今週のスター: 12147
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


## 7. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

**概要:** Ghidraは、アメリカ国家安全保障局（NSA）が開発したソフトウェアリバースエンジニアリング（SRE）フレームワークです。コンパイルされたコードの解析を行うための逆アセンブル、アセンブル、逆コンパイル、グラフ化、スクリプト実行などの高度なツールを備えています。

- 言語: Java
- 今週のスター: 6614
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


## 8. [mksglu/context-mode](https://github.com/mksglu/context-mode)

**概要:** Context Modeは、AIコーディングエージェントのコンテキストウィンドウを最適化するためのMCPサーバーです。ツール出力をサンドボックス化して削減し、SQLiteによるセッションメモリの永続化、コード実行によるコンテキスト節約、そして17のプラットフォームにわたるセキュリティ権限の強制を行います。

- 言語: TypeScript
- 今週のスター: 4038
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


## 9. [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context)

**概要:** billion-contextは、小さなコンテキストウィンドウでも動作し、トークン消費量を削減して長時間のセッションを可能にするコンテキスト圧縮プラグインです。

- 言語: TypeScript
- 今週のスター: 659
- ライセンス: NOASSERTION
- AI分析状態: ok（キャッシュ）

### できること

- コンテキストの圧縮を行い、トークン数を約5分の1に削減する。（根拠: README冒頭）

- 数か月にわたる数十億トークンの単一セッションを維持する。（根拠: README冒頭）


### 利用例

- 小さなコンテキストウィンドウ環境で長時間のAIセッションを実行する（README明記／根拠: README冒頭）

- AIコーディングエージェントのトークン消費を抑えてコストを削減する（提案／根拠: README冒頭）


### 最初に試すこと

billion-contextをインストールする

1. npm install -g billion-context --prefix=~/.local


成功の目安: グローバル環境にパッケージがインストールされること

未確認: プラグインの詳細な設定方法や対応している全てのクライアントの詳細なリスト／プロキシの動作に関する詳細な内部仕様


## 10. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**概要:** anthropic/claude-plugins-official は、Claude Code向けの高品質なプラグインを集めた公式ディレクトリです。Anthropicが管理する内部プラグインと、コミュニティやパートナーによる外部プラグインを提供しています。

- 言語: Python
- 今週のスター: 2217
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



## Zenn

- [HTTP 402は29年「予約済み」のまま — x402をNext.jsで動かす](https://zenn.dev/suzuki_tech/articles/x402-01-http-402-nextjs) — SuzukiTech

- [[フィジカルAI]LLM によるテレオペデータで VLA を学習して Strands Robots に組み込んでみた](https://zenn.dev/aws_japan/articles/strands-robots-llm-teleop) — Hikotty / Hikoto Iseda

- [技術書を年に数冊しか買わない自分に、O'Reillyのサブスク年$150は割に合うか（ACM経由で契約してMCPまで）](https://zenn.dev/sonicmoov/articles/oreilly-subscription-acm) — m.okamura

- [ベクトルDBを使わない「階層ナビゲーション型RAG」を作って、ベクトルDB版RAGと比較してみた](https://zenn.dev/aiforall/articles/8e1803396534de) — nishina

- [有名 OSS が PR を閉じはじめた。何が起きていて、どう向き合うか](https://zenn.dev/hand_dot/articles/ecb391d4322330) — Kyohei Fukuda

- [2026年に自作Swingコンポーネントを紹介する](https://zenn.dev/desktopgame/articles/372d43b8e0777b) — desktopgame

- [ICFPC2026 参加記](https://zenn.dev/algoartis/articles/b5dd3c401d5dd4) — がんぽん

- [国産モデル sarashina3-mini は日本語の推敲で何を変えるのか？](https://zenn.dev/algoartis/articles/03ca12150ccbee) — 大賀愛一郎（oga_aiichiro）

- [OpenTelemetryでStep Functions越しにtraceparentを引き回し、複数Lambdaを一つのトレースにつなぐ](https://zenn.dev/boy_techblog/articles/connecting-trace-serverless) — watariryo

- [jpstatで始めるe-Stat API入門](https://zenn.dev/tyasuakwa/articles/3f6a1394323275) — tya-guin

- [【LocalLLM】Claude Codeの代わりになる？精度・同時人数・費用を検証](https://zenn.dev/solvio/articles/6d374a9224327a) — okawa2929

- [Akinatorで始めるAgentic RL ー タスク設計と初期検証  ー](https://zenn.dev/mkj/articles/8e1da67da67f98) — クリリン

- [レポ：mixi2のインターンに参加しました！](https://zenn.dev/riochin/articles/mixi2-intern-2026) — Riochin

- [改めて考える、AIエンジニアリングの今](https://zenn.dev/r_kaga/articles/2fd185c50cea7c) — r.kagaya

- [【セキュリティ】お客さんからの「うちは大丈夫？」に答えるため、IPAの点検項目をレガシーPHPのECサイトで上から順にやってみた](https://zenn.dev/subara3/articles/b90ff538d87aa6) — Subara3

- [Gemini 4 Argonの日本語性能を検証してみた](https://zenn.dev/algoartis/articles/19bb1705ea4b16) — 大賀愛一郎（oga_aiichiro）

- [『現場で役立つシステム設計の原則』を読んで学んだこと、実践したこと、これからやりたいこと](https://zenn.dev/wwwave/articles/38b8284f96bd9e) — 塚本

- [話題の逆解析 MCP「REA」を Claude Code に隔離してつないだ——静的解析の A/B 試験と安全設計](https://zenn.dev/keigoly/articles/8738d8d241b5a1) — keigoly

- [良いテストを書き、良いテストを見分ける ─『単体テストの考え方/使い方』のエッセンス](https://zenn.dev/nexta_/articles/unit-testing-principles-essence) — tetsu.k

- [SQLite 本体にベクトル検索拡張 vec1 がやってきた](https://zenn.dev/mattn/articles/6e9996319ac099) — mattn


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。