<!-- tex script for md -->
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
 MathJax.Hub.Config({
 tex2jax: {
 inlineMath: [['$', '$'] ],
 displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
 }
 });
</script>

# 週次報告書 2021年07月12日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 問題の明確化（報告済み）
- 手法の調査
    - オントロジー
    - トピックモデル
- 予備実験 △
    - トピック抽出

## 2. 実施内容

### 目次
- 2.1 手法の調査
    - 2.1.1 オントロジー（skip）
    - 2.1.2 LSI, PLSI, LDAの記事
    - 2.1.3 トピックモデルを用いた多言語ニュース推薦の論文
- 2.2 提案手法の検討
- 2.3 予備実験の計画

### 2.1 手法の調査

#### 2.1.1 オントロジー（skip）
前回読みかけていた論文に目を通した。

オントロジーには、異言語間の同音異義語に強くなるなどの利点がある。

論文では、同一の地名などが推薦できるよう、Concept（ニュースタイトルの名詞）にアノテーションし、それ専用のオントロジーのクラスを作成していた。

オントロジー以外の推薦に応用可能なツールとして、ニュースから情報抽出するGATEや、アノテーションのためのGazetterr・ANNIEは夏に確認する必要がある。

[1]S. N. FerdousとM. M. Ali, 「A semantic content based recommendation system for cross-lingual news」, 2017 IEEE International Conference on Imaging, Vision Pattern Recognition (icIVPR), 2月 2017, pp. 1–6. doi: 10.1109/ICIVPR.2017.7890880.

#### 2.1.2 LSI, PLSI, LDAの記事
類義語の次元圧縮を行うトピックモデルの手法として、LSI, PLSI, LDAについて学んだ。

<!-- LSIは文章行列Mの特異値分解$M = U \Sigma V^*$という形式で次元圧縮を試みる。このとき、**各単語のトピックとしての重要度が特異値として算出され**、後述の提案手法に応用しやすいと考えた。ただし、先生が仰ったように頻度ベースであるため、希少なニュースに対応できない可能性が高い。 -->

LDAは学習データのない新規データに利用可能とのことで、ニュース推薦に適していると考えた。

[1] 「【入門】トピックモデルとは？トピック分析の３つの手法を解説」. https://spjai.com/topic-model/ (参照 7月 10, 2021).

#### 2.1.3 トピックモデルを用いた多言語ニュース推薦の論文
トピックモデルとしてLDAを用いた論文の一部に目を通した。

類似した文章を推薦しており、私が目指す多様性は考えられていない。また、抄録を使用しており、これにニュースの何を使用するかが肝となりそうである（詳細は読めていない）。

ラベルの推薦が可能なため、新しい希少なデータにも対応しやすいと考えた。

[1]M.-J. Tian, Z.-H. HuangとR.-Y. Cui, 「Labeled Bilingual Topic Model for Cross-Lingual Text Classification and Label Recommendation」, 2018 5th International Conference on Information Science and Control Engineering (ICISCE), 7月 2018, pp. 285–289. doi: 10.1109/ICISCE.2018.00067.

### 2.2 提案手法の検討
LDAでは、既知の単語列の下でのトピック列の条件付確率$P(z_i=k|\vec{z_{\neg}i},\vec{w})$ が得られる。つまり、ある記事に対して、複数のトピックラベルのそれぞれの該当度が得られると考える。

この該当度を基に、以前図に示した「ニュース事象のより多くのトピックを網羅する和集合の記事群」を推薦することを考える。

推薦したい記事は、以下の条件を満たす

![](./img/topic-labels-comparing.png)

このとき推薦されるべき記事は、入力記事のベクトルとのコサイン類似度が中程度になるものだと考える。

また、ある閾値以下の小さい要素は0に置き換えることで、推薦されるべきかの差が明確化すると考える。加えて、記事タイトルの名詞や固有名詞の重みを増やすのも有効だと考える。さらに、希少なデータを重要視するため、他のベクトルには殆ど含まれないトピックは重みを大きくするとよいと考える。

このような工夫や条件を追加し、より適切な定式化を行う研究ができるとよい。

