# Tech Daily — 2026-10-23

生成日時: 2026-10-23T09:05:54.824979+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、ネイティブバイナリ、アプリ、ランタイム動作の逆アセンブルや調査をAIエージェントとMCP経由で行うためのツールです。ソースコードがない状態でもアプリの仕組みを解析し、証拠とともに提示します。

- 言語: TypeScript
- 今週のスター: 106341
- ライセンス: MIT
- AI分析状態: ok

### できること

- ネイティブバイナリ、JavaScript/Electronアプリ、.NETアセンブリ、ウェブサイトなどの検査ツールをエージェントに接続する（根拠: README冒頭）

- Hopper、Ghidra、IDAなどのネイティブ解析エンジンと連携して、疑似コードやアセンブリ、文字列、シンボルを解析する（根拠: What you can analyze）

- 抽出したJavaScriptやElectronアプリのディレクトリ、ASARファイルを対象にモジュールやインポート、Electron境界をJSON形式で検査する（根拠: Use the terminal）


### 利用例

- アプリに見つけた機能の仕組みをAIエージェントに調査させ、プロジェクト用のバージョンを構築する（README明記／根拠: README冒頭）

- ノートアプリの検索機能の仕組みを理解し、証拠を表示させ、プロジェクト用に同様の機能を自作する（README明記／根拠: Ask your agent）

- デスクトップアプリやゲームのバイナリ解析を行い、サウンド計算やクリップボード連携、弾幕計算などのアルゴリズムを再構築する（README明記／根拠: Showcases）


### 最初に試すこと

REAのエージェント設定と最小限のターミナル動作確認を行う

1. npx rea-agents setup

2. npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json


成功の目安: エージェント設定のセットアップ画面が起動し、ターミナルでJavaScript/Electronアプリケーションの解析結果が出力されること

未確認: 対応しているすべてのプラットフォームにおける依存ツールの詳細な導入手順やパス設定の仕様


## 2. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**概要:** anthropic/claude-plugins-official は、Claude Code向けの高品質なプラグインを集めた公式ディレクトリです。Anthropicが管理する内部プラグインと、コミュニティやパートナーによる外部プラグインを提供しています。

- 言語: Python
- 今週のスター: 5649
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


## 3. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**概要:** rufloは、Claude CodeやCodexなどのモデルを拡張するエージェントメタハーネスです。100以上の専門エージェント、協調スウォーム、アダプティブメモリ、マルチプロバイダー対応、ゼロトラストなエージェント間フェデレーション機能などを提供し、AIエージェントのチーム運用をサポートします。

- 言語: TypeScript
- 今週のスター: 3708
- ライセンス: MIT
- AI分析状態: ok

### できること

- Claude CodeやCodexなどのモデルにツール、メモリ、ループ、サンドボックス、制御レイヤーを提供するハーネス機能（根拠: Ruflo）

- コーディング、テスト、セキュリティ、ドキュメントなどに対応する100以上の専門エージェントとスウォーム協調機能（根拠: What You Get）

- mTLSとed25519によるゼロトラスト検証やPII保護パイプラインを備えたエージェントフェデレーション機能（根拠: Agent Federation — Slack for Agents）


### 利用例

- 複数マシーンや組織間でエージェント同士が安全にワークスペースを共有し、タスクを協調して実行する（README明記／根拠: Agent Federation — Slack for Agents）

- HNSWインデックス付きのベクターメモリを活用した高速なエージェントの記憶検索と学習を行う（README明記／根拠: What You Get）

- Claude Code上でプラグインやコンソールを用いてエージェントのワークフローやコストを管理する（README明記／根拠: Get started with Ruflo）


### 最初に試すこと

Rufloの初期化ウィザードを実行してプロジェクトのセットアップを行う

1. npx ruflo@latest init wizard


成功の目安: プロジェクトのセットアップウィザードが正常に起動し、ホストサーフェス等の設定が行われること




## 4. [android/skills](https://github.com/android/skills)

**概要:** Android開発向けのAI最適化されたモジュール式指示とリソースを提供するリポジトリです。LLMが苦手とするユースケースやワークフローを対象としています。

- 言語: Kotlin
- 今週のスター: 1384
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


## 5. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

**概要:** Scientific Agent Skillsは、AIエージェントに生物学、化学、医学などの科学的タスクを実行させるための177件の検証済みスキルと100以上の科学データベースを提供するライブラリです。

- 言語: Python
- 今週のスター: 3967
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 177件の科学・研究スキルと100以上の科学データベースへの対応（根拠: README冒頭）

- Cisco AI Defense Skill Scannerを用いたLLMベースのセキュリティスキャン（根拠: ⚠️ Security Disclaimer）


### 利用例

- AIエージェントに複雑な多段階の科学的ワークフローを実行させること（README明記／根拠: 💡 Quick Examples）

