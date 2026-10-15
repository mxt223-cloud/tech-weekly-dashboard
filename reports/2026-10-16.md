# Tech Daily — 2026-10-16

生成日時: 2026-10-16T08:46:38.840618+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、ネイティブバイナリ、アプリ、ランタイム動作などをエージェント経由でリバースエンジニアリングするためのModel Context Protocol（MCP）ツールです。ソースコードがないアプリの調査、仕組みの解説、証拠の提示、プロジェクトへの機能実装支援などをローカル環境で実行できます。

- 言語: TypeScript
- 今週のスター: 214837
- ライセンス: MIT
- AI分析状態: ok

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


## 2. [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5)

**概要:** AnyPS5は、PS5の実行ファイルをLinuxおよびWindows向けに自動移植するためのツールです。エミュレーションや別プロセスの実行を行わず、ネイティブ形式への変換やシステムライブラリの実装を提供します。

- 言語: C++
- 今週のスター: 28240
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


## 3. [mattpocock/skills](https://github.com/mattpocock/skills)

**概要:** mattpocock/skillsは、Claude Code、Codex、GitHub CopilotなどのAIコーディングエージェント向けに設計された、小型で拡張可能なエージェントスキルのコレクションです。要件定義の精緻化、共有言語の構築、テスト駆動開発（TDD）、コードベースのアーキテクチャ改善など、実際のソフトウェアエンジニアリングを支援する様々なスキルを提供します。

- 言語: Shell
- 今週のスター: 12292
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


## 4. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを確定的なMP4動画に変換するためのオープンソースフレームワークです。AIコーディングエージェントとの統合や、CLI、ホスト型オーサリングのレンダリングコアとしての利用を想定して設計されています。

- 言語: TypeScript
- 今週のスター: 5123
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




## 5. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

**概要:** diagram-designは、独立したHTMLおよびSVGファイルとしてブランドに合わせたダイアグラムを作成できるAIエージェント向けのスキルです。Claude Code、Cursor、GitHub Copilotなどの様々なエージェントスキルホストに対応し、多数のダイアグラムタイプを生成できます。

- 言語: HTML
- 今週のスター: 10706
- ライセンス: MIT
- AI分析状態: ok

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


## 6. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

**概要:** Ghidraは、アメリカ国家安全保障局（NSA）が開発したソフトウェアリバースエンジニアリング（SRE）フレームワークです。コンパイルされたコードの解析を行うための逆アセンブル、アセンブル、逆コンパイル、グラフ化、スクリプト実行などの高度なツールを備えています。

- 言語: Java
- 今週のスター: 5613
- ライセンス: Apache-2.0
- AI分析状態: ok

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


## 7. [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context)

**概要:** billion-contextは、小さなコンテキストウィンドウでも動作し、トークン消費量を削減して長時間のセッションを可能にするコンテキスト圧縮プラグインです。

- 言語: TypeScript
- 今週のスター: 628
- ライセンス: NOASSERTION
- AI分析状態: ok

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


## 8. [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)

**概要:** earthtojake/text-to-cad は、AIエージェントにCADの機能や3Dモデル生成、製造性チェック、エンジニアリング図面の作成機能などを追加するためのプラグインおよびスキル集です。

- 言語: Python
- 今週のスター: 1994
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- STEP、GLB、STL、3MFファイル形式での3Dモデル生成（根拠: text-to-cad）

- 製造性のチェック（DfAMやDFMレビュー）やエンジニアリング図面の生成（根拠: text-to-cad）

- 3Dプリンティング、板金、CNC加工サービスへの接続（根拠: text-to-cad）


### 利用例

- プレーンテキストや画像のリクエストからCADモデルを作成・編集する（README明記／根拠: 🧰 Skills）

- ネジや軸受け、モーターなどの既製STEPパーツを検索する（README明記／根拠: 🧰 Skills）

- パーツから寸法付きのエンジニアリング図面をPDFとして作成する（README明記／根拠: 🧰 Skills）


### 最初に試すこと

エージェントにtext-to-cadをインストールする

1. エージェントに次のメッセージを送信する: Install text-to-cad from https://github.com/earthtojake/text-to-cad


成功の目安: エージェントがtext-to-cadのインストールを実行すること

未確認: エージェントごとの個別の詳細な内部動作や最新のAPI仕様の完全な網羅


## 9. [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)

**概要:** SwiftUI-Agent-Skillは、Claude CodeやCodexなどのAIコーディングアシスタントが、よりシンプルでモダンなSwiftUIコードを書くためのスキルを提供するツールです。

- 言語: 不明
- 今週のスター: 930
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- APIの使用方法、デザイン、パフォーマンス、アクセシビリティに関するガイダンスを提供する（根拠: README冒頭）

- ナビゲーション、レイアウト、アニメーション、状態管理、VoiceOver、非推奨APIなどに対応する（根拠: README冒頭）

- Claude CodeやCodex、Gemini、CursorなどのAIツールにnpxコマンドやプラグイン等でインストールできる（根拠: Installing SwiftUI Pro）


### 利用例

- AIコーディングアシスタントを使ってモダンで効率的なSwiftUIコードを作成する（README明記／根拠: README冒頭）

- プロジェクト内の非推奨APIの使用箇所をチェックする（README明記／根拠: Using SwiftUI Pro）

- プロジェクトのパフォーマンス問題やアクセシビリティを検証する（README明記／根拠: Using SwiftUI Pro）


### 最初に試すこと

npxを使用してSwiftUI Proスキルをインストールする