ただしこの手法では、題目の「クラスタ」を用いたといえるかがあやしい。

### 2.3 予備実験の計画
金曜日に紹介した実験手順を以下に引用する。この手順を具体的な内容で考える。

- ~~社会~~ 技術的問題点の手法
    1. 世界の記事を翻訳する
    2. **全記事で、共通する「出来事・登場人物を指す名詞」が多い記事群を抽出**
        - 固有名詞
        - 固有名詞自体にtf-idf的手法
    3. 抽出した記事群のうち、共通しない固有名詞を含む文章の主張を抽出
    4. 主語、主張のセットで重複しないものを抽出
    5. **何らかの重要度でランク付け**
        - どの記事でも取り上げられている人物・組織は重要
        - 意見の類似度の全体との離れ様？

新規性となる手順2，5は考えず、他の手順のみを簡易化して予備実験する。
1. CNNのニュースと、YahooニュースをDeepLで変換した記事本文を用意する
    - 各カテゴリの見出し30ずつ＋以下の記事
        - 意外な推薦を見つけるため
    - ファイザー, 世界の接種率
    - ファイザー, 世界の3回目摂取
    - モデルナ, 世界の7月の接種率
    - モデルナ, 世界の7月の接種率
        - 入力記事
    - ワクチンだと話題がブレそう？
    - 社名はグレーだが、医療論文で取り上げられるのでセーフ？
2. LDAで類似度順に並べる


## 3. 次回までに実施予定であること
- 月
    - 報告会の振り返り
    - スライド作成
- 火-水
    - 予備実験
    - 概要書作成
- 木-日
    - 手法調査
    - 概要書修正
    - スライド作成
    - 報告資料作成

## 4. 雑多メモ

### 概要チェック前
- 階層的クラスタリングの是非
    - 単なるUI表示はユーザの行動に繋がらない
    - 階層の何に着目するのか
- オントロジーは固有名詞に弱いのでは
    - 錦織と大阪の区別がつかない
    - 新規性になりそう
    - 固有名詞だけで済むのか
        - 固有名詞は翻訳が難しい
        - オントロジーによる多言語の強化
    - 読みかけの論文では対応できている
        - タイトルから抽出？
- オントロジーが抽象すぎて、似すぎないトピックを推薦する
    - 固有名詞をどう組み込むかが肝
    - オントロジーの関係に重要度が
- オントロジーのクラスタリング手法を詰める
- オントロジーで途中まで似ていて途中から急変する文を推薦
- トピック語が強い枝を残す
- 予備実験どうする
    - トピック抽出したい
    - オントロジーを眺めたい
        - いい急変具合がないか
        - ジャンルを変えてみる
    - 単純翻訳で推薦したい
    - 多種の言語の単純翻訳を見たい
- 多言語ニュース推薦 概要調査
    - 複数のモダリティを用いた多言語放送ニュースの新規性と冗長性の測定
- オントロジーとその他の手法の指標が異なり、比較が難しそう
- トピック
    - 文章量が伝えたい量
    - 話題性、質
    - 一般人が結婚しても興味ない
    - 新規性を感じる言葉
- SVOC

### 概要チェックを受けて

#### 相談内容
- 目的の迷子
- 調査を受けて
    - オントロジーの是非
    - 階層的クラスタリングの是非
    - 新規性は
        - 調査不足

#### メモ
- 社会問題の大和言葉化（被ってよい）
    - 同じ事象で異なる解釈の記事は数多く存在するが、同じ地域で偏った解釈の記事ばかりを読みがち
    - 多くの解釈を汲んだ上での知識吸収が、応用する上で人生の糧となる。記事の問題解決の近道。
        - 偏りの自覚を促したい
        - 中立である必要はない
        - 偏りの要因は「政治、経済、技術、文化」や当事者意識の有無による調査の深さ？
