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

# 論文要約 『Doctor XAI: an ontology-based approach to black-box sequential data classification explanations』
- [1]C. Panigutti, A. PerottiとD. Pedreschi, 「Doctor XAI: an ontology-based approach to black-box sequential data classification explanations」, Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency, New York, NY, USA, 1月 2020, pp. 629–639, doi: 10.1145/3351095.3372855.- 

<!-- -------------------- -->

## 概要
- モデルにとらわれない説明可能性手法
    - XAI博士、 マルチラベル、シーケンシャル、オントロジーにリンクされたデータを処理できるもの
- 病歴を入力
- 次の訪問を予測するマルチラベル分類器
- データの時間的次元と医療オントロジーにエンコードされたドメイン知識を活用
- マイニングされた説明の品質がどのように向上するかを示す

<!-- -------------------- -->

## はじめに
- 電子カルテ
    - ノイズが多い
    - 断片的
    - 高次元
    - 非線形関係
- MLの医療応用
    - 表現学習
    - 転帰予測？（outcome prediction）
    - 新たなプロトタイプの発見
- ブラックボックスモデルは、データの偏りや敵対的サンプルで揺らぐ
    - 法律的に根拠が必要
- 新規性
    - シーケンシャルデータやオントロジーリンクされたデータの分類に適用できる初めての不可知論的なXAI技術
        - オントロジーに基づいてブラックボックスモデルでラベル付け
        - 決定木用にデータを加工し、逐次性を持たせる
        - ラベル付けされた患者で決定木の学習
        - 説明として決定ルールを抽出
- 論文の目標
    - 我々は、逐次データ分類の説明問題に取り組むことができる不可知論的（依存しない）説明可能性技術を提案する。
    - 医療オントロジーに存在する意味的な情報を利用することで、説明の質が向上することを示す。
- 比較
    - オントロジーの生む

<!-- -------------------- -->

## 関連研究

### Doctor AI
- Gated Recurrent Units (GRU)を用いたRecurrent Neural Network (RNN)
- 患者の次回の診察時間、診断、薬の順番を予測
- Sutter Health Palo Alto Medical FoundationのEHRsデータベースの260,000人の患者でモデルを学習
- 手順
    - 多変量ベクトルを低次元に投影
    - RNN
    - Softmax
- 評価
    - recall@nでn = 10, 20, 30
- 解釈可能性の最近の不十分なアプローチ
    - 逐次モデルにAttention、Attention-waitを説明の一形態
    - 内部動作の理解に焦点
- ブラックボックスに依存しないアプローチ
    - LIME
        - 常により単純で、より相互参照可能なモデルによって局所的に近似することができる
        - 疎な線形モデルの重みのセット
    - SHAP
        - ゲーム理論
        - 局所的な特徴の重要性を評価
    - ANCHORS
        - multi-armed bandit（盗賊）アプローチで問題を定式化

### MLでのオントロジーの活用
- 10％性能向上
- 一致が多いデータは類似度を過大評価するので注意

<!-- -------------------- -->

## 方法
- ブラックボックスの局所的な振る舞い・決定境界を訓練
- neighbourhood
    - 説明したいインスタンスxの周辺の合成インスタンスのセット
- 手順
    - neigbourhoodをブラックボックスでラベル付け
    - neigbourhood上で解釈可能なモデルを学習
    - 象徴的なルールを出力

### 説明のパイプライン
- 

### 
- 

### 
- 

<!-- -------------------- -->

## 
- 

### 
- 

### 
- 

### 
- 

<!-- -------------------- -->

## 
- 

### 
- 

### 
- 

### 
- 

