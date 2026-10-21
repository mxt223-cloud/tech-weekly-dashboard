# Tech Daily — 2026-10-21

生成日時: 2026-10-21T09:02:56.491768+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、ネイティブバイナリ、アプリ、ランタイム動作などをAIエージェントと組み合わせてリバースエンジニアリングするためのMCPサーバーおよびCLIツールです。

- 言語: TypeScript
- 今週のスター: 157631
- ライセンス: MIT
- AI分析状態: ok

### できること

- ネイティブバイナリの擬似コード、アセンブリ、文字列、シンボル、呼び出し、参照の検査（根拠: What you can analyze）

- JavaScriptやElectronアプリケーションのモジュール、インポート、ソースマップ、ルート、IPC関係の解析（根拠: What you can analyze）

- .NETアセンブリのメタデータ、CIL命令、宣言されたネイティブ依存関係、ビルド比較の静的検査（根拠: What you can analyze）


### 利用例

- アプリ内の特定の機能がどのように動作しているかを調査し、同じような機能を自分のプロジェクト用に構築する（README明記／根拠: README冒頭）

- ゲーム内の古い計算処理やサウンドの仕組みを解析してC言語やC++として再構築する（README明記／根拠: Showcases）

- Electronアプリのレンダラーからメインプロセスへ至るクリップボード連携やAPIの挙動を追跡する（README明記／根拠: Showcases）


### 最初に試すこと

REAのエージェント連携セットアップを行う

1. Node.jsとnpmがインストールされた環境で端末を開く

2. npx rea-agents setup を実行する

3. 使用するエージェントを選択し、変更内容を確認して承認する

4. エージェントを再起動する


成功の目安: REAのMCPサーバーとワークフロー手順がエージェントに正しく登録され、利用可能になること

未確認: ネイティブ解析プロバイダとしてHopper、Ghidra、IDA以外の未記載ツールに対応しているかどうか／対応しているすべてのプラットフォームにおける具体的な依存関係の詳細


## 2. [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)

**概要:** ai-job-searchは、Claude Codeを基盤として自身のPC上で動作するAI求職・応募フレームワークです。求人情報の評価、CV（履歴書）の最適化、カバーレターの作成、面接対策を自動化します。

- 言語: Python
- 今週のスター: 12848
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- Claude Codeを活用して、求人広告の評価や適合度のスコアリング、CVのカスタマイズ、カバーレターの作成を行います。（根拠: README冒頭）

- 自身のプロフィールを設定し、ドラフターとレビューアーによるアプリケーションパイプラインを実行します。（根拠: What this is）

- 求人ポータルサイトの検索やセットアップのためのコマンド（/setup、/scrape、/applyなど）を提供します。（根拠: What this is）


### 利用例

- 自分のPC上で求職活動を自動化し、求人の適合度評価やCVの作成、面接対策を行う。（README明記／根拠: README冒頭）

- LaTeXなどを使用して、応募先企業や職務に合わせたカスタムCVやカバーレターを自動生成する。（README明記／根拠: What this is）

- デンマーク市場向けの求人ポータル検索機能を利用して求人を探す。（README明記／根拠: What this is）


### 最初に試すこと

リポジトリをフォークし、前提条件を確認してセットアップを開始する

1. リポジトリをフォークして自身の環境にクローンする

2. Claude CodeやPython 3.10+、Bun、LaTeXディストリビューションなどの前提条件を準備する


成功の目安: 前提条件が整い、ドキュメントの指示に従ってプロフィール設定の準備ができること

未確認: Quick startセクションの具体的なインストール・実行コマンド（READMEが途中で切れているため詳細なコマンドライン手順は不明）


## 3. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**概要:** anthropic/claude-plugins-official は、Claude Code向けの高品質なプラグインを集めた公式ディレクトリです。Anthropicが管理する内部プラグインと、コミュニティやパートナーによる外部プラグインを提供しています。

- 言語: Python
- 今週のスター: 5650
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


## 4. [mksglu/context-mode](https://github.com/mksglu/context-mode)

**概要:** Context Modeは、AIコーディングエージェントのコンテキストウィンドウを最適化するためのMCPサーバーです。ツール出力をサンドボックス化して削減し、SQLiteによるセッションメモリの永続化、コード実行によるコンテキスト節約、そして17のプラットフォームにわたるセキュリティ権限の強制を行います。

- 言語: TypeScript
- 今週のスター: 3556
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


## 5. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

**概要:** Ghidraは、アメリカ国家安全保障局（NSA）が開発したソフトウェアリバースエンジニアリング（SRE）フレームワークです。コンパイルされたコードの解析を行うための逆アセンブル、アセンブル、逆コンパイル、グラフ化、スクリプト実行などの高度なツールを備えています。

- 言語: Java
- 今週のスター: 6184
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


## 6. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

**概要:** Scientific Agent Skillsは、AIエージェントに生物学、化学、医学などの科学的タスクを実行させるための177件の検証済みスキルと100以上の科学データベースを提供するライブラリです。

- 言語: Python
- 今週のスター: 4549
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


