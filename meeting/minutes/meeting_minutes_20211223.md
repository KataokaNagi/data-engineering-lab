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

# 報告会 議事録 2021年12月23日

## 報告

### 片岡
- 1列に01ラベルを付けているならば、交差エントロピーではなく最小二乗法
    - num_label=1
    - weightは交差エントロピー用
    - 最小二乗
    - appendを2次元にして交差エントロピーにするのもあり
- 標準出力に最後のバッチを表示
    - 1エポック内でLossがあまり変化していない前提、一般論がある
    - でも今回は変動している
- Transformerごと学習
    - エポック数が少ないと、Transformer部分は事前学習できてもNN部分が学習できていない
- 本の転移学習のパートを読むと良い
    - 上層だけ学習しているのを確認
    - でもSimpleTransformersは全体を学習してしまっている
        - 転移学習の旨味を活かせていない可能性
    - 有りものでできるならそれでよいが
        - どこかで見切って自作
        - 最後のタスクを決めて見切る
- runningもevalも減るのが健全
    - 今回
        - runningが単調減少
        - evalが単調増加
            - 見切る基準
        - 典型的な過学習
- 片岡「2層という数の根拠を考えておきたい」
    - 2層はある意味結果が出ている
    - 3-4層
    - エポックの数
    - 2層は少ない気がする（主観）
- まとめ
    - 見切る
    - パチンコと一緒
    - 判断理由を付けて見切る
        - 論文にも書ける

### 亀川
- アンケートの添削
    - 違和感の定義
    - 違和感のレベルだけ聞くと、摂動以外の部分について回答してしまう可能性
        - 格子にふって回答させるのもあり
        - ひとつのバイアスになってしまう
        - 自由回答で分析するのもよい
- 既存の論文の評価
    - 人間向けではなく、機械向けに騙すのが多い
    - 順番の効果を減らす
    - 画像の効果を減らす
    - 自由記述

### 志田
- 

### 土屋
- 

### 平山
- 

### 増岡
- 

### 松本
- 

### モ
- 

### 原田
- 

## 気になったこと
- 

## 業務連絡
- 
