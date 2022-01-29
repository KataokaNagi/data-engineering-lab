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

# 論文要約 『Neural Collaborative with Sentence BERT for News Recommender System』

- [1]B. JuartoとA. S. Girsang, 「Neural Collaborative with Sentence BERT for News Recommender System」, JOIV : International Journal on Informatics Visualization, vol. 5, no. 4, Art. no. 4, 12月 2021, doi: 10.30630/joiv.5.4.678.
- 20220128参照
- 学部と修士の研究
    - そんな感じがする


<!-- -------------------- -->

## 概要
- 推薦システム
    - ニュースを容易に選択できる
    - 協調フィルタリング
    - ニューラル協調フィルタリング
        - 通常
        - ニュース内容の類似性をユーザに推薦してしまう欠点
            - ニュースのタイトルや内容など
            - ？？
    - SBERTを用いたニューラル協調フィルタリング
        - 文埋め込み
            - アイテムID、ユーザID、ニュースカテゴリとのニューラル協調に利用
    - Microsoftニュースデータセット
        - 50,000人のユーザー
        - 51,282のニュース
        - 5,475,542回のユーザーとニュースのインタラクション
    - 精度，再現率，ROC曲線
        - ユーザによるニュースのクリックを予測
    - leave one out 法によるヒット率
    - 評価の結果
        - 精度99.14%
        - 再現率92.48%
        - f1スコア95.69%
        - ROCスコア98%
    - ヒット率@10
        - 50エポック目
        - 文BERTを用いたニューラル協調処理のヒット率は74%
        - ニューラル協調フィルタリング（NCF）より良好
        - ニュースカテゴリを用いたNCFより良好

<!-- -------------------- -->

## 図表
- SBERTのモデルアーキテクチャ
- モデルの比較
- SBERTとNNの融合
    - SBERTの埋め込みをNNに用いてるだけ
- SBERTとNNの融合2
    - 出力は2ノード
        - クリック
        - ノットクリック
- パラメータの表
- 正確度、精度、再現性、F1スコア、ROCの学習・評価ステップ 
- 図5 ヒット率10%の場合の学習・評価ステップ 
- 混同行列の説明
- 予測の例
- モデルの結果
- RATIO@10
    - NCF+SBERTが一番高い

<!-- -------------------- -->

## はじめに
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

<!-- -------------------- -->

## おわりに
- ACCなどは変わらず
- @10は優れている
- ファインチューニングが必要

### 
- 

### 
- 

### 
- 

<!-- -------------------- -->

## 片岡所感
- 

<!-- -------------------- -->

## 重要ピックアップ
- 
