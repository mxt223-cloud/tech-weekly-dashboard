# Tech Daily — 2026-11-07

生成日時: 2026-11-07T10:05:51.281267+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

**概要:** thedotmack/claude-memは、Claude CodeなどのAIエージェントのセッション間でコンテキストを永続化し、自動的な観察のキャプチャ、AIによる圧縮、関連コンテキストの将来のセッションへの注入を行うメモリ圧縮システムです。

- 言語: TypeScript
- 今週のスター: 8726
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- セッション間でコンテキストをシームレスに保存し、AIエージェントの知識の継続性を維持する（根拠: README冒頭）

- 検索、タイムライン、詳細取得の3層ワークフローを持つMCPツールによるインテリジェントなメモリ検索を提供する（根拠: MCP Search Tools）

- CLIコマンドを用いた簡単なインストールと複数IDE/エージェントへの対応を行う（根拠: Quick Start）


### 利用例

- 過去のセッションのコンテキストを引き継いでClaude CodeなどのAIエージェントを利用する（README明記／根拠: Quick Start）

- 自然言語を使用してプロジェクトの履歴や過去の決定事項を検索する（README明記／根拠: MCP Search Tools）

- クラウト同期機能やローカルワーカーサービスを利用してチームでの共同作業やプロジェクトの記録を管理する（README明記／根拠: Quick Start）


### 最初に試すこと

claude-memをインストールして動作確認する

1. npx claude-mem install を実行する


成功の目安: インストーラーが起動し、セットアップ画面またはブラウザでのサインイン案内に進むこと

未確認: 無料トライアル終了後の具体的な料金プランの詳細／サポートされているすべての環境における詳細な動作保証


## 2. [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios)

**概要:** Claude Codeのセッションを本格的なゲーム開発スタジオに変えるためのツールキットです。49体のAIエージェント、74種類のワークフロー用スキル（スラッシュコマンド）、自動検証フック、パス別のコーディング規約を備えており、実際のスタジオ階層を模した協調システムを提供します。

- 言語: Shell
- 今週のスター: 6018
- ライセンス: MIT
- AI分析状態: ok

### できること

- デザイン、プログラミング、アート、音声、ナラティブ、QA、プロダクションの各分野に特化した49体のサブエージェントを利用できる。（根拠: What's Included）

- プロジェクトのワークフロー段階を進めるための74種類のスラッシュコマンド（スキル）を実行できる。（根拠: Slash Commands）

- Godot 4、Unity、Unreal Engine 5の主要3エンジンに対応した専門家エージェントセットを選択できる。（根拠: Engine Specialists）


### 利用例

- Claude Codeのセッション内で複数のAIエージェントを組織化し、ブレインストーミングから機能実装、レビュー、リリースまでのゲーム開発プロセス全体を構造化する。（README明記／根拠: Why This Exists）

- プロジェクトの進捗度や厳格さのレベル（modes.rigor）に応じて、必要な設計ドキュメントの作成やQA検証の度合いを制御する。（README明記／根拠: Configuration）

- 開発中のコードやアセットの変更に対して自動バリデーションフックを実行し、ハードコードやルール違反を検知・防止する。（README明記／根拠: Automated Safety）


### 最初に試すこと

リポジトリをクローンしてClaude Codeを起動し、初期セットアップと開発開始のワークフローを呼び出す。

1. git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game

2. cd my-game

3. claude

4. /start


成功の目安: Claude Codeがプロジェクトのルートディレクトリで起動し、/startコマンドによって現在のプロジェクトの状態確認やワークフローのガイドが開始されること。

未確認: 実際のゲームプレイ映像の出力品質や、特定プロジェクトにおける生成ゲームの市場での成功確率


## 3. [pingdotgg/t3code](https://github.com/pingdotgg/t3code)

**概要:** T3 Codeは、ローカル環境にあるClaude Code、Codex、Cursor、Grok Build、OpenCode、Google Antigravity、fxなどのAIエージェントを、モバイルアプリ、Webアプリ、Electron製デスクトップアプリから一元的にコントロールするためのエージェント制御インターフェースです。

- 言語: TypeScript
- 今週のスター: 16782
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- モバイルアプリ、Webアプリ、Electron製デスクトップアプリを使ったエージェントのコントロール（根拠: README冒頭）

