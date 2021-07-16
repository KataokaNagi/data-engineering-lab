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

# 記事要約 『【深層学習】Transformer - Multi-Head Attentionを理解してやろうじゃないの【ディープラーニングの世界vol.28】』

- https://www.youtube.com/watch?v=50XvMaWhiTY&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR&index=10
- 20210702 AIcia
- 20210716参照

<!-- -------------------- -->

## Transformer
- 特徴
    - 注目すべき情報を選べる
    - 並列処理との相性が良い
    - RNNなし、Attentionのみ
    - 次の単語の確率の蓄積
- システム
    - 埋め込みはサブワード
        - バイトペアエンコーディング
        - 両言語の共通辞書
    - 単語位置はポジショナルエンコーディング
        - 三角関数
    - Transformer論文は行ベクトルを使うので注意
    - Scaled dot-product attention
    - Attention(Q,K,V)
        - KeyとValueをどう学習するか
    - $Multi-Head(Q,K,V) = concat(head_i)W^O$
        - concatは行ベクトルの連結
        - $head_i = Attention(QW_i^Q, KW_i^Q, VW_i^V)$
    - 8個のAttentionに入力するため、Xの横ベクトルの次元をWで8分の1に
    - DecoderははV, KはEncoderから、Qは翻訳先言語から
        - 英で注目部位を決めて独を入力
- 使い方
    - XのそれぞれにWを掛けてQ,K,Vを作成
        - 基底を回す？
    - Q:Xのどの部分を処理するか
    - K:Xの注目の仕方を決める
        - 同じXをひねってぶつける
    - V:Xを回して出力の様子を調整する
- Masked Multi-Head Attention
    - Decoderで後ろの単語の情報から前の単語への流入をブロック
    - 文章生成の自然な理屈
    - BERTでは不要に
