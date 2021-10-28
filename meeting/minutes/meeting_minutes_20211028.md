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

# 報告会 議事録 2021年10月28日

## 報告

### 片岡
- BERTの類似度の平均とは
- GPUによる正規表現表示の高速化
    - ストリームエディター
    - sed
        - 学習コストが低い
    - awk
    - 正規表現スクリプトが残せる
    - パイプ処理
- 省略のピリオド
    - 文末のピリオドの後は\s大文字
    - BERTでDetection
        - 少し大変
    - (?=)(?=)
    - 文末人名コンマの例外
    - 自分で辞書を作ってしまう
    - BERTに必要な可能性があるため、#などに変換する
- ピリオド除去が一般化できないか

### 亀川
- 

### 志田
- 

### 土屋
- 

### 平山
- python独特のデバッグのしにくさに注意

### 増岡
- 

### 松本
- 文の類似度と単語の類似度では分布範囲が異なる可能性
- scibert

### モ
- 

### 原田
- 

## 気になったこと
- 

## 業務連絡
- 11/3, 5の報告会、相談会は無し（芝祭休暇）
- GPUを挿す必要がある人は早めに報告してください
    - 自分で挿した3人以外は基本挿さっていないか、学習に- 不向きなGPUが挿さっています
            - lspci | grep VGA でGPUの品名が確認できます
        - 研究室に挿していないGPUが2つあります
        - 必要があれば買い足します
