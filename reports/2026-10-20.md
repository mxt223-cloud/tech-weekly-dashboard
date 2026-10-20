# Tech Daily — 2026-10-20

生成日時: 2026-10-20T09:33:09.000781+09:00  
AI分析: 10/10件成功（gemini-3.5-flash-lite）


## 1. [morluto/rea](https://github.com/morluto/rea)

**概要:** REAは、ネイティブバイナリ、アプリ、実行時の振る舞いなど、あらゆるものをAIエージェントとMCP（Model Context Protocol）を活用してリバースエンジニアリングするためのツールです。

- 言語: TypeScript
- 今週のスター: 201065
- ライセンス: MIT
- AI分析状態: ok

### できること

- ネイティブバイナリ、JavaScript/Electronアプリ、.NETアセンブリ、ウェブサイトなどの検査ツールにAIエージェントを接続します。（根拠: REA: Reverse Engineer Anything）

- Hopper、Ghidra、IDAなどのネイティブ解析エンジンや、内蔵の静的解析ツールを利用してコードを調査できます。（根拠: What you can analyze）

- 抽出したJavaScriptやElectronアプリのディレクトリまたはASARを対象に、モジュール、インポート、Electron境界とその証拠をJSON形式で取得できます。（根拠: Quick start）


### 利用例

- アプリ内の特定の機能がどのように動作しているかを調査し、その証拠を表示した上で、自分のプロジェクト向けに同様の機能を構築する。（README明記／根拠: REA: Reverse Engineer Anything）

- DX-Ballのサウンドパン計算処理を再構築し、元のx86のケースを通過させてコンパイルされた関数バイトを再現する。（README明記／根拠: Showcases）

- NotionのElectronクリップボードブリッジをトレースし、レンダラーのAPIからプリロードやIPCを経由してメインプロセスに至る流れを調査する。（README明記／根拠: Showcases）


### 最初に試すこと

エージェントのセットアップを行い、REAを利用可能にする

1. npx rea-agents setup


成功の目安: エージェントを選択し、提案された変更を確認して承認することで、REAのMCPサーバーと対応するワークフロー手順が追加されること




## 2. [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

**概要:** anthropic/claude-plugins-official は、Claude Code向けの高品質なプラグインを集めた公式ディレクトリです。Anthropicが管理する内部プラグインと、コミュニティやパートナーによる外部プラグインを提供しています。

- 言語: Python
- 今週のスター: 5441
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


## 3. [storytold/artcraft](https://github.com/storytold/artcraft)

**概要:** ArtCraftは、アーティスト、デザイナー、映画制作のためのインタラクティブなAI画像および動画制作IDEです。2Dでの構成、3Dでのシーン配置、多彩なAIモデルの選択を組み合わせ、プロンプト入力を視覚的なクラフト作業へと変化させます。

- 言語: Rust
- 今週のスター: 13572
- ライセンス: Apache-2.0
- AI分析状態: ok（キャッシュ）

### できること

- 3D空間内での背景、前景、プロップのレイヤー合成による奥行きのある構成（根拠: Show, Don't Tell: Advanced Crafting Features）

- 画像を3Dメッシュオブジェクトへ変換し、正確な位置調整や回転、フレーミングが可能（根拠: Show, Don't Tell: Advanced Crafting Features）

- テキストプロンプトからの画像生成および、描画・マスク・インペインティングを活用したキャンバス画像編集（根拠: Quick and Easy Prompting）


### 利用例

- 仮想の登場人物を一定の環境に配置し、同一の部屋で複数ショットを計画する（README明記／根拠: Show, Don't Tell: Advanced Crafting Features）

- 3Dアセットキットを組み合わせて、カメラアングルやオブジェクト配置、奥行きを制御するシーンブロッキングを行う（README明記／根拠: Show, Don't Tell: Advanced Crafting Features）

- 選択した動画モデルと生成コントロールを使用して画像をアニメーション化し、動画を作成する（README明記／根拠: Quick and Easy Prompting）


### 最初に試すこと

アプリケーションのダウンロードまたはソースからのビルドを行い、ArtCraftを起動して使い始める

1. 公式サイトやGitHub ReleasesからWindowsおよびmacOS向けの安定版をダウンロードしてインストールするか、_docs/dev_setup.mdを参照してソースからビルドする


成功の目安: ArtCraftが手元の環境で起動し、IDEインターフェースを利用できるようになること

