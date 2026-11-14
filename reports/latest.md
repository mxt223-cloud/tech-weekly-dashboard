# Tech Daily — 2026-11-14

生成日時: 2026-11-14T10:38:14.269364+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)

**概要:** sherlock-project/sherlockは、ユーザー名を手がかりに400以上のソーシャルネットワークからソーシャルメディアアカウントを検索・特定するためのPythonツールです。

- 言語: Python
- 今週のスター: 13364
- ライセンス: MIT
- AI分析状態: ok

### できること

- 400以上のソーシャルネットワークを対象としたユーザー名検索（根拠: README冒頭）

- 単一または複数のユーザー名を同時に指定した検索（根拠: General usage）

- 検索結果のテキストファイルやCSV、XLSXなどでの保存（根拠: General usage）


### 利用例

- 特定のユーザー名が使われているソーシャルメディアアカウントの調査（README明記／根拠: README冒頭）


### 最初に試すこと

コマンドを使用して単一のユーザー名を検索する

1. sherlock user123


成功の目安: 見つかったアカウント情報がターミナルに表示され、ユーザー名に応じたテキストファイルに保存されること

未確認: 詳細な設定ファイルの詳細な挙動／公式パッケージ以外のサポート範囲の詳細


## 2. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 6169
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


## 3. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

**概要:** OpenMausBotは、チャットアプリの形式で複数のAIボットを管理できるオープンソースのGrok Bot代替ツールです。ローカル環境でClaude、Codex、GrokなどのAIエージェントを実行し、それぞれに独自のパーソナリティや仮想コンピュータを持たせてやり取りすることができます。

- 言語: TypeScript
- 今週のスター: 7763
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


## 4. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

**概要:** agent-browserは、AIエージェント向けのネイティブRust製ブラウザ自動化CLIツールです。シェルコマンドから1つずつブラウザを操作でき、ページをアクセシビリティツリーのコンパクトなテキストとしてスナップショット取得して要素の参照（ref）を返し、それに対してクリックなどの操作を行えます。

- 言語: Rust
- 今週のスター: 4360
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


## 5. [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)

**概要:** elephant-goldfish-model（EGM）は、AIアシスタント向けのオープンソースプラグインです。プロジェクトの文脈を保持する「Elephant」と、新鮮な視点でレビューを行う「Goldfish」の役割を組み合わせ、ソフトウェア仕様の設計やレビュー、コードとの乖離チェックを行います。

- 言語: Python
- 今週のスター: 5560
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- プロジェクトの文脈や要件を整理し、コンセプトブリーフの作成や仕様書のドラフト作成を行う。（根拠: Choose a skill）

- 既存の会話コンテキストを含めずに参照資料やドキュメントを検証し、前提の抜けや見落としを検出するレビューを行う。（根拠: How it works）

- チェックインされているドキュメントと現在のソースコードを比較し、乖離を報告する。（根拠: Choose a skill）


### 利用例

- 新しい機能のアイデアについて要件やトレードオフを検討し、合致した方向性を保存する。（README明記／根拠: Try your first design）

- 既存の設計図やREADME、PRプランを実際のコードに対してレビューする。（README明記／根拠: Try a 60-second review on existing code）

- 既存のコードベースに対するドキュメントを作成または更新する。（README明記／根拠: Choose a skill）


### 最初に試すこと

プロジェクトを開き、機能のアイデアに対するブレインストーミングや設計ドラフト作成の流れを確認する。

1. /egm-brainstorm Add webhook delivery to this project.

2. /egm-draft

3. /egm-review design_draft.md


成功の目安: エージェントとの対話を通じてコンセプトブリーフや設計ドラフトが生成され、レビューを実施できること。

未確認: サブエージェントを作成できない環境での動作制限の詳細について、外部ドキュメント以外の具体的な挙動


## 6. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

**概要:** ZhuLinsen/daily_stock_analysisは、LLMを活用して複数の市場における株式の自動分析と通知を行うインテリジェントな分析システムです。

- 言語: Python
- 今週のスター: 3778
- ライセンス: MIT
- AI分析状態: ok

### できること

- 核心結論、スコア、トレンド、売買ポイント、リスク警告などを含むAI決定レポートの生成（根拠: 功能特性）

- A株、香港株、米国株、日本株、韓国株、台湾株、ETFの多市場データ集約（根拠: 功能特性）

- GitHub Actions、Docker、ローカルの定期実行、FastAPIサービス、各種チャットツールやメールへの通知（根拠: 功能特性）


### 利用例

- 毎日の株式分析結果を決定ダッシュボード形式で企業微信、飛書、Telegram、Discord、Slack、メールへ自動送信する（README明記／根拠: README冒頭）

- WebやAPIを利用して、移動平均線やボリンジャーバンドなどの15種類の内蔵戦略に基づくマルチターン形式のAI戦略質問を行う（README明記／根拠: 功能特性）

- 画像やCSV、Excelなどのデータをスマートに取り込み、株式コードや名称の補完を行う（README明記／根拠: 功能特性）


### 最初に試すこと

リポジトリをクローンして依存関係をインストールし、手動で解析を実行する

1. git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

2. pip install -r requirements.txt

3. cp .env.example .env && vim .env

4. python main.py


成功の目安: 解析スクリプトがエラーなく実行されること




## 7. [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)

**概要:** Auto Ontologyは、企業データのメタデータからセマンティックな知識グラフやオントロジーを構築し、AIエージェントの決定論的なクエリ生成やコンテキスト取得を支援するPythonフレームワークです。

- 言語: Python
- 今週のスター: 4108
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


## 8. [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

**概要:** MuJoCoは、ロボット工学、バイオメカニクス、機械学習などの分野で高速かつ正確な物理シミュレーションを行うための汎用物理エンジンです。