- Claude Code、Codex、Cursor、Grok Build、OpenCode、Google Antigravity、fxなどのプロバイダーとの連携（根拠: Installation）

- コマンドラインでのサーバー起動やバックグラウンドサービスとしての常駐、更新機能（根拠: Command line）


### 利用例

- スマートフォンなどのリモート端末から、手元のマシンで動作するAIエージェントを遠隔操作する（README明記／根拠: README冒頭）

- デスクトップアプリやWebアプリを用いて、複数の異なるAIエージェントの開発環境を統合的に管理する（README明記／根拠: README冒頭）

- インストールせずに一時的にコマンドを実行して動作を試す（README明記／根拠: Command line）


### 最初に試すこと

インストールせずに一時的にT3 Codeを試す

1. npx t3@latest


成功の目安: サーバーが起動し、ローカルのWebアプリが開くこと

未確認: 詳細なエージェント連携時の内部動作やAPI仕様／コントリビューションの受け入れ条件の詳細


## 4. [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

**概要:** Worktrunkは、Gitワークツリーの管理を効率化し、複数のAIエージェントを並行して実行しやすくするためのコマンドラインツールです。

- 言語: Rust
- 今週のスター: 2184
- ライセンス: NOASSERTION
- AI分析状態: ok（キャッシュ）

### できること

- ブランチ名を指定してワークツリーの切り替えや作成、削除を行える（根拠: Worktrunk makes git worktrees as easy as branches）

- ワークツリーの一覧をステータス付きで表示できる（根拠: Worktrunk makes git worktrees as easy as branches）

- フック機能によるワークフローの自動化や、LLMを活用したコミットメッセージの生成が行える（根拠: Worktrunk makes git worktrees as easy as branches）


### 利用例

- 複数のAIエージェントにそれぞれ独立した作業用ディレクトリを割り当てて並行作業させる（README明記／根拠: Context: git worktrees）

- ワークツリーを作成すると同時にClaudeなどのエージェントを起動して開発を始める（README明記／根拠: Worktrunk makes git worktrees as easy as branches）

- 作業が完了したワークツリーをマージして不要になったブランチとともに一括で削除する（README明記／根拠: Quick start）


### 最初に試すこと

新しい機能用のワークツリーを作成して切り替える

1. wt switch --create feature-auth


成功の目安: 新しいブランチとワークツリーが作成され、そこに切り替わっていること

未確認: 詳細な設定ファイルやフックのカスタムスクリプトの全仕様


## 5. [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

**概要:** Nutlope/hallmarkは、Claude Code、Cursor、Codex、OpenCode向けの「AIっぽいデザイン」を避けるためのデザインスキルです。50種類のテーマやカスタムデザイン、ブラウザでの自動lint機能などを提供し、機械的でテンプレート感のある見た目を防ぎます。

- 言語: CSS
- 今週のスター: 6900
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 50種類のテーマから適切なものを選び、ページのレイアウトや構造を構築する機能（根拠: New in v2）

- 既存のページやアプリをURL、開発サーバー、ファイルパスから指定してスクリーンショットや監査を行う機能（根拠: New in v2）

- 既存のコンテンツや配線を維持したままリデザインを行う「/hallmark redesign」や監査を行う「/hallmark audit」機能（根拠: Redesign）


### 利用例

- AIが生成したような紋切り型のデザインを避け、人間が作ったような自然なWebページを構築したい場合（README明記／根拠: README冒頭）

- 既存のWebページやアプリケーションを指定して、コンテンツの配線を変えずにデザインのリメイクや監査を行いたい場合（README明記／根拠: New in v2）

- 予約ページやショップ、ニュースレター登録など、目的のジョブに合わせたページ構造を自動で配置したい場合（README明記／根拠: New in v2）


### 最初に試すこと

hallmarkをグローバルにインストールする

1. npx skills add nutlope/hallmark -g


成功の目安: Node 18以降の環境で、パッケージが正常にインストールされること




## 6. [anthropics/skills](https://github.com/anthropics/skills)

**概要:** Claudeが専門的なタスクでパフォーマンスを向上させるため、動的に読み込む指示、スクリプト、リソースのフォルダ（スキル）を提供するAnthropicのリポジトリです。

