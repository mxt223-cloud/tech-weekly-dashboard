# Tech Daily — 2026-11-13

生成日時: 2026-11-13T11:02:24.025631+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 6055
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


## 2. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

**概要:** OpenMausBotは、チャットアプリの形式で複数のAIボットを管理できるオープンソースのGrok Bot代替ツールです。ローカル環境でClaude、Codex、GrokなどのAIエージェントを実行し、それぞれに独自のパーソナリティや仮想コンピュータを持たせてやり取りすることができます。

- 言語: TypeScript
- 今週のスター: 9104
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- Claude、Codex、GrokのCLIをローカル環境で実行し、独自のログイン情報やサブスクリプションを利用可能（根拠: Why）

- macOS、Windows、Ubuntu 24.04に対応したデスクトップビルドおよびパッケージング機能の提供（根拠: Quick start）

- ハーネスサーバーが組み込まれており、リリース版では個別のサーバー設定が不要（根拠: Quick start）


### 利用例

- サイドバーに配置された複数のAIボットとチャットアプリのように会話を行い、作業を監視して承認する（README明記／根拠: README冒頭）

- ローカルにインストールされたAIエージェントを利用して独自のパーソナリティやクラウドコンピュータを持つボットを動かす（README明記／根拠: Why）

- Tailscaleを介して別のWindows、macOS、Ubuntuホストのクライアントとしてデスクトップ同士をペアリングする（README明記／根拠: Quick start）


### 最初に試すこと

ソースコードから開発サーバーおよびデスクトップシェルを起動して動作を確認する

1. git clone https://github.com/milind-soni/OpenMausBot && cd OpenMausBot

2. pnpm install

3. pnpm dev:server

4. pnpm dev

5. pnpm dev:desktop


成功の目安: ハーネスサーバーおよびElectronシェルが起動し、アプリケーションが正常に動作すること

未確認: Featuresセクションの具体的な詳細内容（READMEの途中で文章が途切れているため）


## 3. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

**概要:** agent-browserは、AIエージェント向けのネイティブRust製ブラウザ自動化CLIツールです。シェルコマンドから1つずつブラウザを操作でき、ページをアクセシビリティツリーのコンパクトなテキストとしてスナップショット取得して要素の参照（ref）を返し、それに対してクリックなどの操作を行えます。

- 言語: Rust
- 今週のスター: 4601
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- ページをコンパクトなテキスト（アクセシビリティツリー）としてスナップショット取得し、各要素にrefを割り当てる機能（根拠: README冒頭）

- クリック、入力、スクロール、待機、スクリーンショット撮影などの豊富なブラウザ操作コマンドの提供（根拠: Commands）

- エージェント向けのスキル取得機能やMCPサーバーとしての起動機能（根拠: For AI agents）


### 利用例

- シェルからAIエージェントにWebページを開かせ、要素を指定してクリックや入力を行わせるブラウザ自動化（README明記／根拠: Quick start）

- AIエージェントにスキルやMCPサーバー機能を組み込んで、インタラクティブなWeb操作ワークフローを実行させる（README明記／根拠: For AI agents）


### 最初に試すこと

ブラウザを開いてページのインタラクティブな要素のスナップショットを取得し、要素をクリックして結果を確認する

1. agent-browser open example.com

2. agent-browser snapshot -i

3. agent-browser click @e1

4. agent-browser get url

5. agent-browser close


成功の目安: コマンドが正常に実行され、指定したURLのページ操作結果が取得できること

未確認: 詳細な設定ファイルや環境変数によるカスタマイズの全容／LightpandaやObscuraなど特定エンジン・プロバイダの具体的な設定・接続手順


## 4. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)

**概要:** Auto Ontologyは、企業データのメタデータからセマンティックな知識グラフやオントロジーを構築し、AIエージェントの決定論的なクエリ生成やコンテキスト取得を支援するPythonフレームワークです。

