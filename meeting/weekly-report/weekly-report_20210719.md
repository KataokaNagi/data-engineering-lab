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

# 週次報告書 2021年07月19日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 

## 2. 実施内容

### 目次
- 2.1 
- 2.2 
- 2.3 

### 2.1 
- 

### 2.2 
- 

### 2.3 
- 

## 3. 次回までに実施予定であること
- 

## 4. 雑多メモ

### 4.1 勉強会前
- ズレる主張
    - LDAのトピック語に近い単語を含む文章の〇〇
- 主張の調査
- 記事の事象
    - 日付とLDAでトピックを揃える
    - 見出しに載る内容なら揃うはず
    - 新規性のポイントでないので泥臭く行う
- 記事内の主張
    - 疑問符の構造を学習
        - 短くまとめられた人・組織の主張なことが多い
        - 英語で学習し、英語に翻訳した任意の言語に対応
        - 疑問符以外にも対応
            - 名詞を含む
        - 協調になるものは除外
        - ジャンルによってはわからん
        - 予備実験
            - 引用符の中身を長さ、形態素の数などでソートして考察
        - 疑問符内にありそうな文章の類似度でクラスタリング
    - 「LDAで得た単語に最も近い意味の主語」に係る連用語
        - word2vec？
        - 固有名詞は文脈を見ないとわからない？
    - LDAで単語をクラスタリングし、集めた記事からLDAで文章クラスタリングする
        - 新規性、関連性
- 記事の言語学的な調査
    - 何と比べて
    - 大事なものが上に、は言語依存
    - 記事的書き方->TV的書き方->記事的書き方
    - ニュースは5W1Hで書かれる
        - 重要度の低いものから消える
        - [1]I. Fang, Writing Style Differences in Newspaper, Radio, and Television News. Monograph Series No. 1. Center for Interdisciplinary Studies in Writing, University of Minnesota, 227 Lind Hall, 207 Church St, 1991. 参照: 7月 13, 2021. [Online]. Available at: https://eric.ed.gov/?id=ED377481
- 新規キーワード
    - TDT（Topic Detection and Tracking）
    - 議論マイニング
    - 含意関係認識
    - procon（賛否）
    - annotation（注釈）
    - XLU（cross-lingual understanding）
    - zero-shot
        - 片方の言語にのみラベル
    - cross-lingual word embeddings
    - contextual word embeddings
    - sentence embeddings
- 単語LDA->文章LDA
- 要約したときに食い違うもの
    - 要約は何を見ているか
    - BERT
    - 同音異義を排除できているか
- LDAは固有名詞と関係ない潜在トピック？
    - 分類、新規性の検出、要約、類似性や関連性（元論文より）

## 4.2 勉強会後
- 事象か否かのクラス分類（クラスタリング？）
    - MLを調べる
        - [LSTM](https://qiita.com/KojiOhki/items/89cd7b69a8a6239d67ca)
        - [LSTMのクラス分類](https://qiita.com/MENDY/items/99da56f61f9af51dda15)
            - many to one
        - まだよくわかっていない
        - 文章ごとにクラスタリング
        - [Attention](https://www.youtube.com/watch?v=bPdyuIebXWM)
            - 特徴
                - Transformer、BERTの始祖
                - 変換対象との関連性を計算
                - 語順変化に強い
                - 30語以上の長文にも強い
                - 未知語（固有名詞）への対処が弱い
            - システム
                - 前後に文脈を伝播（Annotation）
                - 意味ベクトル１つでなく、単語ごとに意味を付与
        - [Transformer](https://www.youtube.com/watch?v=50XvMaWhiTY&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR&index=9)
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
        - [BERT](https://ledge.ai/bert/)
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
        - [SCDV](https://www.youtube.com/watch?v=gnnnB3gd_0U&list=PLhDAH9aTfnxL4XdCRjUCC0_flR00A6tJR&index=7)
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
        - [SCDV](https://qiita.com/fufufukakaka/items/a7316273908a7c400868)
            - t-SNEで分化すると良さそう
        - [RoBERTa](https://data-analytics.fun/2020/05/08/understanding-roberta/)
            - BERTより沢山学習
            - Newsを学習
            - 長い文章に対応
            - 毎回ランダムにマスキング
        - [FASTTEXT]()