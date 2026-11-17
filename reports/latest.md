# Tech Daily — 2026-11-17

生成日時: 2026-11-17T13:06:24.407848+09:00  
AI分析: 9/10件成功（gemini-3.5-flash-lite）


## 1. [GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

**概要:** モダンなWebプラットフォームの専門知識やベストプラクティスをコーディングエージェントに組み込むためのスキルとドキュメントを提供するソースリポジトリです。古いパターンを避け、最新のWebプラットフォームの機能を活用した解決策へと導きます。

- 言語: TypeScript
- 今週のスター: 6542
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- 対話型ウィザードを使用したモダンWebガイダンスのインストール機能（根拠: Quickstart）

- 関連するガイドの検索、IDによるガイドの取得、コードベースのレガシーパターンのスキャンを行うCLI機能（根拠: Quickstart）

- ユーザーエクスペリエンス、CSSレイアウト、パフォーマンスに関する最新のWebプラットフォーム機能やガイドの提供（根拠: What's Included?）


### 利用例

- コーディングエージェントが古いコードや冗長なJavaScriptを生成するのを防ぎ、最新のネイティブなWebプラットフォームソリューションを活用させる（README明記／根拠: Why?）

- プロジェクトのコードベースをスキャンしてレガシーパターンを検出し、モダン化するためのガイドを適用する（README明記／根拠: Quickstart）


### 最初に試すこと

インストールせずにCLIを使用して関連ガイドを検索する

1. npx modern-web-guidance@latest search "animate a dialog modal backdrop"


成功の目安: ダイアログモーダルの背景アニメーションに関連するガイドの検索結果が表示されること

未確認: 代替のインストール方法の詳細な手順


## 2. [meta/astryx](https://github.com/meta/astryx)

**概要:** Astryxは、Metaで社内開発されオープンソース化された、カスタマイズ可能でAIエージェントの利用にも対応したオープンソースのデザインシステムです。150以上のアクセシブルなコンポーネント、テーマ機能、ダークモード、テンプレート、CLIを提供します。

- 言語: TypeScript
- 今週のスター: 10939
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


## 3. [backnotprop/plannotator](https://github.com/backnotprop/plannotator)

**概要:** The workspace to stay in the loop and on top of agents - shape, decide, plan, annotate, review code, share with team, and send all feedback to agents with one click.

- 言語: TypeScript
- 今週のスター: 2325
- ライセンス: Apache-2.0
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



## 4. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 5666
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


## 5. [vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

**概要:** agent-browserは、AIエージェント向けのネイティブRust製ブラウザ自動化CLIツールです。シェルコマンドから1つずつブラウザを操作でき、ページをアクセシビリティツリーのコンパクトなテキストとしてスナップショット取得して要素の参照（ref）を返し、それに対してクリックなどの操作を行えます。

- 言語: Rust
- 今週のスター: 3760
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


## 6. [we-promise/sure](https://github.com/we-promise/sure)

**概要:** we-promise/sure は、開発が終了した Maybe Finance プロジェクトのコミュニティ主導によるフォーク版であり、すべての人のための個人財務・資産管理アプリケーションです。Dockerによるセルフホストやブラウザ、デスクトップアプリ、モバイルアプリなどからのアクセスをサポートしています。

- 言語: Ruby
- 今週のスター: 4679
- ライセンス: AGPL-3.0
- AI分析状態: ok（キャッシュ）

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


## 7. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

**概要:** ZhuLinsen/daily_stock_analysisは、AI大模型を活用して複数の市場（A股、港股、美股、日股、韩股、台股等）の株式を自動分析し、企業微信やTelegramなどの通知ツールへ「决策仪表盘」をプッシュ通知するスマート分析システムです。

- 言語: Python
- 今週のスター: 4355
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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




## 8. [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)

**概要:** sherlock-project/sherlockは、ユーザー名を手がかりに400以上のソーシャルネットワークからソーシャルメディアアカウントを検索・特定するためのPythonツールです。

- 言語: Python
- 今週のスター: 7067
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