- 言語: Python
- 今週のスター: 5802
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- メタデータから企業向けオントロジーを生成し、知識グラフを構築する（根拠: README冒頭）

- 自然言語の質問をSQLに翻訳し、接続されたデータベースに対して実行する（根拠: Key Features）

- MCP、CLI、APIを通じて任意のAIエージェントにコンテキストを提供する（根拠: README冒頭）


### 利用例

- リレーショナルソース上のセマンティックカタログ層として利用し、データの意味や関係性をエージェントに与える（README明記／根拠: Key Features）

- Web UIのチャット、分析、データカタログ機能を通じてデータ分析や設定を行う（README明記／根拠: Key Features）

- MCPサーバーを用いて任意のMCPクライアントからオントロジーに対する読み取り専用ツールにアクセスする（README明記／根拠: Use it from your agent）


### 最初に試すこと

Docker Composeを使用してAuto-Ontologyをローカル環境で起動し、サンプルデータベースに対する質問応答を確認する

1. git clone https://github.com/NVIDIA/auto-ontology.git && cd auto-ontology

2. cp .env.example .env

3. docker compose up -d --wait postgres

4. git clone https://github.com/NVIDIA/auto-ontology-eval.git ../auto-ontology-eval

5. docker compose up -d --build


成功の目安: ブラウザで http://localhost:3000 を開き、ログイン後にセマンティックコンパイルが完了し、チャットで質問に対してSQLと回答が返ってくること

未確認: 外部からのプルリクエストの受け入れ可否（現在のREADMEでは非受付と記載されているが将来の変更可能性は不明）／KumoRFM以外の予測サービスの具体的な統合方法


## 5. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

**概要:** cloudflare/security-audit-skillは、コーディングエージェントをセキュリティ監査人に変えるスキルリポジトリです。偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成という6つのフェーズで構造化されたセキュリティ監査を実行します。

- 言語: JavaScript
- 今週のスター: 10700
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




## 6. [vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)

**概要:** agent-desktopは、AIエージェントがmacOS、Windows、LinuxのデスクトップアプリをOSのアクセシビリティツリー経由で操作するためのコンピュータ用CLIおよびCライブラリです。

- 言語: Rust
- 今週のスター: 6414
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- OSのアクセシビリティツリーを読み取り、操作可能な要素に参照（ref）を付与してJSON形式で返却する。（根拠: README冒頭）

- クリックや文字入力などのUI操作を、スクリーンショットやピクセルマッチングなしで実行できる。（根拠: README冒頭）

- すべてのコマンドをstdio経由のMCPツールとして提供する機能を持つ。（根拠: MCP）


### 利用例

- AIエージェントがデスクトップアプリのUI要素のツリー構造を把握し、指定した要素に対して操作と結果の検証を繰り返す。（README明記／根拠: README冒頭）

- MCPサーバーを介してAIエージェントの外部ツールとして統合し、デスクトップ操作を行わせる。（README明記／根拠: MCP）


### 最初に試すこと

Finderアプリのインタラクティブ要素のスナップショットを取得し、要素に対する操作と確認を行う

1. agent-desktop snapshot --app Finder -i

2. agent-desktop click @s8f3k2p9:e8

3. agent-desktop snapshot --app Finder -i


成功の目安: スナップショットおよびクリック操作の結果がJSON形式で正常に出力されること

未確認: リポジトリのドキュメントに詳細な仕様が記載されていない一部の設定や高度なAPIの使い方


## 7. [mattpocock/skills](https://github.com/mattpocock/skills)

**概要:** mattpocock/skillsは、Claude Code、Codex、GitHub CopilotなどのAIコーディングエージェント向けに設計された、小型で拡張可能なエージェントスキルのコレクションです。要件定義の精緻化、共有言語の構築、テスト駆動開発（TDD）、コードベースのアーキテクチャ改善など、実際のソフトウェアエンジニアリングを支援する様々なスキルを提供します。

