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

# 記事要約 『【自然言語処理】tf-idf 単語の情報量を加味した類似度分析【Elasticsearch への道①】』

- https://www.youtube.com/watch?v=nsEbfO3U2pY&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR
- 20201204
- 20210816参照

- term frequency - inverse document freqency
- 頻度とレア度に重み
    - 数でなく割合
- シャープは「ナンバーサイン」で個数を表す
- 定義
    - $$ tf-idf = tf * idf $$
    - $$ tf = \frac{\sharp ~of~ t \in d}{\sharp d} $$
    - $$ idf = \ln{\frac{\sharp D}{\{d \in D | t \in d}\}} $$
- log(1/確率)は情報量