- 言語: Python
- 今週のスター: 3159
- ライセンス: 不明
- AI分析状態: ok

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


## 7. [milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

**概要:** OpenMausBotは、Grok Botのオープンソース代替として提供される、チャットアプリ形式のAIボット管理ツールです。ローカルファーストで動作し、独自のパーソナリティや接続アプリを持つ複数のAIボットとチャット形式でやり取りできます。

- 言語: TypeScript
- 今週のスター: 6395
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- ClaudeやCodex、Grokなどの既存のAIエージェントCLIをローカル環境で実行して利用できる。（根拠: Why）

- ローカルファーストのアーキテクチャにより、トランスクリプトやキー、イベントをクラウドではなくローカル（~/.openmausbot）に保存できる。（根拠: Why）

- macOS、Windows、Ubuntu 24.04に対応したElectronベースのデスクトップアプリとして利用できる。（根拠: Quick start）


### 利用例

- サイドバーに配置された複数のボットと連絡先のようにチャットを行い、作業を監視して承認する。（README明記／根拠: README冒頭）

- SettingsからカスタムのCLIバイナリをエンジンとして指定し、独自の環境でAIボットを動作させる。（README明記／根拠: Why）


### 最初に試すこと

ソースコードから開発サーバーとデスクトップシェルを起動して動作を確認する

1. git clone https://github.com/milind-soni/OpenMausBot && cd OpenMausBot

2. pnpm install

3. pnpm dev:server

4. pnpm dev

5. pnpm dev:desktop


成功の目安: ハーネスサーバーやアプリ、Electronシェルが起動し、デスクトップアプリとして操作できるようになること

未確認: 機能セクションの続き（「Agents with hands」以降の詳細な説明）がREADMEの途中で切れているため、ボットが使用する仮想環境やクラウドLinuxデスクトップの詳細な仕様は不明です。


## 8. [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

**概要:** pbakaus/impeccableは、コーディングエージェントのためのデザイン語彙ツールです。デザインの調整、レビュー、AI生成のありふれた表現（スロップ）の検出をサポートします。

- 言語: Rust
- 今週のスター: 8172
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- デザインの方向性を調整するための24種類のコマンドを提供します。（根拠: 24 commands）

- 使い勝手のヒューリスティックに基づいてデザインをスコア化しレビューします。（根拠: Why）

- 決定的ルールを用いて、AI生成のありふれた表現や品質上の問題を検出します。（根拠: Why）


### 利用例

- 価格設定カードなどのデザインを特定の指示で調整する。（README明記／根拠: Why）

- アクセシビリティやパフォーマンス、レスポンシブ動作を技術的に監査する。（README明記／根拠: Why）

- ブラウザ上で要素を選択し、バリエーションを切り替えてライブで反復作業を行う。（README明記／根拠: Live mode）


### 最初に試すこと

Impeccableをインストールして初期化する

1. npx impeccable install

2. コーディングツールをリロードする

3. エージェントで /impeccable init を実行する


成功の目安: プロジェクトにImpeccableが初期化され、PRODUCT.mdが作成されること

未確認: 詳細な内部実装や商用利用における追加の制限事項


## 9. [obra/superpowers](https://github.com/obra/superpowers)

**概要:** Superpowersは、AIコーディングエージェント向けのエージェントスキルフレームワークおよびソフトウェア開発方法論であり、ブレインストーミングやテスト駆動開発などのスキルを自動的に組み合わせて開発プロセスをサポートします。

- 言語: Shell
- 今週のスター: 4577
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

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




## 10. [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)

**概要:** DeepTutorは、チュータリング、リサーチ、制作、演習を統合した、エージェントネイティブな生涯パーソナライズ学習ワークスペースです。

- 言語: Python
- 今週のスター: 4588
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- チャット、クイズ、リサーチ、可視化、解決、マスターパス、読書など、複数の学習モードを共有セッションコンテキスト上で実行可能。（根拠: Key Features）

- LlamaIndex、PageIndex、GraphRAG、LightRAGを用いたバージョン管理付きライブラリの構築や、ソース付き引用による学習機能。（根拠: Key Features）

- L1トレース、L2ファクト、L3合成による透明で編集可能なパーソナライズメモリ。（根拠: Key Features）


### 利用例