- 言語: Shell
- 今週のスター: 8731
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


## 8. [zed-industries/zed](https://github.com/zed-industries/zed)

**概要:** Zedは、AtomとTree-sitterの開発者によって作られた、高性能かつマルチプレイヤー対応のコードエディタです。

- 言語: Rust
- 今週のスター: 2339
- ライセンス: NOASSERTION
- AI分析状態: ok（キャッシュ）

### できること

- macOS、Linux、Windows向けにダウンロードまたはパッケージマネージャー経由でインストールできる。（根拠: Installation）


### 利用例

- 複数人での共同作業やコーディングを行う。（README明記／根拠: README冒頭）


### 最初に試すこと

公式サイトからZedをダウンロードまたはインストールして利用を開始する

1. 公式サイトのダウンロードページにアクセスする

2. macOS、Linux、Windowsのいずれかの方法でインストールを行う


成功の目安: Zedエディタが起動すること

未確認: 具体的なマルチプレイヤー機能の詳細な操作方法／サポートされている全てのパッケージマネージャーのリスト


## 9. [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

**概要:** MuJoCoは、ロボット工学、バイオメカニクス、機械学習などの分野で高速かつ正確な物理シミュレーションを行うための汎用物理エンジンです。

- 言語: C++
- 今週のスター: 1671
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- C言語のAPIを持ち、低レベルデータ構造を用いたパフォーマンス重視の実行時シミュレーションモジュールを提供します。（根拠: README冒頭）

- ネイティブデスクトップウィンドウやウェブブラウザでのインタラクティブな可視化機能が含まれています。（根拠: README冒頭）

- PythonバインディングおよびUnityゲームエンジン向けのプラグインが提供されています。（根拠: README冒頭）


### 利用例

- ロボット工学や機械学習の研究開発において、環境と相互作用する関節構造の高速な物理シミュレーションに利用する。（README明記／根拠: README冒頭）

- ブラウザ上でWebAssembly版のMuJoCo Studioを使用し、モデルの閲覧やドラッグ＆ドロップによる確認を行う。（README明記／根拠: Getting Started）

- Pythonのチュートリアルノートブックを使用して、強化学習のポリシー訓練やLQRコントローラーの合成を行う。（README明記／根拠: Getting Started）


### 最初に試すこと

Python環境でMuJoCoのパッケージをインストールし動作確認を行う

1. pip install mujoco


成功の目安: エラーなくパッケージがインストールされ、Pythonからインポート可能になること

未確認: ソースコードからのビルド手順の詳細については、外部ドキュメントを参照する必要がある。


## 10. [google/skills](https://github.com/google/skills)

**概要:** google/skillsは、Googleの製品やテクノロジー（Google Cloudなど）に関するAgent Skillsを収集・提供するリポジトリです。npxなどのコマンドを使用して、エージェント用のスキルやプラグインを追加・更新できます。

- 言語: Python
- 今週のスター: 1933
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- Google Cloudなどの製品やテクノロジーに関する多数のAgent Skillsの提供（根拠: Available Skills）

- npx skills addコマンドによるスキルの追加機能（根拠: Installation）

- npx skills updateコマンドによるインストール済みスキルの更新と不要スキルの削除オプション（根拠: Updating Skills）


### 利用例

- Google Cloudの認証や基盤構築、AI/ML、インフラ管理などのタスクをAIエージェントに実行させる（README明記／根拠: Available Skills）

- Claude CodeやCodexなどのエージェントハーネスにGoogle製品のプラグインを追加して利用する（README明記／根拠: Plugins）

- インストール済みのスキルを最新バージョンに一括でアップデートする（README明記／根拠: Updating Skills）


### 最初に試すこと

スキルをエージェントに追加する

1. npx skills add google/skills を実行する

2. プロンプトが表示されたら、特定のスキルまたは全スキル、ターゲットのエージェント、インストール範囲を選択する


