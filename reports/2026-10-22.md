# Tech Daily — 2026-10-22

生成日時: 2026-10-22T09:08:26.571340+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、バイナリ、アプリケーション、ランタイムの動作などをAIエージェントと連携してリバースエンジニアリングするためのModel Context Protocol (MCP) ツールです。ソースコードがない状態でもアプリの動作調査や検証、証拠の提示を行うことができます。

- 言語: TypeScript
- 今週のスター: 129417
- ライセンス: MIT
- AI分析状態: ok

### できること

- ネイティブバイナリ、JavaScript、Electronアプリ、.NETアセンブリ、ウェブサイトなどの検査をエージェントのツールに接続します。（根拠: README冒頭）

- Hopper、Ghidra、IDAなどのネイティブ分析エンジンを用いた疑似コードやアセンブリの取得が可能です。（根拠: What you can analyze）

- ローカル環境で分析を実行し、各結論の裏付けとなる証拠や制限事項を含めた結果を返します。（根拠: README冒頭）


### 利用例

- アプリ内の機能がどのように動いているかを調査し、自分のプロジェクト向けの類似機能を構築する。（README明記／根拠: README冒頭）

- 抽出したJavaScriptやElectronアプリのディレクトリ、ASARファイルを分析し、モジュールやインポート関係を把握する。（README明記／根拠: Quick start）


### 最初に試すこと

REAのエージェント設定をセットアップする

1. npx rea-agents setup を実行する

2. エージェントを選択して変更内容を確認し、承認して再起動する


成功の目安: REAのMCPサーバーとワークフロー手順がエージェントに追加されること




## 2. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**概要:** anthropic/claude-plugins-official は、Claude Code向けの高品質なプラグインを集めた公式ディレクトリです。Anthropicが管理する内部プラグインと、コミュニティやパートナーによる外部プラグインを提供しています。

- 言語: Python
- 今週のスター: 5703
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


## 3. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

**概要:** Scientific Agent Skillsは、AIエージェントに生物学、化学、医学などの科学的タスクを実行させるための177件の検証済みスキルと100以上の科学データベースを提供するライブラリです。

- 言語: Python
- 今週のスター: 4719
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


## 4. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**概要:** Rufloは、Claude CodeやCodexなどのモデル上で動作するエージェントメタハーネスであり、多人数エージェントのスウォーム協調、自律ワークフロー、アダプティブメモリ、ベクトルRAG統合などの機能を提供します。

- 言語: TypeScript
- 今週のスター: 3590
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 100以上の専門エージェントによるコーディング、テスト、セキュリティ、ドキュメント作成、アーキテクチャ設計のサポート（根拠: What You Get）

- HNSWインデックス付きのベクトルメモリとエージェントDBによる高速な検索機能（根拠: What You Get）

- ゼロトラストなエージェントフェデレーションによる、異なるマシンや組織間の安全な協調作業（根拠: What You Get）


### 利用例

- Claude Code環境内でプラグインやコンソール機能を用いて、複数の自律エージェントやスウォームを統括する。（README明記／根拠: Get started with Ruflo）

- エージェント間でのベクトル検索やRAG統合を活用し、過去の成功パターンから自己学習する開発支援環境を構築する。（README明記／根拠: What You Get）

- 複数マシン間でのセキュアなエージェント連携（フェデレーション）により、機密データを保護しながらタスクを分散処理する。（README明記／根拠: Agent Federation — Slack for Agents）


### 最初に試すこと

CLIインストールによるプロジェクトセットアップとウィザードの実行

1. npx ruflo@latest init wizard


成功の目安: プロジェクトのセットアップウィザードが正常に起動すること




## 5. [android/skills](https://github.com/android/skills)

**概要:** Android開発向けのAI最適化されたモジュール式指示とリソースを提供するリポジトリです。LLMが苦手とするユースケースやワークフローを対象としています。

- 言語: Kotlin
- 今週のスター: 1332
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


## 6. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

**概要:** Ghidraは、アメリカ国家安全保障局（NSA）が開発したソフトウェアリバースエンジニアリング（SRE）フレームワークです。コンパイルされたコードの解析を行うための逆アセンブル、アセンブル、逆コンパイル、グラフ化、スクリプト実行などの高度なツールを備えています。

- 言語: Java
- 今週のスター: 5769
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


## 7. [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

**概要:** VoiceStudioは、音声クローン、音声デザイン、ビデオの吹き替え、ディクテーション、音声文字起こし、オーディオブック作成を646言語で提供するオープンソースのローカル完全対応アプリケーションです。

