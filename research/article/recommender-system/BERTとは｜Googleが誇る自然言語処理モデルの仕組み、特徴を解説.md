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

# 記事要約 『BERTとは｜Googleが誇る自然言語処理モデルの仕組み、特徴を解説』

- https://ledge.ai/bert/
- 2020 Ledge.ai
- 20210716参照

## BERT
- NLPなら何でもできる？
- Masked Language Model
    - 確率でマスク
- Next Sentence Prediction
    - 文が隣りあっているかの学習
- 可能タスク
    - MNLI：含意関係の分類タスク
    - QQP：質問内容が同じであるかを分類するタスク
    - QNLI：質問と文が与えられ文が質問の答えになるか当てる分類タスク
    - SST-2：映画のレビューに対する感情分析タスク
    - CoLA：文の文法性判断を行う分類タスク
    - STS-B：2文の類似度を5段階で評価する分類タスク
    - MRPC：ニュースに含まれる2文の意味が等しいかを当てる分類タスク
    - RTE：小規模な含意関係の分類タスク
