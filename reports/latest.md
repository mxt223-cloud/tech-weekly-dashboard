# Tech Daily — 2026-10-25

生成日時: 2026-10-25T08:33:43.323746+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

**概要:** cloudflare/security-audit-skillは、コーディングエージェントをセキュリティ監査人に変えるスキルリポジトリです。偵察、カバレッジ主導のハント、候補検証、構造化出力、独立した記録検証、ターゲット非依存のレポート作成という6つのフェーズで構造化されたセキュリティ監査を実行します。

- 言語: JavaScript
- 今週のスター: 11223
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




## 2. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、バイナリやアプリケーション、実行時の振る舞いをAIエージェントと連携してリバースエンジニアリングするためのMCPサーバーおよびCLIツールです。

- 言語: TypeScript
- 今週のスター: 88243
- ライセンス: MIT
- AI分析状態: ok

### できること

- ネイティブバイナリ、JavaScript/Electronアプリ、.NETアセンブリ、ウェブサイトなど多様なターゲットの調査に対応しています。（根拠: What you can analyze）

- Hopper、Ghidra、IDAなどのネイティブ解析エンジンや静的解析ツールと連携し、擬似コードやアセンブリ、文字列などを取得します。（根拠: What you can analyze）

- ローカルでの分析を実行し、結論の背後にある証拠や制限事項を含めた結果を返します。（根拠: README冒頭）


### 利用例

- アプリ内で使われている機能をAIエージェントに調査させ、ソースコードなしで仕組みを理解して自分のプロジェクト用に再構築する。（README明記／根拠: README冒頭）

- 抽出したJavaScriptやElectronアプリのディレクトリまたはASARファイルを対象に、モジュールやインポート情報を検査する。（README明記／根拠: Quick start）

- ゲームなどのバイナリの動作や計算処理を解析し、当時の実装をC/C++などで再現する。（README明記／根拠: Showcases）


### 最初に試すこと

エージェントにREAをセットアップし、動作確認を行う

1. npx rea-agents setup


成功の目安: エージェントにMCPサーバーとワークフロー手順が追加され、設定が完了すること

未確認: サポートされているすべてのエージェントの詳細な動作仕様／外部ネイティブ解析ツールのライセンス認証の個別手順


## 3. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**概要:** anthropic/claude-plugins-official は、Claude Code向けの高品質なプラグインを集めた公式ディレクトリです。Anthropicが管理する内部プラグインと、コミュニティやパートナーによる外部プラグインを提供しています。

- 言語: Python
- 今週のスター: 4250
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


## 4. [ruvnet/ruflo](https://github.com/ruvnet/ruflo)

**概要:** ruvnet/rufloは、Claude CodeやCodexなどのモデルを拡張するエージェントのメタハーネスであり、100以上の専門エージェント、協調スウォーム、自己学習メモリ、ゼロトラストなエージェント間フェデレーション機能を提供します。

- 言語: TypeScript
- 今週のスター: 3349
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 100種類以上のコーディング、テスト、セキュリティ、ドキュメント作成向け専門エージェント（根拠: What You Get）

- 複数マシン間での安全な情報交換やピア認証を行うゼロトラストフェデレーション機能（根拠: Agent Federation — Slack for Agents）

- HNSWインデックスによる高速なベクトルメモリ（AgentDB）（根拠: What You Get）


### 利用例

- 複数エージェントによる協調的なワークフローの自動化とタスク調整（README明記／根拠: README）

- 過去の成功パターンやフィードバックから学習する自己学習型プロセスの実行（README明記／根拠: What You Get）

- 脆弱性やCVEスキャン、プロンプトインジェクションのブロックといったセキュリティ監査（README明記／根拠: What You Get）


### 最初に試すこと

Claude Code環境でプラグインマーケットプレイスからrufloをインストールして初期化する

1. /plugin marketplace add ruvnet/ruflo

2. /plugin install ruflo-core@ruflo

3. /plugin install ruflo-console@ruflo

4. /plugin install ruflo-mods@ruflo

5. /reload-plugins

6. /ruflo


