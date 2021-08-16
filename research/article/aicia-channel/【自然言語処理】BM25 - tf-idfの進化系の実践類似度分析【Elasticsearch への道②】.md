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

# 記事要約 『【自然言語処理】BM25 - tf-idfの進化系の実践類似度分析【Elasticsearch への道②】』

- https://www.youtube.com/watch?v=_HSOX0oh2ns&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR&index=2
- 20201211
- 20210816参照

- tf-idfのtfを拡張
- 検索クエリq = {q_1, ...,q_n}
- qとdのマッチ度で並べる
    - $$ score(q, d) = \sum_i idf(q_i) \frac{(k_1 + 1) f(q_i, d)}{f(q_i, d) + k_1(1 - b + b \frac{\sharp d}{avgdl} )}$$
    - $$ k_1 > 0 $$
        - 1.2が多い
        - scoreの上限の調節
    - $$ |b| \geq 1 $$
        - 0.75が多い
        - BM25の罰則の強さ
    - $$ \sharp d$$
        - 文章dの単語数
    - avgdl
        - average of document length
    - f
        - 文章d中の単語q_iの量
        - ElasticSearchなどではルートを取ることも
- 意味
    - $$ \frac{\sharp d}{avgdl} $$
        - 文書うdの相対的な長さ
    - d = avgdlのとき
        - $$ score = \frac{(k_1 + 1) f}{f + k_1} $$
        - fが増えるとk_1 + 1に漸近
    - $$ (1 - b + b \frac{\sharp d}{avgdl} ) $$
        - $　\frac{\sharp d}{avgdl}　$と1を1:(1-b)で配合
        - 文章が相対的に長さに比例
        - 単語が頻出でも文章が長ければ大きくしない
        - 極限値は保持