- NVIDIA OpenShellなどのポリシー制御されたサンドボックス環境内でスキルを実行すること（README明記／根拠: 🔬 Use Cases）


### 最初に試すこと

サードパーティ製スキルのローカルセキュリティスキャンを実行する

1. uv pip install cisco-ai-skill-scanner

2. skill-scanner scan /path/to/skill --use-behavioral


成功の目安: スキャンコマンドがエラーなく実行され、結果が出力されること

未確認: Getting Startedセクションの具体的なインストールコマンドの記述／Quick Examplesセクションの具体的なプロンプト例の記述


## 6. [anomalyco/opencode](https://github.com/anomalyco/opencode)

**概要:** opencode は、開発作業を支援するオープンソースの AI コーディングエージェントです。

- 言語: TypeScript
- 今週のスター: 6750
- ライセンス: MIT
- AI分析状態: ok

### できること

- 開発作業向けのフルアクセスなビルドエージェント（build）を利用できます。（根拠: Agents）

- 分析やコード探索用の読み取り専用プランエージェント（plan）を利用できます。（根拠: Agents）

- 複雑な検索や複数ステップのタスク向けの一般的なサブエージェント（general）を利用できます。（根拠: Agents）


### 利用例

- 見慣れないコードベースの探索や変更の計画に活用できます。（README明記／根拠: Agents）


### 最初に試すこと

CLIツールをインストールして利用を開始する

1. curl -fsSL https://opencode.ai/v2/install | bash


成功の目安: opencodeがインストールされ、利用可能になること

未確認: 詳細な内部プロンプトの仕組みや対応しているすべてのAIモデルの種類


## 7. [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

**概要:** CLI-Anythingは、あらゆるソフトウェアをAIエージェント対応のCLIに変換するためのフレームワークおよびハブです。

- 言語: Python
- 今週のスター: 3275
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- cli-anything-hubパッケージマネージャーを介したコミュニティ製CLIのブラウジング、検索、インストール、管理。（根拠: 🚀 Quick Start）


### 利用例

- 既存のCLIエコシステムを利用して、公開されている便利なCLIをインストールして実行する。（README明記／根拠: 🚀 Quick Start）


### 最初に試すこと

CLI-Hubパッケージマネージャーのインストール

1. pip install cli-anything-hub


成功の目安: cli-hubコマンドが利用可能になること

未確認: 7フェーズのハーネス生成の詳細なコマンドや手順


## 8. [cursor/plugins](https://github.com/cursor/plugins)

**概要:** Cursorプラグインの仕様と、開発者ツール、フレームワーク、SaaS製品向けの公式プラグイン群を提供するリポジトリです。

- 言語: TypeScript
- 今週のスター: 2046
- ライセンス: 不明
- AI分析状態: ok

### できること

- 人気のある開発者ツールやSaaS製品向けの公式Cursorプラグイン集を提供する（根拠: README冒頭）

- 各プラグインがリポジトリのルートに独立したディレクトリとして配置され、プラグイン用マニフェストを持つ構造にする（根拠: README冒頭）

- マーケットプレイス用マニフェスト（marketplace.json）と、各プラグインのマニフェスト（plugin.json）で構成されるマルチプラグインのマーケットプレイスリポジトリである（根拠: Repository structure）


### 利用例

- GitHubやGoogle Drive、Slack等のSaaS製品やツールと連携するプラグインを探して利用する（README明記／根拠: README冒頭）

- 独自のエージェントプラグインを新しく作成して検証する（README明記／根拠: Plugins）

- TypeScript SDKを使用してアプリやスクリプト、自動化機能を構築する（README明記／根拠: Plugins）


### 最初に試すこと

リポジトリのプラグイン構成や一覧を確認する

1. リポジトリのREADMEを開き、提供されているプラグインの一覧を確認する

2. Repository structureのセクションでディレクトリ構成を確認する


成功の目安: プラグインの一覧と各ディレクトリの構造が確認できていること

未確認: 具体的なインストールコマンドやセットアップ手順／各プラグインの詳細な利用方法やコード例


## 9. [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

**概要:** ai-memoryは、複数のAIコーディングエージェント（Claude Code、Codex、Cursorなど）の間で長期的なコンテキストや作業の引き継ぎを共有するためのRust製ソリューションです。

- 言語: Rust
- 今週のスター: 3322
- ライセンス: MIT
- AI分析状態: ok

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


## 10. [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

**概要:** VoiceStudioは、音声クローン、音声デザイン、動画の吹き替え、ディクテーション、文字起こし、オーディオブック作成を646言語でサポートするオープンソースのローカル音声AIアプリケーションです。

- 言語: Python
- 今週のスター: 13581
- ライセンス: AGPL-3.0
- AI分析状態: ok

### できること

