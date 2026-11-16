# Tech Daily — 2026-11-16

生成日時: 2026-11-16T10:19:41.545903+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [meta/astryx](https://github.com/meta/astryx)

**概要:** Astryxは、Metaで社内開発されオープンソース化された、カスタマイズ可能でAIエージェントの利用にも対応したオープンソースのデザインシステムです。150以上のアクセシブルなコンポーネント、テーマ機能、ダークモード、テンプレート、CLIを提供します。

- 言語: TypeScript
- 今週のスター: 13501
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 150以上のアクセシブルなReactコンポーネントと完全なTypeScriptサポートを提供します。（根拠: Overview）

- ブランドレベルのテーマ機能、ダークモード、すぐに使えるテンプレートを備えています。（根拠: Overview）

- コンポーネントのソースコードをプロジェクトに取り込んで直接編集できる「swizzle」機能を持ちます。（根拠: Overview）


### 利用例

- 人手とAIアシスタントの両方で同じツールやAPIを用いてUIを構築する。（README明記／根拠: Overview）

- Tailwind CSSやCSSモジュール、通常のCSSなど既存のプロジェクトのスタイリング方法で上書きして利用する。（README明記／根拠: Overview）

- CLIツールを活用したコンポーネントのドキュメント参照やテンプレート、スキャホーディング、テーマ管理を行う。（README明記／根拠: Packages）


### 最初に試すこと

npmを使用して、Astryxのコアパッケージ、中立テーマ、依存関係、およびCLIをインストールする。

1. npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex

2. npm install -D @astryxdesign/cli


成功の目安: エラーなくパッケージのインストールが完了し、プロジェクトの依存関係に追加されること。

未確認: 具体的なNext.jsやVite、Tailwindなどの詳細な統合手順（パッケージ内の外部ドキュメントを参照する必要があるため）


## 2. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 6077
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


## 3. [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)

**概要:** sherlock-project/sherlockは、ユーザー名を手がかりに400以上のソーシャルネットワークからソーシャルメディアアカウントを検索・特定するためのPythonツールです。

- 言語: Python
- 今週のスター: 10412
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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


## 4. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

**概要:** plannotatorは、AIコーディングエージェントの作業を確認、レビュー、アノテーションするためのローカルなブラウザベースのレビューツールです。

- 言語: TypeScript
- 今週のスター: 1719
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- プラン、仕様、Markdown、HTMLなどのアーティファクトに注釈を付け、エージェントにフィードバックを送信できます。（根拠: README冒頭）

- ローカルの変更やリモートのプルリクエストのコードレビューを行い、差分へのコメントやコードの提案が可能です。（根拠: README冒頭）

- エージェントがプランを提示した際にブラウザでレビュー画面を自動的に開くことができます。（根拠: Plan mode）


### 利用例

- AIコーディングエージェントが作成したプランや提案を確認し、ブラウザ上で直接フィードバックを書き込んでエージェントに戻す。（README明記／根拠: Plannotator）

- GitやGitHub等の差分に対してコメントを残し、コードレビューを効率化する。（README明記／根拠: Code Review）

- ターミナル内でエージェントの返信やMarkdownドキュメントのレビューを行う。（README明記／根拠: Herdr Annotate: Plannotator in the Terminal）


### 最初に試すこと

plannotatorのインストールと動作確認を行う

1. curl -fsSL https://plannotator.ai/install.sh | bash を実行してインストールする

2. /plannotator-last を実行してエージェントの最後の返信に注釈を付ける


成功の目安: plannotatorが正常にインストールされ、ブラウザまたはコマンド上でレビュー画面が起動すること




## 5. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

**概要:** agent-browserは、AIエージェント向けのネイティブRust製ブラウザ自動化CLIツールです。シェルコマンドから1つずつブラウザを操作でき、ページをアクセシビリティツリーのコンパクトなテキストとしてスナップショット取得して要素の参照（ref）を返し、それに対してクリックなどの操作を行えます。

- 言語: Rust
- 今週のスター: 4217
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


## 6. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

**概要:** ZhuLinsen/daily_stock_analysisは、AI大模型を活用して複数の市場（A股、港股、美股、日股、韩股、台股等）の株式を自動分析し、企業微信やTelegramなどの通知ツールへ「决策仪表盘」をプッシュ通知するスマート分析システムです。

- 言語: Python
- 今週のスター: 4548
- ライセンス: MIT
- AI分析状態: ok

### できること

- AIによる核心結論、スコア、トレンド、売買ポイント、リスク警報を含む意思決定レポートの生成（根拠: 功能特性）

- 複数市場のデータ（株価、Kライン、テクニカル指標、ニュース、公告、ファンダメンタルズなど）の集約（根拠: 功能特性）

- GitHub Actions、Docker、ローカルの定期実行による自動化と各種チャット・メールへの通知（根拠: 功能特性）


### 利用例

- 毎日の株式市場の分析結果と意思決定ダッシュボードをチャットツールやメールに自動で受け取る（README明記／根拠: 功能特性）

- WebインターフェースやAPIを使い、AIエージェントの戦略に基づいた銘柄の対話型質問や分析を行う（README明記／根拠: 功能特性）


### 最初に試すこと

ローカル環境でプロジェクトをクローンして依存関係をインストールし、分析を実行する

1. git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

2. pip install -r requirements.txt

3. cp .env.example .env && vim .env

4. python main.py


成功の目安: main.pyがエラーなく実行され、株式の分析処理が完了すること




## 7. [we-promise/sure](https://github.com/we-promise/sure)

**概要:** we-promise/sure は、開発が終了した Maybe Finance プロジェクトのコミュニティ主導によるフォーク版であり、すべての人のための個人財務・資産管理アプリケーションです。Dockerによるセルフホストやブラウザ、デスクトップアプリ、モバイルアプリなどからのアクセスをサポートしています。

- 言語: Ruby
- 今週のスター: 4556
- ライセンス: AGPL-3.0
- AI分析状態: ok

### できること

- Dockerを使用して個人財務アプリをセルフホストできる（根拠: Hosting Sure）

- ブラウザ、macOSデスクトップアプリ、モバイルアプリ、APIクライアント、LLMエージェントからアクセス可能（根拠: Hosting Sure）

- 開発環境向けにデモデータをロードする機能を持つ（根拠: Local Development Setup）


### 利用例

- 個人や家族の資産管理・財務状況の把握のためにアプリを自前でホストして利用する（README明記／根拠: Hosting Sure）

- 開発者がローカル環境でアプリのソースコードを実行し、貢献やカスタマイズを行う（README明記／根拠: Local Development Setup）


### 最初に試すこと

ローカル環境でアプリケーションを起動し、動作を確認する

1. cd sure

2. cp .env.local.example .env.local

3. bin/setup

4. bin/dev

5. rake demo_data:default


成功の目安: http://localhost:3000 にアクセスしてアプリケーションが閲覧でき、デモデータの資格情報でログインできること

未確認: Maybe Financeからのフォーク以降に追加された具体的な新機能の全容／LLMエージェントやモバイルアプリとの連携の詳細な設定手順


## 8. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

**概要:** OpenMausBotは、チャットアプリの形式でAIボットを管理できるオープンソースのGrok Bot代替アプリケーションです。ローカルで動作するClaudeやCodexなどのAIエージェントを連絡先のように操作し、それぞれにパーソナリティや専用のクラウドコンピュータを持たせることができます。

- 言語: TypeScript
- 今週のスター: 5463
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- ClaudeやCodexなどのAIエージェントCLIをローカル環境で実行し、既存のログイン情報やサブスクリプションをそのまま利用できる（根拠: Why）

- macOS、Windows、Ubuntu 24.04向けのデスクトップアプリとしてビルドおよび実行が可能である（根拠: Quick start）

- Tailscaleを介して、別のコンピュータ上のボットを開いて操作することができる（根拠: Quick start）


### 利用例

- 複数のAIボットとチャットアプリ感覚で会話を行い、作業を進めさせる（README明記／根拠: README冒頭）

- ローカルにインストールされたAIエージェントを利用して開発やタスクを実行する（README明記／根拠: Why）


### 最初に試すこと

ソースコードから開発サーバーおよびElectronシェルを起動する

1. git clone https://github.com/milind-soni/OpenMausBot && cd OpenMausBot

2. pnpm install

3. pnpm dev:server

4. pnpm dev

5. pnpm dev:desktop


成功の目安: Electronシェルが起動し、デスクトップアプリとして操作できるようになること

未確認: 具体的なボットの内部実装や詳細なカスタマイズ方法／対応しているすべての機能やコマンドの詳細なオプション


## 9. [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)

**概要:** elephant-goldfish-model（EGM）は、AIアシスタント向けのオープンソースプラグインです。プロジェクトの文脈を保持する「Elephant」と、新鮮な視点でレビューを行う「Goldfish」の役割を組み合わせ、ソフトウェア仕様の設計やレビュー、コードとの乖離チェックを行います。

- 言語: Python
- 今週のスター: 5060
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

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


## 10. [google-deepmind/mujoco](https://github.com/google-deepmind/mujoco)

**概要:** MuJoCoは、ロボット工学、バイオメカニクス、機械学習などの分野で高速かつ正確な物理シミュレーションを行うための汎用物理エンジンです。

- 言語: C++
- 今週のスター: 1922
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



## Zenn

- [Lightdashで作れるグラフを試してみた【dbt v2】](https://zenn.dev/ryatora/articles/lightdash-chart-catalog) — rnm

- [FTDで実装するTLS Decryption](https://zenn.dev/5x4x7/articles/92a962f3cd6cb6) — 5x4x7

- [Canton Networkとは何か――金融機関が「見せる相手を選べる」ブロックチェーンに集まる理由](https://zenn.dev/komlock_lab/articles/canton-network-evm-comparison-2026) — Kobara Toi

- [.NET 11 の ASP.NET Core Blazor の新機能のスケールイン対応機能！](https://zenn.dev/microsoft/articles/aspnetcore-blazor-dotnet11-scale) — Kazuki Ota

- [フロントエンドのフレームワークを、安全に段階的に入れ替える](https://zenn.dev/yasuakiomokawa/articles/de83bb4c4ea928) — Yasuaki Omokawa

- [【2026/11/13時点】Claude Duet を Team プランで触ってみた（組織で使うときの注意点つき）](https://zenn.dev/canly/articles/e2bd67c9a4c18b) — ふくだ（fukuda ryu）

- [Qwen3.8 Flash Nextに混ざる中国語を、出力層の書き換えで消した: 27%→0%、他の重みは1バイトも変えずに](https://zenn.dev/caphtech/articles/qwen38-zh-ban) — rizumita

- [ng: Neovim のためのシンプルな GUI](https://zenn.dev/shougo/articles/ng-nvim-simple-gui) — Shougo

- [5年後のエンジニアは、何に責任を持つのだろうか](https://zenn.dev/ara_ta3/articles/thinking-about-engineers-five-years-from-now) — ara_ta3

- [【pstack】AIに敵対的レビューをさせるな。トークンは検証に使え](https://zenn.dev/karamage/articles/5c3f8370b2b370) — karamage

- [仕組み編：Two-Towerによる検索システム（学習・推論・配信）](https://zenn.dev/ca_kagglers/articles/two-tower-mechanism) — ihiratch

- [PostgreSQLのバージョンアップ後に ANALYZE VERBOSE を実行する理由](https://zenn.dev/fusic/articles/e05247d244838e) — きたのかい

- [脱WordPress：10年超の個人ブログをAstro + Cloudflare Workersへ移行しPageSpeed 100点を実現](https://zenn.dev/unsoluble_sugar/articles/8cdf1efc01e6cb) — 星影

- [AIで膨らみ続けるテストケースを、リスクベースドテストで選んで回すまでの記録](https://zenn.dev/pivotmedia/articles/risk-based-testing-for-uat) — Keisuke

- [Skills を持つ単一エージェントは、サブエージェント構成より品質で上回ることが多い — Anthropic が示す移行の手順](https://zenn.dev/happy_elements/articles/201519107f93de) — ko.+

- [Software Factoryの先へ：全社の仕事をAI-NativeにするUbieの内製クラウドエージェント基盤](https://zenn.dev/ubie_dev/articles/45501469c9c044) — Yuku Kotani

- [SlackでMarkdown記法が使えるようになっていた](https://zenn.dev/lnest_knowledge/articles/ed5977bd7b6c1f) — shown_it

- [ISUCON2026 で優勝しました（準備編）](https://zenn.dev/luvtechno/articles/isucon2026-preparation) — Yoshinori Kawasaki

- [退屈なCoding AgentはMuseにやらせよう](https://zenn.dev/watany/articles/342b9815dd0553) — watany

- [Claude Codeで最近使っているTips【2026/11】](https://zenn.dev/oikon/articles/claude-code-recipe) — Oikon


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。