成功の目安: Claude Code上でプラグインが有効化され、/rufloコマンドを実行してコンソールやツールを利用できること

未確認: 具体的な商用利用におけるスケーラビリティや実運用での詳細なパフォーマンス数値


## 5. [stablyai/orca](https://github.com/stablyai/orca)

**概要:** Orcaは、複数のコーディングエージェント（Claude Code、Codexなど）を並行して実行・管理するためのAIオーケストレーターです。デスクトップ、モバイル、リモートランタイムに対応しており、複数のエージェントを独立したワークツリーで同時に動かすことができます。

- 言語: TypeScript
- 今週のスター: 9545
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- 独立したgitワークツリー上で複数のAIエージェントを並行して実行し、結果を比較してマージできる（根拠: Features）

- モバイルアプリを使用して、エージェントの作業完了の通知受け取りやスマホからのフォローアップ指示ができる（根拠: Features）

- Chromiumウィンドウ上のUI要素をクリックして、HTMLやCSS、切り抜きスクリーンショットをエージェントのプロンプトに送信できる（根拠: Features）


### 利用例

- 1つのプロンプトを複数のエージェントに同時に処理させ、最も優れた結果をマージする（README明記／根拠: Features）

- 外出先やデスクから離れた場所からでも、モバイル端末でAIエージェントの進捗監視や指示出しを行う（README明記／根拠: Features）

- アプリ内でGitHubのプルリクエストやIssue、プロジェクトボードを確認し、文脈を切り替えることなくワークツリーを開いてレビューする（README明記／根拠: Features）


### 最初に試すこと

Orcaデスクトップアプリをインストールして起動する

1. 公式サイト（onorca.dev/download）またはHomebrew（brew install --cask stablyai/orca/orca）などのパッケージマネージャーを使用してインストールする


成功の目安: Orcaデスクトップアプリが正常に起動すること

未確認: CONTRIBUTING.mdの詳細な開発手順／cloud/ディレクトリにあるリレーサーバーの具体的なセットアップ手順


## 6. [anomalyco/opencode](https://github.com/anomalyco/opencode)

**概要:** anomalyco/opencodeは、オープンソースのAIコーディングエージェントであり、ターミナルUIやデスクトップアプリを通じて開発作業やコードの探索を支援します。

- 言語: TypeScript
- 今週のスター: 6765
- ライセンス: MIT
- AI分析状態: ok（キャッシュ）

### できること

- buildエージェントによる開発向けのフルアクセスなコーディング作業（根拠: Agents）

- planエージェントによるコードの分析や読み取り専用の探索（根拠: Agents）

- Tabキーによるエージェント間の切り替え（根拠: Agents）


### 利用例

- 不慣れなコードベースの探索や変更の計画（README明記／根拠: Agents）

- 開発作業におけるフルアクセスなコーディング支援の利用（README明記／根拠: Agents）

- @generalを使用した複雑な検索や複数ステップのタスクの実行（README明記／根拠: Agents）


### 最初に試すこと

CLI環境でopencodeをインストールして使い始める

1. curl -fsSL https://opencode.ai/v2/install | bash


成功の目安: インストールスクリプトが正常に実行され、opencodeが利用可能になること

未確認: 詳細な設定方法やAIモデルのバックエンドに関する具体的な仕様／コントリビューション手順の細かいルール


## 7. [cursor/plugins](https://github.com/cursor/plugins)

**概要:** Cursor公式のプラグインおよびサードパーティ製プラグインを多数収録しているリポジトリです。各プラグインは独立したディレクトリとして管理され、それぞれにマニフェストファイルを含んでいます。

- 言語: TypeScript
- 今週のスター: 1946
- ライセンス: 不明
- AI分析状態: ok

### できること

- 開発ツール、生産性向上ツール、外部SaaS製品向けの公式Cursorプラグイン集を提供する（根拠: README冒頭）

- プラグインごとに個別のディレクトリと .cursor-plugin/plugin.json マニフェストを持つ（根拠: README冒頭）

- ルートディレクトリの .cursor-plugin/marketplace.json でプラグインのリストを管理する（根拠: Repository structure）