- 技術問題（定量可能）
    - 精度、時間、全く新しい何か
        - そのままでは適用できない
    - （世界の）同一トピックの記事の解釈の微妙なズレを端的に確認する手法が確立されていない（と仮定して要調査）
    - トピックとは
        - 議論・解釈の的となる唯1組の事象
            - SV(OC)（×手法）
            - SVOCの順でない可能性
            - 4W1Hはその肉付け
        - （参考）中心問題，題目，話題，話の種，主題，論題，テーマ，1つの文中で，その文が何について情報を伝えるのかを示す部分；多くの場合文頭に位置するか，日本語の「は」のような文法的な形式で示される
        - 新規性？
            - 社会的問題につながりにくい
    - 解釈
        - トピックの肉付け部分
        - 主語の違い、言い換えの仕方（×手法）
        - ニュースは誰かの解釈を中立に並べている
        - should
    - ズレの内容と幅の数値化（、可視化）（×手法）
    - 世界の記事は数が膨大
        - 極力軽く
        - 日々大量に更新
            - 追加に対応したクラスタリング
        - 検索は難しい
        - 前処理だけで行う必要
        - 世界に限らないのでは
- クラスタリング手法
    <!-- - ソフトクラスタリング後の分析？
    - 階層的クラスタリング
    - オリジナル -->
- この問題解決とトレードオフとなるものは何か
- ある同一の事象に関する様々な人の意見、主張、意図を抽出
    - 同じ事象に揃える必要
    - 同じ人また似た意見は省く
        - 同じ人かつ
    - （手法）多言語でできているのか
        - 日本の主張は「」で挟まれるなど
        - 明示的な言語の「」は外してAttention
            - クラスタではない？
- 代替手法
    - 専門家のコメントで異なる主張も取り入れられるのでは
        - 自動化で専門家のカバーできない範囲を網羅
        - 専門家が全記事を見ているわけではない
- 記事の壁を取り払う
    - 主語、主張のセットで重複しないものを列挙
    - ある重要度でランク付け
        - 意見の類似度が小さいほど推薦したい


### 相談会を受けて
- タイトル「**記事トピックのクラスタを用いた多言語ニュース推薦手法の提案**」
- 社会的問題点
    - 記者によって、ある出来事の要素のうち伝えるべきだと考える対象が異なる
    - 読者は、記事に書かれた一側面だけから出来事を理解した気になってしまう
    - この問題は世界の記事を見たときに顕著
        - 要因：文化などの違い
- 社会的問題点の手法
    1. 世界の記事を翻訳する
    2. 全記事で、共通する「出来事・登場人物を指す名詞」が多い記事群を抽出
        - 固有名詞
        - 固有名詞自体にtf-idf的手法
    3. 抽出した記事群のうち、共通しない固有名詞を含む文章の主張を抽出
    4. 主語、主張のセットで重複しないものを抽出
    5. 何らかの重要度でランク付け
        - どの記事でも取り上げられている人物・組織は重要
        - 意見の類似度の全体との離れ様？
    - これらをそのまま予備実験？
    - （自動化で専門家コメントがカバーできない範囲を網羅）
        - （専門家が全記事を見られるわけではない）
- 技術的問題点（定量）
    - 固有名詞の翻訳、利用が難しい＝抽出したい理想記事との類似度の精度が下がる
    - 大規模なデータに耐えうる速度
    - 日々大量の更新が可能なシステム
- 技術的問題点の手法
    - ...
- 別の社会問題手法の着眼点
    - 記事の壁を取り払う
        - 何の記事から引用したかは必要

### 報告会の議題
- 社会的問題、その手法、技術的問題（、その手法）を大和言葉に
    - まず図で抽象的に説明
    - 文章で説明
- 所感
    - 社会的問題に繋がる技術的問題が見当たらない
    - まだ具体的に踏み込めてなさそう
- 質問
    - 技術的問題点を見つけるコツ
        - まずは予備実験
        - 論文を読む
        - ニュースを眺める
        - 報告会の議事録を見る
        - 友人と話す
    - トピックモデル繋がるか

### 日曜
- Poly-linguralという新ワード
- ニュースの固有名詞の特徴
    - 使われ方は同じ
        - 単語埋め込みで検出して統合（次元圧縮）
- 先行研究
    - LSI
    - 単語埋め込み
    - ニュースのトピックモデルで固有名詞は考慮されていない