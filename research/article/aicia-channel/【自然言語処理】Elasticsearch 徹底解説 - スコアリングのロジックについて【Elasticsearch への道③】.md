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

# 記事要約 『【自然言語処理】Elasticsearch 徹底解説 - スコアリングのロジックについて【Elasticsearch への道③】』

- https://www.youtube.com/watch?v=V7WVdlUSOco&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR&index=3
- 20201218
- 20210816参照

- Lucene's Practical Scoring function
    - 検索で有名なElastic Searchの内部アルゴリズム
    - いい感じの検索結果になるtf-idf
- $queryNorm(q) \times coord(q, d) \times \sum_i{tf(q_i, d) \times idf(q_i)^2 \times q_i.getBoost() \times norm(q_i, d)}$
    - $queryNorm(q) = \frac{1}{\sqrt{\sum_i idf(q_i)^2}} \sum_i idf(q_i) \times tf-idf(q_i, d))$
        - レア単語を異なるqueryで比較可能に
    - $getBoost()$
        - 調節可能な検索のボーナス
            - 本文よりタイトル
    - $norm(q_i, d) = \frac{1}{\sqrt{\sharp d}} \times boost(q_i, d)$
        - boost(q_i, d)は非推奨
            - DBのindexによるボーナスで、更新に弱い
            - 1とする？
        - ゼロ除算を防ぐために $\sharp d + 1$ とすることも
            - 長く単語の多い文章への罰則
        - $tf(q_i, d) \times norm(q_i, d) \coloneq \sqrt{ふつうのtf-idf}$ としていることに注意
    - $coord(q, d) = \frac{\sharp \{ i | 1 \geq i \geq n, q_i \in d \}}{\sharp q}$
        - クエリの中で文章dに登場するものの割合
