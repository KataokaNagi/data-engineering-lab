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

# 記事要約 『【深層学習】Attention - 全領域に応用され最高精度を叩き出す注意機構の仕組み【ディープラーニングの世界 vol. 24』

- https://www.youtube.com/watch?v=bPdyuIebXWM
- 20210702 AIcia
- 20210716参照

<!-- -------------------- -->

## Attention
- 特徴
    - Transformer、BERTの始祖
    - 変換対象との関連性を計算
    - 語順変化に強い
    - 30語以上の長文にも強い
    - 未知語（固有名詞）への対処が弱い
- システム
    - 前後に文脈を伝播（Annotation）
    - 意味ベクトル１つでなく、単語ごとに意味を付与