- 言語: C++
- 今週のスター: 1764
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

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


## 9. [mattpocock/skills](https://github.com/mattpocock/skills)

**概要:** mattpocock/skillsは、Claude Code、Codex、GitHub CopilotなどのAIコーディングエージェント向けに設計された、小型で拡張可能なエージェントスキルのコレクションです。要件定義の精緻化、共有言語の構築、テスト駆動開発（TDD）、コードベースのアーキテクチャ改善など、実際のソフトウェアエンジニアリングを支援する様々なスキルを提供します。

- 言語: Shell
- 今週のスター: 7599
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


## 10. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

**概要:** addyosmani/agent-skillsは、AIコーディングエージェントに本番品質のエンジニアリングスキルやワークフローを適用するための、25個のスキルとスラッシュコマンドを提供するリポジトリです。

- 言語: JavaScript
- 今週のスター: 3502
- ライセンス: MIT
- AI分析状態: ok

### できること

- 開発ライフサイクルに沿った9個のスラッシュコマンド（/spec, /plan, /build, /test, /constraints, /review, /webperf, /code-simplify, /shipなど）を提供します。（根拠: Commands）

- 合計25個のスキル（24個のライフサイクルスキルと1個のメタスキル）を収めており、構造化されたステップや検証ゲートをエージェントに実行させます。（根拠: All 25 Skills）

- オープンなskills CLIを使用して、70以上のエージェントに一括または個別のスキルをインストールできます。（根拠: Quick Start）


### 利用例

- 開発の初期段階で、エージェントに要件定義やPRDの作成を行わせる。（README明記／根拠: Commands）

- マージ前のコードレビューで、品質ゲートに基づいたコード改善を行う。（README明記／根拠: Commands）

- ウェブパフォーマンスの最適化や測定を行う。（README明記／根拠: Commands）


### 最初に試すこと

skills CLIを使用してリポジトリの全スキルをインストールする

1. npx skills add addyosmani/agent-skills


成功の目安: 全25個のスキルがエージェント環境にインストールされること





## Zenn

- [ng: Neovim のためのシンプルな GUI](https://zenn.dev/shougo/articles/ng-nvim-simple-gui) — Shougo

- [困ったらAIにすぐ聞く3年目エンジニアが社会人になって読んだ技術書 10冊.](https://zenn.dev/atrae/articles/032b9fccca0ff7) — shin

- [5年後のエンジニアは、何に責任を持つのだろうか](https://zenn.dev/ara_ta3/articles/thinking-about-engineers-five-years-from-now) — ara_ta3

- [【pstack】AIに敵対的レビューをさせるな。トークンは検証に使え](https://zenn.dev/karamage/articles/5c3f8370b2b370) — karamage

- [仕組み編：Two-Towerによる検索システム（学習・推論・配信）](https://zenn.dev/ca_kagglers/articles/two-tower-mechanism) — ihiratch

- [最強オープンウェイトモデル Kimi-K3.1-Pro をセルフホストして独自ベンチで比べてみた](https://zenn.dev/fixstars/articles/kimi-k31-pro-benchmark) — iizuka kota

- [AIで膨らみ続けるテストケースを、リスクベースドテストで選んで回すまでの記録](https://zenn.dev/pivotmedia/articles/risk-based-testing-for-uat) — Keisuke

- [セキュリティ・キャンプ 2026 応募課題晒し](https://zenn.dev/uvu/articles/758ee227a614ea) — ?Sw()m%kLc$VfD!!

- [AWS EmulatorはAWS Blocksのモックを置き換えるのか？実際に動かして見えた「三つ目の層」](https://zenn.dev/genda_jp/articles/18d1f780f6b41f) — ikenyal

- [AIエージェントが決定を勝手に変えてしまった5つのパターンと工夫](https://zenn.dev/dress_code/articles/568fd547315abe) — いっしー

- [Node.js 22 / 24 / 26 の脆弱性、自分のアプリが影響を受けるか確認する方法【2026年11月】](https://zenn.dev/rakko_inc/articles/nodejs-security-nov-2026-proxy) — maya honey

- [Software Factoryの先へ：全社の仕事をAI-NativeにするUbieの内製クラウドエージェント基盤](https://zenn.dev/ubie_dev/articles/45501469c9c044) — Yuku Kotani

- [Claude Code に忘れさせたら、トークン使用量が4割減った](https://zenn.dev/sae_eng/articles/0e9ed7205ebc41) — Sae_Eng

- [ISUCON2026 で優勝しました（準備編）](https://zenn.dev/luvtechno/articles/isucon2026-preparation) — Yoshinori Kawasaki

- [Snowflake Dashboards 2.0が最高な理由と、これからBIに求められること](https://zenn.dev/dataheroes/articles/snowflake-dashboards-2-and-future-of-bi) — ぺい(pei0804)

- [Rustで作られたExpoの新フレームワーク「Exact」で、モバイル・Web・デスクトップアプリを作ってみた](https://zenn.dev/tellernovel_inc/articles/expo-exact-first-impression) — kazutoyo@TellerNovel

- [退屈なCoding AgentはMuseにやらせよう](https://zenn.dev/watany/articles/342b9815dd0553) — watany

- [Claude Codeで最近使っているTips【2026/11】](https://zenn.dev/oikon/articles/claude-code-recipe) — Oikon

- [脆弱性問題を解決するためにRustに移行するべきなのか？](https://zenn.dev/garasubo/articles/72340052cdd871) — ガラスボー

- [なぜ mixi2 は iPhone Duo の発売初日から最適化できたのか？](https://zenn.dev/mixi/articles/b0ea64fded9503) — kuno


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。