- 言語: Python
- 今週のスター: 15125
- ライセンス: AGPL-3.0
- AI分析状態: ok（キャッシュ）

### できること

- 音声のクローン作成や独自の音声デザインができる（根拠: Your voice. Your workflow.）

- タイミングの合った音声でビデオの吹き替えができる（根拠: Your voice. Your workflow.）

- ローカルAPIやMCP（Model Context Protocol）をエージェント向けに提供する（根拠: Your voice. Your workflow.）


### 利用例

- 自分の声や他者の声をクローンして、テキストから音声を生成する（README明記／根拠: Your voice. Your workflow.）

- 動画ファイルに対してタイミングを合わせた吹き替え音声を作成する（README明記／根拠: Your voice. Your workflow.）

- ストーリーテリングやオーディオブック、バッチ処理による音声コンテンツの大量生成を行う（README明記／根拠: Your voice. Your workflow.）


### 最初に試すこと

macOSまたはLinux環境でワンコマンドインストールスクリプトを実行してデスクトップアプリを導入する

1. 端末（ターミナル）を開く

2. curl -fsSL https://voicestudio.sh/install | sh を実行する


成功の目安: VoiceStudioのデスクトップアプリが正常にインストールされ、起動できる状態になること

未確認: 対応している646言語それぞれの詳細な品質や個別エンジンの挙動／各モデルウェイトの商用利用に関する具体的な権利範囲


## 8. [mksglu/context-mode](https://github.com/mksglu/context-mode)

**概要:** Context Modeは、AIコーディングエージェントのコンテキストウィンドウを最適化するためのMCPサーバーです。ツール出力をサンドボックス化して削減し、SQLiteによるセッションメモリの永続化、コード実行によるコンテキスト節約、そして17のプラットフォームにわたるセキュリティ権限の強制を行います。

- 言語: TypeScript
- 今週のスター: 2968
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


## 9. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを決定論的なMP4動画に変換するためのオープンソースフレームワークです。CLIを用いたローカルでの操作やAIコーディングエージェントからのスキル利用、ホスト型オーサリングワークフローのレンダリングコアとして機能します。

- 言語: TypeScript
- 今週のスター: 5740
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- HTMLとCSS、シーク可能なアニメーションを使用して決定論的なMP4動画をレンダリングする（根拠: README冒頭）

- CLIやAIコーディングエージェントのスキルを通じて動画の作成、プレビュー、レンダリングを行える（根拠: Quick Start）

- GSAP、CSSアニメーション、Lottie、Three.js、Anime.js、WAAPIなどのフレームアダプターを利用したアニメーションに対応する（根拠: How It Works）


### 利用例

- 製品発表動画や機能アナウンスメントの作成（README明記／根拠: What You Can Build）

- アニメーション付きコード差分、ナレーション、字幕を含むPRウォークスルーの作成（README明記／根拠: What You Can Build）

- データビジュアライゼーションやチャートレース、マップアニメーションの制作（README明記／根拠: What You Can Build）


### 最初に試すこと

プロジェクトの初期化、ブラウザでのライブリロードプレビュー、MP4へのレンダリングを行う

1. npx hyperframes init my-video

2. cd my-video

3. npx hyperframes preview

4. npx hyperframes render


成功の目安: ブラウザでのライブリロードプレビューが表示され、プロジェクトがMP4へレンダリングされること

未確認: AWS Lambdaレンダリングの詳細なセットアップ手順や設定ファイルの内容


## 10. [cursor/plugins](https://github.com/cursor/plugins)

**概要:** Cursor用の公式プラグインおよび仕様をまとめたマルチプラグインリポジトリです。開発ツール、生産性向上ツール、各種SaaS連携などのプラグインが含まれており、それぞれが独立したディレクトリとプラグインマニフェストを持っています。

- 言語: TypeScript
- 今週のスター: 2049
- ライセンス: 不明
- AI分析状態: ok

### できること

- 人気のある開発ツール、フレームワーク、SaaS製品向けの公式Cursorプラグインを提供する（根拠: README冒頭）

- 各プラグインをリポジトリのルートに独立したディレクトリとして配置し、plugin.jsonマニフェストを持たせる（根拠: README冒頭）

- ルートの.cursor-plugin/marketplace.jsonですべてのプラグインを一覧化する（根拠: Repository structure）


### 利用例