### 利用例

- 開発ツールやSaaS製品向けのプラグインを利用する（README明記／根拠: README冒頭）

- 新しいエージェントプラグインを構築および検証する（README明記／根拠: Plugins）

- リポジトリ構造に沿って独自のエージェントスキルやルールを追加・管理する（提案／根拠: Repository structure）


### 最初に試すこと

リポジトリの構造やプラグイン一覧を確認する

1. リポジトリのREADMEを開き、一覧から興味のあるプラグインを確認する

2. リポジトリ内の .cursor-plugin/marketplace.json および各プラグインディレクトリの構成を確認する


成功の目安: プラグインの一覧とリポジトリ構造が確認できること

未確認: 各プラグインの詳細なインストール手順や具体的なコマンド


## 8. [android/skills](https://github.com/android/skills)

**概要:** Android開発向けのAI最適化されたモジュール式指示とリソースを提供するリポジトリです。LLMが苦手とするユースケースやワークフローを対象としています。

- 言語: Kotlin
- 今週のスター: 1471
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


## 9. [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

**概要:** anthropic/knowledge-work-pluginsは、Claudeを専門業務特化型のアシスタントに変えるためのオープンソースプラグイン集です。Claude CoworkおよびClaude Codeで利用でき、スキル、コネクター、スラッシュコマンド、サブエージェントをバンドルしてタスクを効率化します。

- 言語: Python
- 今週のスター: 2625
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- ロール、チーム、企業に合わせた専門的なプラグイン（生産性向上、営業、カスタマーサポート、製品管理、マーケティング、法務、財務、データ分析、エンタープライズ検索、バイオ研究、プラグイン管理など11種類）を提供する。（根拠: Plugin Marketplace）

- MCPサーバーを介してSlack、Notion、Asana、Snowflakeなどの外部ツールやデータソースと接続する。（根拠: How Plugins Work）

- マークダウンとJSONによるファイルベースの構造を採用し、コードやインフラストラクチャなしでカスタムプラグインの作成や既存プラグインのカスタマイズができる。（根拠: Making Them Yours）


### 利用例

- 営業活動において、見込み客の調査、コールの準備、パイプラインの確認、アウトリーチの下書き、競合バトルカードの作成を行う。（README明記／根拠: Plugin Marketplace）

- 財務業務において、仕訳の準備、勘定科目の消込、財務諸表の作成、差異分析、決算管理、監査支援を行う。（README明記／根拠: Plugin Marketplace）

- データ分析において、クエリの記述、可視化、データセットの解釈、統計分析、ダッシュボードの構築を行う。（README明記／根拠: Plugin Marketplace）


### 最初に試すこと

Claude Codeを使用してマーケットプレイスを追加し、特定のプラグインをインストールする

1. claude plugin marketplace add anthropics/knowledge-work-plugins

2. claude plugin install sales@knowledge-work-plugins


成功の目安: 指定したプラグインがClaude Code環境に正常にインストールされること

未確認: プラグインごとの詳細な内部実装コードや個別のコネクター設定の全詳細


## 10. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを決定論的なMP4ビデオに変換するためのオープンソースフレームワークです。CLIを通じてローカルで使用できるほか、AIコーディングエージェントのスキルとしても活用できます。

- 言語: TypeScript
- 今週のスター: 5553
- ライセンス: Apache-2.0
- AI分析状態: ok

### できること

- HTMLとCSS、シーク可能なアニメーションを定義して決定論的なMP4ビデオにレンダリングする（根拠: How It Works）

- Claude CodeなどのAIコーディングエージェント向けにスキルを導入し、エージェント経由で動画制作を行える（根拠: Quick Start）

- CLIやカタログ機能を通じて、プレビュー、ローカル・クラウドレンダリング、再利用可能なブロックの追加ができる（根拠: HyperFrames Stack）


### 利用例

- 製品のローンチ動画や機能紹介アニメーションの作成（README明記／根拠: What You Can Build）

- アニメーション付きのコード差分やナレーション、字幕を含むPRウォークスルーの作成（README明記／根拠: What You Can Build）