成功の目安: 選択したスキルやエージェントの設定が正常に完了すること

未確認: 各スキルが内部でどのような処理を行っているかに関する詳細な動作仕様



## Zenn

- [【備忘録】Transformerを数式レベルからnumpyのみで実装して理解する（②Backward Propagation編）](https://zenn.dev/matsu8/articles/a01ba3fc713e03) — やくも

- [Tauri の MSI インストーラーが更新のたびに削除済みデスクトップショートカットを復活させる問題を直した話](https://zenn.dev/takahiro_nago/articles/article-tauri-msi-desktop-shortcut) — TakahiroNago

- [セキュリティ・キャンプ 2026 応募課題晒し](https://zenn.dev/uvu/articles/758ee227a614ea) — ?Sw()m%kLc$VfD!!

- [AWS EmulatorはAWS Blocksのモックを置き換えるのか？実際に動かして見えた「三つ目の層」](https://zenn.dev/genda_jp/articles/18d1f780f6b41f) — ikenyal

- [週刊Cloudflare - 2026/11/08週](https://zenn.dev/gemcook/articles/weekly-cloudflare_2026_1101-1107) — あさひ

- [AIエージェントが決定を勝手に変えてしまった5つのパターンと工夫](https://zenn.dev/dress_code/articles/568fd547315abe) — いっしー

- [Node.js 22 / 24 / 26 の脆弱性、自分のアプリが影響を受けるか確認する方法【2026年11月】](https://zenn.dev/rakko_inc/articles/nodejs-security-nov-2026-proxy) — maya honey

- [libsignal のグループ暗号化を追って、署名改ざんのテストを追加した](https://zenn.dev/under_michi/articles/7791295efdb23e) — michi

- [Software Factoryの先へ：全社の仕事をAI-NativeにするUbieの内製クラウドエージェント基盤](https://zenn.dev/ubie_dev/articles/45501469c9c044) — Yuku Kotani

- [AI ファーストな管理画面を、WebMCP もどきで実現したい](https://zenn.dev/tokium_dev/articles/llm-admin-interface) — urugus

- [Claude Code に忘れさせたら、トークン使用量が4割減った](https://zenn.dev/sae_eng/articles/0e9ed7205ebc41) — Sae_Eng

- [Amazon Bedrock AgentCore Gatewayで、vLLMのQwenとAmazon Bedrockを使い分けてみた](https://zenn.dev/fusic/articles/4dc357178cbc1e) — xthixsl_ml@レオナ

- [ISUCON2026 で優勝しました（準備編）](https://zenn.dev/luvtechno/articles/isucon2026-preparation) — Yoshinori Kawasaki

- [AIに書かせた、が全然AIが書いてない件](https://zenn.dev/appleworld/articles/65aed6c725af71) — petanko

- [Snowflake Dashboards 2.0が最高な理由と、これからBIに求められること](https://zenn.dev/dataheroes/articles/snowflake-dashboards-2-and-future-of-bi) — ぺい(pei0804)

- [Rustで作られたExpoの新フレームワーク「Exact」で、モバイル・Web・デスクトップアプリを作ってみた](https://zenn.dev/tellernovel_inc/articles/expo-exact-first-impression) — kazutoyo@TellerNovel

- [退屈なCoding AgentはMuseにやらせよう](https://zenn.dev/watany/articles/342b9815dd0553) — watany

- [Claude Codeで最近使っているTips【2026/11】](https://zenn.dev/oikon/articles/claude-code-recipe) — Oikon

- [脆弱性問題を解決するためにRustに移行するべきなのか？](https://zenn.dev/garasubo/articles/72340052cdd871) — ガラスボー

- [なぜ mixi2 は iPhone Duo の発売初日から最適化できたのか？](https://zenn.dev/mixi/articles/b0ea64fded9503) — kuno


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。