- コードレビューやCI、デプロイなどの開発チーム向けワークフローをCursorプラグインで自動化する（README明記／根拠: Plugins）

- Gmail、Google Drive、GitHub、Slackなどの外部サービスやSaaSと連携してデータを操作する（README明記／根拠: Plugins）


### 最初に試すこと

リポジトリの構造やプラグイン一覧を確認する

1. リポジトリのREADMEを開き、提供されているプラグインの一覧を確認する

2. plugins/ ディレクトリ以下の構造を確認する


成功の目安: プラグイン一覧やリポジトリのディレクトリ構成が確認できること

未確認: 各プラグインの具体的なインストール方法やセットアップコマンド／クイックスタートの詳細手順



## Zenn

- [cronのclaude -pが"ok"だけで4万トークン——--safe-modeと--tools ""で98%削減](https://zenn.dev/yosiki/articles/claude-p-cron-token-diet) — yosiki

- [個人事業主が App Store の有料アプリ契約を有効にするまで。Apple は組織を選べず、私は納税フォームを2つ出した](https://zenn.dev/hk_work/articles/sole-proprietor-app-store-paid-apps-agreement) — HIROKI KUROGI

- [Amazon Bedrock Guardrails を AnswerCarefully で試してみた](https://zenn.dev/aws_japan/articles/bedrock-guardrails-japanese-tier) — Yuta Okubo

- [EKS に Graviton を導入して、arm64 と amd64 を混ぜて運用を始めました](https://zenn.dev/socialplus/articles/eks-graviton-arm64-migration) — guchim

- [Package.resolved の originHash は何のためにあるのか](https://zenn.dev/zunda_pixel/articles/ecba94910fa062) — zunda

- [Devinに問い合わせ調査を任せて見えてきた「原因未特定」の正体。過去の約700件を分類してみた](https://zenn.dev/canly/articles/9c19bb123e208c) — ddd

- [Laravel の token guard 認証バイパス、表に無い 11 以下はどうなの？全タグのソースを確認してみた](https://zenn.dev/nix/articles/236ceb8194a9c5) — ___nix___

- [安くて速い Jev を6回チューニングしたら、最後に Claude の grep に2倍差で負けた話](https://zenn.dev/koudai0711/articles/f7a5cc10496820) — koudai0711

- [dbt と Cloud DLP で面接の文字起こしから氏名を消す実装ガイド](https://zenn.dev/zenkigen_tech/articles/1714ede7f27e10) — なずな

- [LINEに送った写真と音声メモを、自宅のPCが文字にしてくれるようにした](https://zenn.dev/hilopon/articles/line-local-ai-photo-voice-capture) — みんなのおたすけ研究所

- [PTCG AI Battle Challenge Simulation振り返り＆反省](https://zenn.dev/ryyy_my/articles/d35d4c655c63f2) — ryuto_my

- [AI にリバースエンジニアリングさせる REA を触って、持ち帰ったのは「証拠付きで進める」考え方でした](https://zenn.dev/flinters_blog/articles/3b377ce568d676) — Takashi Kawachi

- [Oxlint + Oxfmt で規約をコード化するモノレポ運用](https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006) — Toshiki Okazaki

- [Chromium(V8)のArray.prototype.fillを最大約7倍高速化した](https://zenn.dev/dinii/articles/5b8edc7856c25b) — Riya Amemiya

- [AIペネトレーションテストツール「Strix」を試してみた](https://zenn.dev/turquoise123/articles/df481032f6b405) — yokoyan

- [Claude Code で CI 待ち時間を 18 分から 4 分台に短縮する【GitHub Actions】](https://zenn.dev/edash_tech_blog/articles/5b90aa33bd8d49) — iakito

- [Cloudflare + EmDash の自サイトを点検したら Server-Timing から内部情報が見えていた話](https://zenn.dev/masaru21/articles/2100616bb5110d) — lonely_creator_m

- [AI時代、配布するPythonコードをどう守るか: 難読化の実験と判断軸](https://zenn.dev/pksha/articles/0f9c11d1daea2e) — 山本隼輔

- [生産計画を手を動かして学ぶ ― OSS の frePPLe で MRP・需要予測・CP-SAT まで](https://zenn.dev/rkawajiri/books/frepple-tutorial-ja) — Ryoma Kawajiri

- [ポートフォリオをVoidで作り直したので、Voidの来歴と中身を整理する](https://zenn.dev/nkzn/articles/my-first-void) — Nkzn


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。