- データビュジュアライゼーションやマップアニメーション、チャートレースの制作（README明記／根拠: What You Can Build）


### 最初に試すこと

CLIを使用して新しいビデオプロジェクトを初期化し、プレビューおよびレンダリングを行う

1. npx hyperframes init my-video

2. cd my-video

3. npx hyperframes preview

4. npx hyperframes render


成功の目安: ブラウザでのライブリロードによるプレビュー確認、およびMP4へのレンダリングが完了すること





## Zenn

- [MultiheadAttentionの高速経路がVRAMを18GB食っていた話](https://zenn.dev/genelab_999/articles/387bf151caf716) — GeneLab

- [リンクで確認した SNS のメール購読に、作り直さずに「解除の保護」を付ける](https://zenn.dev/sk8jp/articles/260e3c0fa07ed9) — YAZ

- [Laravel を IdP にして Ory Hydra で SSO を組み、PHP 5.6 のレガシーアプリも認証ブローカーで乗せる](https://zenn.dev/sprix_it/articles/464d97d1ebdbfd) — いけ

- [Gowin FPGAの配置配線オプションを実測比較 — ビルド時間とFmaxのバランス](https://zenn.dev/akiyukiokayasu/articles/66be017200e64e) — Akiyuki Okayasu

- [AIコードレビューの不合格率が51%→13%に。3モデル中2つは判定していなかった](https://zenn.dev/taka8823/articles/2df36d66844c15) — yuki takamura

- [webauthn-ruby をもう一回覗いてみた](https://zenn.dev/smartcamp/articles/22bde5829493e5) — 職人

- [「分担を見直したい」では動かなかった。チーム間の議論を変えた1枚の図](https://zenn.dev/shun0530/articles/32946ce85a536d) — shun

- [AI隆盛期に考える、情シス的セキュリティのあれこれ](https://zenn.dev/kinasato_mochi/articles/db662a5909ea19) — 鬼無里 餅衛門

- [eMudhraの中間CA証明書の秘密鍵を求めてみる](https://zenn.dev/herumi/articles/search_bad_emudhra_key) — herumi

- [[Flutter]main()を通らない起動ルートで初期化漏れした話（Android着信のヒヤリハット）](https://zenn.dev/lincwell_inc/articles/ab2a642ea8f6f0) — Take

- [Claude CodeやCodexで並列開発していたら、Macのストレージが残り8GBになったので掃除した](https://zenn.dev/yoshinani_dev/articles/0c17dec1c082a1) — ひょうどう

- [Rootless Dockerと学ぶSELinux【初心者向け】](https://zenn.dev/nexryai/articles/afb828d7dda6b7) — nexryai

- [厳選・セキュリティが心配ならClaude Codeにこの問いかけをコピペするべし20](https://zenn.dev/yuiseki/articles/54b01670841898) — yuiseki

- [脆弱性管理の仕組みを整えた](https://zenn.dev/dress_code/articles/be5550254695cd) — anizozina

- [【速報：2026/10/22 04:00】PHP2Shellの対応状況まとめ：PHP本体、Linux、レンタルサーバ、KUSANAGI](https://zenn.dev/tyamadadd/articles/c02a27af771dd2) — tyamadadd

- [仕組みを理解する動画を、Claude Codeに作らせると便利すぎる](https://zenn.dev/explaza/articles/c749042ecbe232) — musoukun

- [バイブコーディングを6週間続けたら、Mac の起動が20分かかるようになった](https://zenn.dev/singularity/articles/vibe-coding-mac-boot-20min) — Isamu

- [Oxlint + Oxfmt で規約をコード化するモノレポ運用](https://zenn.dev/reality_tech/articles/oxc-monorepo-20261006) — Toshiki Okazaki

- [Claude Code で CI 待ち時間を 18 分から 4 分台に短縮する【GitHub Actions】](https://zenn.dev/edash_tech_blog/articles/5b90aa33bd8d49) — iakito

- [AI時代、配布するPythonコードをどう守るか: 難読化の実験と判断軸](https://zenn.dev/pksha/articles/0f9c11d1daea2e) — 山本隼輔


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。