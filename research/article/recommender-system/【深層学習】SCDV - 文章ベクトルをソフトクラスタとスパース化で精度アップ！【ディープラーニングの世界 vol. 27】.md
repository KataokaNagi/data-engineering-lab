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

# 記事要約 『【深層学習】SCDV - 文章ベクトルをソフトクラスタとスパース化で精度アップ！【ディープラーニングの世界 vol. 27】』

- https://www.youtube.com/watch?v=gnnnB3gd_0U&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR&index=7
- 20210611 AIcia
- 20210716参照

<!-- -------------------- -->

## SCDV
- Sparse document vector
- 1単語に1ベクトルではない
    - ベクトルが足されて中和されない
        - ソフトクラスタリング
    - 単のの複数の意味を解釈
    - 1つの文章に複数の話題
    - 文脈を活かしてスパース化される
    - 意味が混ざりにくい
        - 足す重みがクラスタで変化
    - Sparse
        - 次元の呪いの回避
            - 60万次元あたりが60次元で済む
        - SVMが動く
        - 軽量
    - 高速
        - 従来: LDA O(V^2NT)
        - SCDV: GMM O(VNT^2)
            - 単語数、文章数、トピック数