未確認: 具体的なインストールコマンドや実行コマンドがREADME内に記載されていないため、CLI上での操作手順は不明です。


## 4. [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)

**概要:** ai-job-searchは、Claude Codeを基盤として自身のPC上で動作するAI求職・応募フレームワークです。求人情報の評価、CV（履歴書）の最適化、カバーレターの作成、面接対策を自動化します。

- 言語: Python
- 今週のスター: 9073
- ライセンス: MIT
- AI分析状態: ok

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


## 5. [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5)

**概要:** AnyPS5は、PS5の実行ファイルをLinuxおよびWindows向けに自動で移植するためのツールです。エミュレーションや独立したランタイムプロセスを使用せず、ネイティブ形式への変換やシステムライブラリの実装を行います。

- 言語: C++
- 今週のスター: 12389
- ライセンス: GPL-2.0
- AI分析状態: ok（キャッシュ）

### できること

- PS5の実行ファイルをLinuxおよびWindows向けに自動移植するリリンカーを含みます。（根拠: About）

- macOS（Appleシリコンを含む）でリリンカーのみのビルドを実行可能です。（根拠: About）

- SDLマッピングされたゲームコントローラー（アナログスティックやトリガーを含む）をサポートし、キーボードとマウスは設定ファイルで構成可能です。（根拠: Input mapping）


### 利用例

- PS5の実行ファイルをLinuxやWindowsのネイティブ形式に変換する。（README明記／根拠: About）

- デバイス上でファイルを処理できるWebコンバーターを使用する。（README明記／根拠: About）

- ゲームコントローラーやキーボード・マウスの入力マッピングを設定して操作する。（README明記／根拠: Input mapping）


### 最初に試すこと

Webコンバーターを利用してファイルを処理する

1. Webコンバーターのページにアクセスする

2. ファイルがデバイス内に留まることを確認して変換作業を行う


成功の目安: ブラウザ上でコンバーター機能を利用できること

未確認: 具体的なコマンドライン引数やインストールコマンド


## 6. [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

**概要:** Ghidraは、アメリカ国家安全保障局（NSA）が開発したソフトウェアリバースエンジニアリング（SRE）フレームワークです。コンパイルされたコードの解析を行うための逆アセンブル、アセンブル、逆コンパイル、グラフ化、スクリプト実行などの高度なツールを備えています。

- 言語: Java
- 今週のスター: 7152
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


## 7. [mksglu/context-mode](https://github.com/mksglu/context-mode)

**概要:** Context Modeは、AIコーディングエージェントのコンテキストウィンドウを最適化するためのMCPサーバーです。ツール出力をサンドボックス化して削減し、SQLiteによるセッションメモリの永続化、コード実行によるコンテキスト節約、そして17のプラットフォームにわたるセキュリティ権限の強制を行います。

- 言語: TypeScript
- 今週のスター: 4224
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


## 8. [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**概要:** HyperFramesは、HTML、CSS、メディア、シーク可能なアニメーションを確定的なMP4動画に変換するためのオープンソースフレームワークです。AIコーディングエージェントとの統合や、CLI、ホスト型オーサリングのレンダリングコアとしての利用を想定して設計されています。

- 言語: TypeScript
- 今週のスター: 5945
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




## 9. [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)

**概要:** cathrynlavery/diagram-design は、AIエージェント向けのエディトリアルな図解作成スキルです。影のない、HTMLとSVGが一体化したファイルとして、ブランドに合わせた45種類の図を出力します。

- 言語: HTML
- 今週のスター: 6638
- ライセンス: MIT
- AI分析状態: ok

### できること

- 1つの自己完結型HTMLおよびSVGファイルとして図を描画する（根拠: README冒頭）

- 45種類の図に対応している（根拠: README冒頭）

- ブランドのカラーパレットやフォントに合わせたデザインを作成できる（根拠: README冒頭）


### 利用例

- フロントエンド、バックエンド、データベース、Redisキャッシュを含むアプリの構成図を作成する（README明記／根拠: README冒頭）

- インパクトと工数を軸にしたQ2プロジェクトの象限図を作成する（README明記／根拠: README冒頭）

- 401エラー時のトークンリフレッシュを伴うベアラーコールのシーケンス図を作成する（README明記／根拠: README冒頭）


### 最初に試すこと