- パーソナライズされたチャットやクイズ、リサーチなどの多彩な学習モードを通じた学習活動の実施。（README明記／根拠: Key Features）

- 外部知識ソースやバージョン管理されたライブラリを接続した、ソース付き引用によるドキュメント読書と学習。（README明記／根拠: Key Features）

- モジュールのインストールやアンインストールによる学習環境の拡張とカスタマイズ。（README明記／根拠: Package installations only; source checkouts use enable / disable）


### 最初に試すこと

CLI環境でのモジュールインストールおよびチャットの開始

1. deeptutor module install solve

2. deeptutor chat


成功の目安: モジュールがインストールされ、CLIでチャットが再起動すること

未確認: 詳細なインストール前提条件やPythonのバージョン要件／Webアプリの具体的な起動手順



## Zenn

- [[破壊的変更] 明治時代の開始日が変更になって単体テストが失敗した件](https://zenn.dev/xin9le/articles/9a1cf8e10494d6) — xin9le

- [Web 標準動向 2026年10月版](https://zenn.dev/cybozu_frontend/articles/web-standards-trends-202610) — kuracchi

- [タスク管理までAIエージェントに任せたら、確認待ちに答えるだけになった](https://zenn.dev/rescuenow/articles/4c03a548cd6589) — しもち

- [Claudeを使いこなす人に、MagicPodは要るのか。知らないアプリでPlaywrightと比べた記録](https://zenn.dev/genda_jp/articles/7b423bcd20b532) — ikenyal

- [【.NET/Unity】C# の型制約とボックス化をハックする — IL と手動スタック配置](https://zenn.dev/aakei/articles/csharp-stack-box) — akeit0

- [Security Hub の SBOM インベントリで、Athena を使わずに組織全体のソフトウェアを調べてみた](https://zenn.dev/cscloud_blog/articles/securityhub-sbom-inventory) — 平木 佳介

- [AI駆動文章作成において俺が意識しているテクニック集](https://zenn.dev/ntk221/articles/34ad88a9225364) — ntk

- [.NET にも build.cs 欲しいんじゃーーー](https://zenn.dev/sator_imaging/articles/c10d8da7685308) — サトー™ @sator_imaging

- [Slurm は Kaggle で役に立つ](https://zenn.dev/pomcho555/articles/c455d086ec47af) — pomcho555

- [AI生成コードを本番品質に保つためのフロントエンド開発の仕組み](https://zenn.dev/sun_asterisk/articles/d4e4bc24974b99) — Phung Dinh Son

- [[TypeScript] パスエイリアスには Subpath Imports を使いたい](https://zenn.dev/mediba/articles/167e2a3f663889) — mdbr92

- [Xで積み重ねた日々をmixi2へ。過去ポストのインポート機能ができるまで](https://zenn.dev/mixi/articles/bcf2363e83b0a2) — kuno

- [集約をどこまで機械的に導けるか――形式手法をベースとしたドメインモデリング](https://zenn.dev/nrs/articles/33ba79c8b2542e) — nrs

- [SigLIP2に匹敵する画像エンコーダーをフルスクラッチで開発した話](https://zenn.dev/noetra_techblog/articles/0cea39ce67d2c2) — Mikihiro Tanaka

- [コードを読まずにバイブコーディングしたら、Claude Codeは分かっていてスルーしていた](https://zenn.dev/nexta_/articles/42a828ca2b8a02) — bik

- [OpenCode+Docker+GitHub Actionsで全自動AIペネトレーションテストはじめました](https://zenn.dev/team_zenn/articles/opencode-docker-actions-ai-pentest) — dyoshikawa

- [ADRをregoでlintする](https://zenn.dev/babarot/articles/regomark-adr-checker) — babarot

- [バイブコーディングで機能を継ぎ足していて見えてきたClaudeCodeの実装のクセ](https://zenn.dev/uguisu_blog/articles/45d1f446ece415) — ぴよ

- [ISUCON2026 で優勝しました（当日編）](https://zenn.dev/luvtechno/articles/isucon2026-competition-day) — Yoshinori Kawasaki

- [AIが書く「読みづらいADR」に発狂しかけたので、ADRのガイドラインを作った](https://zenn.dev/tokium_dev/articles/adr-authoring-guideline) — にしこりさぶろ〜 | TOKIUM


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。