## 7. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを確定的なMP4動画に変換するためのオープンソースフレームワークです。AIコーディングエージェントとの統合や、CLI、ホスト型オーサリングのレンダリングコアとしての利用を想定して設計されています。

- 言語: TypeScript
- 今週のスター: 5994
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




## 8. [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

**概要:** VoiceStudioは、音声クローン、音声デザイン、ビデオの吹き替え、ディクテーション、音声文字起こし、オーディオブック作成を646言語で提供するオープンソースのローカル完全対応アプリケーションです。

- 言語: Python
- 今週のスター: 17057
- ライセンス: AGPL-3.0
- AI分析状態: ok

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


## 9. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**概要:** Rufloは、Claude CodeやCodexなどのモデル上で動作するエージェントメタハーネスであり、多人数エージェントのスウォーム協調、自律ワークフロー、アダプティブメモリ、ベクトルRAG統合などの機能を提供します。

- 言語: TypeScript
- 今週のスター: 3143
- ライセンス: MIT
- AI分析状態: ok

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




## 10. [android/skills](https://github.com/android/skills)

**概要:** Android開発向けのAI最適化されたモジュール式指示とリソースを提供するリポジトリです。LLMが苦手とするユースケースやワークフローを対象としています。

- 言語: Kotlin
- 今週のスター: 1255
- ライセンス: Apache-2.0
- AI分析状態: ok

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



## Zenn

- [テストの前提を「実際に遊んで撮ったセーブ」に替えたら、撮影ボットがソフトロックを見つけた](https://zenn.dev/gzer0/articles/real-play-save-fixtures-for-ai-tests) — gzer0

- [AI にリバースエンジニアリングさせる REA を触って、持ち帰ったのは「証拠付きで進める」考え方でした](https://zenn.dev/flinters_blog/articles/3b377ce568d676) — Takashi Kawachi

- [Oxlint + Oxfmt で規約をコード化するモノレポ運用](https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006) — Toshiki Okazaki

- [Chromium(V8)のArray.prototype.fillを最大約7倍高速化した](https://zenn.dev/dinii/articles/5b8edc7856c25b) — Riya Amemiya

- [Claude Code で CI 待ち時間を 18 分から 4 分台に短縮する【GitHub Actions】](https://zenn.dev/edash_tech_blog/articles/5b90aa33bd8d49) — iakito

- [npm と比べて分かった Go の依存管理の「一番の違い」── go get の中身を 6 ステップで追う](https://zenn.dev/shiro_kuma_san/articles/8abfbdacfeaa59) — shiro_kuma_san

- [対象が広い事業・プロダクトが刺さる気がしない](https://zenn.dev/fusa_bp/articles/broad-target-reaches-no-one) — fusa_bp

- [macOSで特定のビューをスクリーンキャプチャから隠す](https://zenn.dev/d_date/articles/macos-capture-protection-preventscapture) — Daiki Matsudate

- [AIを利用したレガシーコード改善](https://zenn.dev/naoyuki1212/articles/20261019-legacy-code-with-ai) — Naoyuki

- [Cloudflare + EmDash の自サイトを点検したら Server-Timing から内部情報が見えていた話](https://zenn.dev/masaru21/articles/2100616bb5110d) — lonely_creator_m

- [AIとコンテストに参加する](https://zenn.dev/attgm/articles/d28df25b88254a) — a2

- [個人情報入りの PDF を AI に渡さない：Drive の前に「関所」を置いて突き合わせを自動化した話](https://zenn.dev/hisa_tech_2973/articles/9cb4aee5b999fa) — HISA

- [普段使いのWindows PCでNodeのサーバーを常駐させて踏んだ罠](https://zenn.dev/matasuke_t/articles/bf784b79b29e86) — またすけ

- [Progate git自作インターン参加記〜AIとチーム開発との付き合い方〜](https://zenn.dev/yurapii/articles/2622d98d641acc) — ゆらぴー

- [Claude Codeの会話を55分放っておいたら、272,422トークンが13,522に圧縮されていました ― アイドル圧縮の観測](https://zenn.dev/ojisan_ai_lab/articles/claude-code-idle-compaction-20261019) — おじさんAIラボ

- [AI時代、配布するPythonコードをどう守るか: 難読化の実験と判断軸](https://zenn.dev/pksha/articles/0f9c11d1daea2e) — 山本隼輔

- [生産計画を手を動かして学ぶ ― OSS の frePPLe で MRP・需要予測・CP-SAT まで](https://zenn.dev/rkawajiri/books/frepple-tutorial-ja) — Ryoma Kawajiri

- [ポートフォリオをVoidで作り直したので、Voidの来歴と中身を整理する](https://zenn.dev/nkzn/articles/my-first-void) — Nkzn

- [技術書を年に数冊しか買わない自分に、O'Reillyのサブスク年$150は割に合うか（ACM経由で契約してMCPまで）](https://zenn.dev/sonicmoov/articles/oreilly-subscription-acm) — m.okamura

- [有名 OSS が PR を閉じはじめた。何が起きていて、どう向き合うか](https://zenn.dev/hand_dot/articles/ecb391d4322330) — Kyohei Fukuda


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。