diagram-design スキルをインストールする

1. npx skills add cathrynlavery/diagram-design


成功の目安: スキルがエージェントホストに正常にインストールされること

未確認: Quickstartセクションのコードブロック以降の詳細な手順がREADME内で途切れているため確認できない


## 10. [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)

**概要:** Scientific Agent Skillsは、AIエージェントに生物学、化学、医学などの科学的タスクを実行させるための177件の検証済みスキルと100以上の科学データベースを提供するライブラリです。

- 言語: Python
- 今週のスター: 4355
- ライセンス: MIT
- AI分析状態: ok

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



## Zenn

- [対象が広い事業・プロダクトが刺さる気がしない](https://zenn.dev/fusa_bp/articles/broad-target-reaches-no-one) — fusa_bp

- [AIとコンテストに参加する](https://zenn.dev/attgm/articles/d28df25b88254a) — a2

- [普段使いのWindows PCでNodeのサーバーを常駐させて踏んだ罠](https://zenn.dev/matasuke_t/articles/bf784b79b29e86) — またすけ

- [Claude Codeの会話を55分放っておいたら、272,422トークンが13,522に圧縮されていました ― アイドル圧縮の観測](https://zenn.dev/ojisan_ai_lab/articles/claude-code-idle-compaction-20261019) — おじさんAIラボ

- [Kaigi on Rails 2026 感想 ＆ OSTで「ファットモデル」の議論をしたよ！](https://zenn.dev/progate/articles/b49c75fc6ab1ff) — 横江（よこえ）

- [AWS Lambda Web FunctionsでImpossible Location検知の課題をまとめて解決！ + 昨今の攻撃への有効性](https://zenn.dev/cscloud_blog/articles/f4ce99ffeb8ee3) — nishikawa

- [AI時代、配布するPythonコードをどう守るか: 難読化の実験と判断軸](https://zenn.dev/pksha/articles/0f9c11d1daea2e) — 山本隼輔

- [Claude Codeでプロンプトインジェクションに備える](https://zenn.dev/luxiar/articles/a341a2df29dcfe) — Suzu

- [クエリキーも型安全に変換するユーティリティを作った](https://zenn.dev/castingone_dev/articles/typesafe_query_key_converter) — ぬまさん

- [Claude Codeのステップごとのレビューを既定から外した理由](https://zenn.dev/ara_jlu/articles/per-task-review-dropped) — Ara;

- [【UMP】同意を外部SDKに反映する【Tenjinを例に】](https://zenn.dev/gameshitai/articles/f65544c1e5a7ea) — スナギモ

- [ドメインの境界を引くだけでは、業務はつながらない](https://zenn.dev/dress_code/articles/4a76f1b88e360d) — かわうそ

- [個人で使うClaude Codeの権限設定についてざっくり見直してみた](https://zenn.dev/takyshu98/articles/915702cf8c84f3) — takyshu98

- [「止まっている案件はどれ?」にSQLで答える。Snowflake Cortex AIで議事録を自動分類する](https://zenn.dev/fusic/articles/snowflake-ai-parse-document-minutes) — Y_uuu

- [リトルの法則で考える障害時のキャパシティプランニング](https://zenn.dev/rea9r/articles/littles-law-capacity-planning) — Takuya Akamatsu

- [生産計画を手を動かして学ぶ ― OSS の frePPLe で MRP・需要予測・CP-SAT まで](https://zenn.dev/rkawajiri/books/frepple-tutorial-ja) — Ryoma Kawajiri

- [ポートフォリオをVoidで作り直したので、Voidの来歴と中身を整理する](https://zenn.dev/nkzn/articles/my-first-void) — Nkzn

- [技術書を年に数冊しか買わない自分に、O'Reillyのサブスク年$150は割に合うか（ACM経由で契約してMCPまで）](https://zenn.dev/sonicmoov/articles/oreilly-subscription-acm) — m.okamura

- [ベクトルDBを使わない「階層ナビゲーション型RAG」を作って、ベクトルDB版RAGと比較してみた](https://zenn.dev/aiforall/articles/8e1803396534de) — nishina

- [有名 OSS が PR を閉じはじめた。何が起きていて、どう向き合うか](https://zenn.dev/hand_dot/articles/ecb391d4322330) — Kyohei Fukuda


> AI分析はREADMEの要約であり、実行可否・安全性・正確性を保証しません。