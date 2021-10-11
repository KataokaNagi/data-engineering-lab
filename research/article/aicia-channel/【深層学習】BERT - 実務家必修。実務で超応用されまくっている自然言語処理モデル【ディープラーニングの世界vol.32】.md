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

# 記事要約 『【深層学習】BERT - 実務家必修。実務で超応用されまくっている自然言語処理モデル【ディープラーニングの世界vol.32】』

- https://www.youtube.com/watch?v=IaTCGRL41_k&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR&index=12
- 20210730
- 20210901参照

<!-- -------------------- -->

## 概要
- Bidirectional Encoder Representations from Transformers（18）
- 高精度
    - Transformerのすごさ
    - 双方向性のすごさ
- 容易
    - pre-training, fine-tuning
        - 大量の教師付きデータを応用
        - 大量の計算資源を応用
            - 応用には数千のデータで高精度
- 応用例
    - Google検索（19）
    - LEGAL BERT（20）

<!-- -------------------- -->

## モデル
- TransformerのEncoderを利用
- 入力
    - 2文章
        - Q&Aなど
        - トークン（単語列）の組
            - CLS, t_1, ..., t_n, SEP, t_1', ..., t_m', SEP
                - classifier
                - separate
- 処理
    - embedding
        - 以下の和を入力
            - token embedding
            - segment embedding
                - 2文章のうちどちらなのか
            - position embedding
                - 何番目の単語か
- 出力
    - 入力と同数のベクトル
        - C, T_1, ..., T_N, T_SEP, T_1', ..., T_M', T_SEP

<!-- -------------------- -->

## Pre-Training
- Masked Language Model (Close Test)
    - 入力の15%をマスクし、その単語を予測
        - 文法や単語の意味の基礎理解
- Next Sentence Prediction
    - BERTへの入力を半分は連続する2文、半分はランダムに繋げた文として、どっちなのかを予測
        - CLS由来のCを予測
        - 文意と文脈を理解

<!-- -------------------- -->

## 使い方
- 文章単位のタスク
    - 入力
        - CLS 文 SEP SEP
            - 1文のみ
    - 出力
        - C T_1 ... T_N T_SEP T_SEP'
            - Cでタスクを解く
                - 文脈や文意が入っている
                    - 文章の意味ベクトル
- 単語単位のタスク (NER: Named Entity Recognition; 固有表現抽出)
    - 入力
        - CLS 文 SEP SEP
            - 1文のみ
    - 出力
        - C T_1 ... T_N T_SEP T_SEP'
            - T_1 ... T_N でタスクを解く
                - 文脈が入っている
                    - 文章の意味ベクトル
