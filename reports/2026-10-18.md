# Tech Daily — 2026-10-18

生成日時: 2026-10-18T08:19:44.572937+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、ネイティブバイナリ、アプリ、実行時の振る舞いなどをAIエージェントと連携してリバースエンジニアリングするためのModel Context Protocol（MCP）ツールです。ソースコードがない状態でもアプリを調査し、仕組みを解析して証拠とともに提示します。

- 言語: TypeScript
- 今週のスター: 248962
- ライセンス: MIT
- AI分析状態: ok

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
- 今週のスター: 20267
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

**概要:** AnyPS5は、PS5の実行ファイルをLinuxおよびWindows向けに自動移植するためのツールです。エミュレーションや別プロセスの実行を行わず、ネイティブ形式への変換やシステムライブラリの実装を提供します。

- 言語: C++
- 今週のスター: 20518
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
- 今週のスター: 9024
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


## 5. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**概要:** anthropic/claude-plugins-official は、Claude Code向けの高品質なプラグインを集めた公式ディレクトリです。Anthropicが管理する内部プラグインと、コミュニティやパートナーによる外部プラグインを提供しています。

- 言語: Python
- 今週のスター: 2328
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


## 6. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを確定的なMP4動画に変換するためのオープンソースフレームワークです。AIコーディングエージェントとの統合や、CLI、ホスト型オーサリングのレンダリングコアとしての利用を想定して設計されています。

- 言語: TypeScript
- 今週のスター: 5601
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




## 7. [mksglu/context-mode](https://github.com/mksglu/context-mode)

**概要:** Context Modeは、AIコーディングエージェントのコンテキストウィンドウを最適化するためのMCPサーバーです。ツール出力をサンドボックス化して削減し、SQLiteによるセッションメモリの永続化、コード実行によるコンテキスト節約、そして17のプラットフォームにわたるセキュリティ権限の強制を行います。

- 言語: TypeScript
- 今週のスター: 4207
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


## 8. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

**概要:** Ghidraは、アメリカ国家安全保障局（NSA）が開発したソフトウェアリバースエンジニアリング（SRE）フレームワークです。コンパイルされたコードの解析を行うための逆アセンブル、アセンブル、逆コンパイル、グラフ化、スクリプト実行などの高度なツールを備えています。

- 言語: Java
- 今週のスター: 7510
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


## 9. [mattpocock/skills](https://github.com/mattpocock/skills)

**概要:** mattpocock/skillsは、Claude Code、Codex、GitHub CopilotなどのAIコーディングエージェント向けに設計された、小型で拡張可能なエージェントスキルのコレクションです。要件定義の精緻化、共有言語の構築、テスト駆動開発（TDD）、コードベースのアーキテクチャ改善など、実際のソフトウェアエンジニアリングを支援する様々なスキルを提供します。

- 言語: Shell
- 今週のスター: 11937
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


## 10. [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context)

**概要:** billion-contextは、小さなコンテキストウィンドウでも動作し、トークン消費量を抑えて超長時間のセッションを可能にするコンテキスト圧縮プラグインです。

- 言語: TypeScript
- 今週のスター: 779
- ライセンス: NOASSERTION
- AI分析状態: ok

### できること

- コンテキストの圧縮により、トークン消費量を5倍削減します。（根拠: README冒頭）

- ネイティブプラグイン、ランLauncher、URL変更の3つの方法で利用できます。（根拠: Quickstart）


### 利用例

- 数ヶ月に及ぶ長時間のセッションでコンテキスト管理を行う（README明記／根拠: README冒頭）


### 最初に試すこと

billion-contextをインストールする

1. npm install -g billion-context --prefix=~/.local


成功の目安: グローバル領域にパッケージがインストールされること

未確認: 具体的な対応クライアントの全リストや詳細な設定手順



## Zenn

- [論文サマリ「随意運動の制御と学習のための階層的ニューラルネットワークモデル」川人ら](https://zenn.dev/zhidao/articles/63db6db6abe9c4) — Zhidao

- [ポートフォリオをVoidで作り直したので、Voidの来歴と中身を整理する](https://zenn.dev/nkzn/articles/my-first-void) — Nkzn

- [コネクタも API も無いサービスを、Claude Code に操作させる](https://zenn.dev/edash_tech_blog/articles/6250fc61ccf009) — じょーじ

- [LLMにとって書きやすい構文とは何か：`end` と `end func foo` を1,000回以上比べてみた](https://zenn.dev/nextbeat/articles/2026-10-syntax-locality-llm) — kmizu

- [技術書を年に数冊しか買わない自分に、O'Reillyのサブスク年$150は割に合うか（ACM経由で契約してMCPまで）](https://zenn.dev/sonicmoov/articles/oreilly-subscription-acm) — m.okamura

- [ベクトルDBを使わない「階層ナビゲーション型RAG」を作って、ベクトルDB版RAGと比較してみた](https://zenn.dev/aiforall/articles/8e1803396534de) — nishina

- [有名 OSS が PR を閉じはじめた。何が起きていて、どう向き合うか](https://zenn.dev/hand_dot/articles/ecb391d4322330) — Kyohei Fukuda

- [国産モデル sarashina3-mini は日本語の推敲で何を変えるのか？](https://zenn.dev/algoartis/articles/03ca12150ccbee) — 大賀愛一郎（oga_aiichiro）

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

- [Claude Codeに過去の会話を思い出させる](https://zenn.dev/babarot/articles/claude-code-session-recall) — babarot

- [モバイルアプリ開発でノートPCを持ち歩かなくなった話](https://zenn.dev/yasi/articles/mobile-dev-from-phone-with-claude) — yasi


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。