1. npx skills add https://github.com/twostraws/swiftui-agent-skill --skill swiftui-pro


成功の目安: エラーなくインストールが完了し、対象のエージェントやプロジェクトでスキルが選択・利用可能になること

未確認: 詳細な内部実装やサポートされているすべてのチェック項目の完全なリスト


## 10. [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym)

**概要:** openGym は、パスキー認証に対応し、自身のサーバーや端末でデータを管理できるセルフホスト型のジムおよび体重管理トラッカーです。ルーティンの計画やワークアウトの記録、筋肉の疲労度・回復状況の確認が行えます。

- 言語: JavaScript
- 今週のスター: 5132
- ライセンス: AGPL-3.0
- AI分析状態: ok

### できること

- 5,600種類以上の演目から曜日ごとのルーティンを計画したり、ボディマップや機器で絞り込みを行える。（根拠: Features）

- パスキー（Face ID、Touch ID、指紋認証）を利用した安全なログインや、デバイス間のデータ同期ができる。（根拠: Features）

- FitNotes、Strong、Hevyからのインポートや、全データのJSON形式でのエクスポートが可能。（根拠: Features）


### 利用例

- 自身のサーバーにDockerを用いて環境を構築し、外部のクラウドサービスに依存せずプライベートにワークアウトデータを管理したい。（README明記／根拠: Why openGym）

- FitNotesなどの他のフィットネスアプリからこれまでの履歴を移行し、openGym上で一元管理したい。（README明記／根拠: Features）

- スマートフォンの生体認証を使って手軽かつセキュアにログインし、複数のデバイス間で記録を同期させたい。（README明記／根拠: Features）


### 最初に試すこと

Docker Composeを使用してローカル環境でアプリケーションを起動し、プロファイルを作成する

1. git clone https://github.com/DuarteSantos8/openGym

2. cd openGym

3. cp .env.example .env

4. docker compose pull

5. docker compose up -d


成功の目安: ブラウザで http://localhost:8080 にアクセスし、Create profileをタップして利用を開始できること





## Zenn

- [ICFPC2026 参加記](https://zenn.dev/algoartis/articles/b5dd3c401d5dd4) — がんぽん

- [【Salesforce】Agent Script入門｜Agentforceの従業員エージェントを作ってみた](https://zenn.dev/actbe_tech/articles/57561ffebaf9ed) — 福西

- [xcrun xcodeproj で .xcodeproj をコマンドラインから編集する（Xcode 27.2）](https://zenn.dev/d_date/articles/xcrun-xcodeproj-xcode27-2) — Daiki Matsudate

- [国産モデル sarashina3-mini は日本語の推敲で何を変えるのか？](https://zenn.dev/algoartis/articles/03ca12150ccbee) — 大賀愛一郎（oga_aiichiro）

- [FFRI × NFLabs. Cybersecurity Challenge 2026 ゆるWriteup](https://zenn.dev/juck28/articles/74c43f18838188) — JUCK

- [AIを使えばドキュメント整備はいらない？いやいや、今こそ人間が動くときだ](https://zenn.dev/atamaplus/articles/2c9538a721c613) — yuki nomura

- [OpenTelemetryでStep Functions越しにtraceparentを引き回し、複数Lambdaを一つのトレースにつなぐ](https://zenn.dev/boy_techblog/articles/connecting-trace-serverless) — watariryo

- [jpstatで始めるe-Stat API入門](https://zenn.dev/tyasuakwa/articles/3f6a1394323275) — tya-guin

- [Akinatorで始めるAgentic RL ー タスク設計と初期検証  ー](https://zenn.dev/mkj/articles/8e1da67da67f98) — クリリン

- [レポ：mixi2のインターンに参加しました！](https://zenn.dev/riochin/articles/mixi2-intern-2026) — Riochin

- [改めて考える、AIエンジニアリングの今](https://zenn.dev/r_kaga/articles/2fd185c50cea7c) — r.kagaya

- [【セキュリティ】お客さんからの「うちは大丈夫？」に答えるため、IPAの点検項目をレガシーPHPのECサイトで上から順にやってみた](https://zenn.dev/subara3/articles/b90ff538d87aa6) — Subara3

- [Gemini 4 Argonの日本語性能を検証してみた](https://zenn.dev/algoartis/articles/19bb1705ea4b16) — 大賀愛一郎（oga_aiichiro）

- [【備忘録】CSSのstickyで作る、せり上がりながら背景が見える演出](https://zenn.dev/crayfisher_zari/articles/75619d5860f885) — にしはら

- [開発しながら同じPCでローカルLLMを動かしてみた話](https://zenn.dev/sumasate_tec/articles/test-local-llm) — スマサテ株式会社

- [『現場で役立つシステム設計の原則』を読んで学んだこと、実践したこと、これからやりたいこと](https://zenn.dev/wwwave/articles/38b8284f96bd9e) — 塚本

- [話題の逆解析 MCP「REA」を Claude Code に隔離してつないだ——静的解析の A/B 試験と安全設計](https://zenn.dev/keigoly/articles/8738d8d241b5a1) — keigoly

- [良いテストを書き、良いテストを見分ける ─『単体テストの考え方/使い方』のエッセンス](https://zenn.dev/nexta_/articles/unit-testing-principles-essence) — tetsu.k

- [SQLite 本体にベクトル検索拡張 vec1 がやってきた](https://zenn.dev/mattn/articles/6e9996319ac099) — mattn

- [WAF でブロックする前に確かめていること](https://zenn.dev/azunyan/articles/7a105969d7d16c) — えみり〜


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。