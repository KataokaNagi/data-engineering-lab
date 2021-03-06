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

# 週次報告書 2021年04月19日
AL18036 片岡 凪

## 今回の報告会までに実施する予定だったこと
- 報告書
- 論文調査
    - XAIの応用技術？
        - 何を説明したいか
        - 具体的なモデルの具体的なXAI手法
    - タグ分類？
    - その他、趣味や既習事項に関連するもの
    - これまでの報告会のメモを眺めてみる
- hand's on ML
- 「研究で求められること」に目を通す
- 応用情報技術者試験対策

## 実施内容

### 「研究で求められること」を読んで
研究で求められる各項目について、自分の考える社会の問題は何か、またそれをデータ工学でどう解決できるかを少しだけ考えた。今週ももう少し考えてみたい。
- 社会的意義があること
    - **Webサービスのサジェスト機能で、良い作品ばかりがサジェストされ、新規参入者が成長しない問題**
        - データ工学での解決がなかなか思いつかない。。。
        - 作品の範囲を狭めるべき。画像？画像の何？
        - **アキネーターの改良？**
            - **一部の似ている特徴量はそのままに、一部の特徴量を大きく離してみたり**
                - 具体案はそのうち思いつくかも
    - **パーソナルファブリケーション**
        - 非専門家が扱えるように専門家が専門技術を加工
        - データ工学では？
            - **可視化**
            - **モデルやパラメータの選択の自動化**
- 技術的意義があること
    - 多少論文の粗が見えたりはするが、他の誰かが既に説明していそうで恐い
    - リサーチあるのみ

### 論文1. 「XAI(eXplainable AI)技術の研究動向」
本稿を選んだ経緯は、相談会で述べた通りである。XAIに関する日本の論文をざっと眺めていたところ、前回のレビュー論文よりも**新しいレビュー論文であり**、かつキーワードとして**未知の単語**「Shapley値」と「Influence Function」が含まれていたため、関心を持った。  
  
内容としては、XAIの分類のうち半分を軽く紹介した後に、分類を深く掘り下げた「Shapley値」と「Influence Function」について導出方法から解説されている。論文を手に取ったときに全体を流し読みし、「Shapley値」と「Influence Function」について掘り下げることはわかっていたが、タイトルから想像ができないほど範囲の狭い技術であった。私が論文を執筆する際には、タイトル詐欺には気を付けようと考えさせられた。  
  
「Shapley値」も「Influence Function」も、問題の定式化までは理解できたが、その問題を数学的にどう解いたかは説明がされておらず、解の複雑さからして学部の1年間では手に負えない数学を用いられている印象を受けた。しかしながら、**数式を用いたXAIの切り口の一例として以下のパターンが掴め**、大変参考になった。  
- 問題の定式化
- 式の要件を列挙
- 要件を全て満たす式を導出
  
この他にXAIの切り口がないか、またこの2つの手法のような説明手法で何を説明したいかをよく考えた上、研究テーマを絞っていきたい。

### 論文2. 「Doctor XAI: an ontology-based approach to black-box sequential data classification explanations」
XAIの論文のうち、2020年以降の発展途上の分野として、既知のモデルを具体的に説明可能にしようとしているものがないかを調査した。検索をかけたところ、以前調査したオントロジーを用いたXAI技術があったので読んでみることにした（**書いていて気がついたが、既知のモデルの説明でなく、既知の手法を用いた複数のモデルの説明であった**。。。）
  
医療系なのでデータの取り扱いが難しそうに思えたが、「まとめ」を見るに、ブラックボックスに依存しないためにオンラインマーケットバスケット分析など広い分野で活用できる技術である。
  
## 次回までに実施予定であること
- 報告書
- 論文調査
    - XAIの応用技術？
        - 何を説明したいか
        - 具体的なモデルの具体的なXAI手法
    - タグ分類？
    - その他、趣味や既習事項に関連するもの
    - これまでの報告会のメモを眺めてみる
- hand's on ML
    - スライド作成
