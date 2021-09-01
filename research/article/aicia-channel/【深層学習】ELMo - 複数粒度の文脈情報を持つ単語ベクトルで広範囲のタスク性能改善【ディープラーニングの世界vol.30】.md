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

# 記事要約 『【深層学習】ELMo - 複数粒度の文脈情報を持つ単語ベクトルで広範囲のタスク性能改善【ディープラーニングの世界vol.30】』

- https://www.youtube.com/watch?v=hMrOcH5dcGM&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR&index=11
- 20210716
- 20210901参照

<!-- -------------------- -->

## 概要
- Embeddings from Language Models
    - 2017
    - 埋め込み
    - 文脈を加味

<!-- -------------------- -->

## モデルと学習
- forward LM と backward LMの両方
    - 前後を加味して単語を予測
- 2層のLSTM
    - 2層目にはResidual connection
        - 双方向
- 最後にSoftmax
- 使い方
    - 既存モデルの埋め込みにconcatenate
        - 縦ベクトルの下に追加
    - ファインチューニング
    - モデルの各段階のベクトルの線形和っぽい形
        - 様々な粒度の情報を加味
