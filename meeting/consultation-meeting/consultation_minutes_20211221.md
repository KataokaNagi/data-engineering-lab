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

# 相談会 20211221

- そのままで4と13エポックで
- 30文→100文でチェック

- バッチサイズが小さすぎる
    - 大きくすると計算時間が長くなる
    - 特別な特徴ばかりを見てしまう
- 鞍点で止まらないように

- weightのコードを見る

- Eばかり
    - 過学習？
- エポック数が少ないときに何度かゼロになっている
    - ゼロにかなり近い→過学習


- Transformerは重みが多い
    - 過学習が起こりやすい
    - 全ての重みに誤差逆伝播はなぁ

- NN数層
    - ドロップアウトなどだけ悩めばよい
    - 若干古いが
    - SimpleTransformersのライブラリを真似て実装

- バッチサイズの決め方
    - 4000文の場合
        - 16文なのか
        - 16バッチなのか
        - まず1/10
            - 無根拠
        - 1/100はだめ
        - 1/3
        - 1/5

- SGD 汎化しやすい
- Adam 収束しやすい

- 8割2割でなく交差でやってみる
- サイキットラーン