- 音声クローン作成および独自の音声デザイン（根拠: Your voice. Your workflow.）

- タイミングの合った音声による動画の吹き替え（根拠: Your voice. Your workflow.）

- ローカルAPIおよびエージェント向けMCPの提供（根拠: Your voice. Your workflow.）


### 利用例

- 自分の声をクローンしたり、新しい音声デザインを作成して音声生成を行う（README明記／根拠: Your voice. Your workflow.）

- 浮動ウィジェットを使用してディクテーションを行う（README明記／根拠: Your voice. Your workflow.）

- 物語やオーディオブック、バッチジョブの生産（README明記／根拠: Your voice. Your workflow.）


### 最初に試すこと

macOSまたはLinux環境でワンコマンドインストールスクリプトを実行してデスクトップアプリをインストールする

1. ターミナルを開く

2. 以下のコマンドを実行する: curl -fsSL https://voicestudio.sh/install | sh


成功の目安: VoiceStudioのElectronデスクトップアプリが正常にインストールされること

未確認: 対応している646言語の具体的な言語リスト／デフォルト以外の全エンジンの詳細な動作要件



## Zenn

- [Node.jsの2026年10月セキュリティリリースに、手元の50リポジトリとVercel・Cloud Runで対応した](https://zenn.dev/yoshinani_dev/articles/0e6513a56eb629) — ひょうどう

- [Claude CodeやCodexで並列開発していたら、Macのストレージが残り8GBになったので掃除した](https://zenn.dev/yoshinani_dev/articles/0c17dec1c082a1) — ひょうどう

- [自宅サーバーの定期バックアップの失敗に気付かなかった話](https://zenn.dev/komorebi_note/articles/d9df64e7e1da82) — こもれび｜インフラ勉強中

- [Rootless Dockerと学ぶSELinux【初心者向け】](https://zenn.dev/nexryai/articles/afb828d7dda6b7) — nexryai

- [テニス解析をピックルボールに使ってみた：四隅の指定でコートの俯瞰表示を補う①](https://zenn.dev/nauh_blog/articles/7f19a2f193d15d) — Ryuji Fujisawa

- [KMPデスクトップはAIエージェントに速いのか？検証してみる](https://zenn.dev/shogo/articles/f847c35ea8dccb) — shogo.yamada

- [脆弱性管理の仕組みを整えた](https://zenn.dev/dress_code/articles/be5550254695cd) — anizozina

- [エージェント用 IDE を3つ試して、今さら cmux を使い始めた](https://zenn.dev/yoshi47/articles/cmux-after-agent-ides) — yoshi47

- [【速報：2026/10/22 04:00】PHP2Shellの対応状況まとめ：PHP本体、Linux、レンタルサーバ、KUSANAGI](https://zenn.dev/tyamadadd/articles/c02a27af771dd2) — tyamadadd

- [「PHPのドカ脆弱性」=「今すぐDynmap止めろ」ではなかった話](https://zenn.dev/56drich/articles/f52bd4a1dae988) — ゴロードリヒ

- [10月21日、PHP2Shell対応の後片付けが終わらない](https://zenn.dev/subara3/articles/1165119ef70e75) — Subara3

- [セキュアな実装をするために意識したいこと](https://zenn.dev/dress_code/articles/unauthorized-access-secure-implementation) — 山田 哲也 / Tetsuya Yamada

- [Next.js の脆弱性に Dependabot が反応しなかったので、GitHub Advisory Database までの流れを追った](https://zenn.dev/rakko_inc/articles/dependabot-cve-to-pr-flow) — katsu

- [仕組みを理解する動画を、Claude Codeに作らせると便利すぎる](https://zenn.dev/explaza/articles/c749042ecbe232) — musoukun

- [バイブコーディングを6週間続けたら、Mac の起動が20分かかるようになった](https://zenn.dev/singularity/articles/vibe-coding-mac-boot-20min) — Isamu

- [AI にリバースエンジニアリングさせる REA を触って、持ち帰ったのは「証拠付きで進める」考え方でした](https://zenn.dev/flinters_blog/articles/3b377ce568d676) — Takashi Kawachi

- [Oxlint + Oxfmt で規約をコード化するモノレポ運用](https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006) — Toshiki Okazaki

- [Chromium(V8)のArray.prototype.fillを最大約7倍高速化した](https://zenn.dev/dinii/articles/5b8edc7856c25b) — Riya Amemiya

- [Claude Code で CI 待ち時間を 18 分から 4 分台に短縮する【GitHub Actions】](https://zenn.dev/edash_tech_blog/articles/5b90aa33bd8d49) — iakito

- [AI時代、配布するPythonコードをどう守るか: 難読化の実験と判断軸](https://zenn.dev/pksha/articles/0f9c11d1daea2e) — 山本隼輔


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。