## 9. [google/elephant-goldfish-model](https://github.com/google/elephant-goldfish-model)

**概要:** elephant-goldfish-model（EGM）は、AIアシスタント向けのオープンソースプラグインです。プロジェクトの文脈を保持する「Elephant」と、新鮮な視点でレビューを行う「Goldfish」の役割を組み合わせ、ソフトウェア仕様の設計やレビュー、コードとの乖離チェックを行います。

- 言語: Python
- 今週のスター: 4249
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
- 今週のスター: 1448
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

- [スマホ内蔵のセンサーを使って周辺光取得を試す](https://zenn.dev/aldagram_tech/articles/f7b57935e31070) — KSND

- [AI駆動開発で自分用の情報収集Discordサーバーを作る](https://zenn.dev/tree_and_tree/articles/ai-driven-discord-info-server) — さみっと

- [実践パスキー認証設計](https://zenn.dev/yasuakiomokawa/articles/89f5c46e8effe9) — Yasuaki Omokawa

- [Kotlin Fest 2026 参加記](https://zenn.dev/0st_ts/articles/d55862e1a134c2) — わかと

- [X の投稿を Rust で画像にするライブラリ xeet を試す](https://zenn.dev/yamauz/articles/fb97f92af23a3e) — やまう

- [QA生産性を爆上げさせるためのQA AIプラットフォーム構築](https://zenn.dev/gatechnologies/articles/8bdea59269eb10) — akki

- [物理世界とAIをつなぐ：可視化で学ぶカメラ・座標系・運動制御入門](https://zenn.dev/turing_motors/articles/cea9e3c85611b2) — ymg_aq

- [インフラ＆CI/CD（GitHub Actionsの自動デプロイ）〜化石時代のFTPから脱却。あえて作り込まない「運用カバー」の自動化〜](https://zenn.dev/dgft/articles/da631c5758aa6a) — イナガキ

- [若手の「説明力」は、AI開発で育てられるか ― 資料レビューAIを題材にしたOJTの実践](https://zenn.dev/nttdata_tech/articles/d159fdd9c38c00) — Yuichi Moriya / 守谷 祐一

- [Claude Codeが書いたコードを読む代わりにやっていること](https://zenn.dev/linkedge/articles/claude-code-instead-of-reading-code) — Misugi Takeru

- [mizchi/mutator を入れてみた](https://zenn.dev/polyco/articles/e05cb28c569801) — Tatsunori Nakano

- [GitHub IssueにArtifactとしてHTMLとMarkdownを添付できるようになった](https://zenn.dev/kesin11/articles/20261114_github_issue_artifact) — Kesin11

- [サンドボックス内のAIエージェントにHerdrを安全に使わせたい](https://zenn.dev/naofumimurata/articles/nono-hc-proxy) — Naofumi Murata

- [AIの回答が長すぎて、理解しないまま実装している問題（理解負債）](https://zenn.dev/kent_code/articles/5892898be90cac) — Kent

- [フロントエンドのフレームワークを、安全に段階的に入れ替える](https://zenn.dev/yasuakiomokawa/articles/de83bb4c4ea928) — Yasuaki Omokawa

- [ng: Neovim のためのシンプルな GUI](https://zenn.dev/shougo/articles/ng-nvim-simple-gui) — Shougo

- [5年後のエンジニアは、何に責任を持つのだろうか](https://zenn.dev/ara_ta3/articles/thinking-about-engineers-five-years-from-now) — ara_ta3

- [【pstack】AIに敵対的レビューをさせるな。トークンは検証に使え](https://zenn.dev/karamage/articles/5c3f8370b2b370) — karamage

- [Software Factoryの先へ：全社の仕事をAI-NativeにするUbieの内製クラウドエージェント基盤](https://zenn.dev/ubie_dev/articles/45501469c9c044) — Yuku Kotani

- [ISUCON2026 で優勝しました（準備編）](https://zenn.dev/luvtechno/articles/isucon2026-preparation) — Yoshinori Kawasaki


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。