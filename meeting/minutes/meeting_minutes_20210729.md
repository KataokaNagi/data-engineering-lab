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

# 研究発表 議事録 2021年07月29日

## 木村研究室

### 片岡
- 様々な名詞の立場の違いを本当に分割できるか
    - 「出来事の階層はこのようなもの（図）を期待し、この立場の違いが生まれるように分析・修正する」
- ベクトルで推薦してから出来事と主張を分割すればよいのでは
    - 「仰る通り」
    - 「提案手法とどちらがより近い出来事を推薦できるかは、比較する必要がある」
    - 昔考えたはずなのに忘れていた
        - 昔の議事録を振り返ると良さそう
- 声が小さかった
- 画面共有のメニューが共有画面に表示されてしまっていた
- 矢印キーが何故かたまに効かなかった
    - 「失礼しました」がテンパってごにょごにょした
- 予備資料の見せ方を練習してなかった
- 杉本先生のご質問を理解することができなかった
- 緊張した
    - 声が震えた
    - 息を吐けなくなった
- ご説明します　と言ってしまった
- 相槌に「うーん」「あー」と言ってしまって失礼
- 回答を伝える順番が回りくどかった
    - 先に仰る通りだと伝えるべき
- 「全容を把握する」を一部修正し忘れていた
- 顔が写っているのを忘れていた
    - 杉本先生の質疑応答でかなりしかめ面をしていた気がする

### 亀川
- 寝癖注意
- 3式　条件～～が必要なのでは
    - 「仰る通り（予備資料）」
- イプシロン
    - この条件と人間に気付かれないという条件の対応は簡単でない
    - イプシロンを変えてやったか
        - 「変えました」
            - 「1では白くなる」
            - 「150/255と100/255とした」
            - 「3のみ」
                - 摂動の最大値の意味がわからない、イプシロンと関係あるのか
                - もっと積極的にできるのではないか（？）
- 自分の概要を開ける状況にしておくとよい
    - スライドに入れる？
- 質疑応答はペンタブに切り替えていつでも書ける状態にしておけばよかった
- 
### 志田
- ターゲットが限られていて簡単なタスクに見える
- 照明をどうして除外できるのか
    - 時系列データの考慮
        - 本当？
- 曲がるときをどう判断するか

### 土屋
- 目的がわからない。誰が喋っているのかを知りたいのか
    - 「3人の議論で、誰が離しているのか」
- 図2の縦軸がわかりにくい
    - 「音の強さ」
    - 汎用性はあるのか、学習してないものを見せてわかるのか
        - 「沢山学習します」
        - 「動作の動きと音の強さが比例してると考えられる」
    - 顔の向きの違いを検出できるのか
        - 「いろんな角度のデータを集めたい」

### 平山
- ぼかし背景で猫ちゃんが
- 忘却は軽減したが、9割忘却しているのは実用的でないのでは
- λとは何か、これで変わるのでは
    - 「1としました」
    - 「大きくしても小さくしても変わらない」
        - おかしくない
        - 大きくして減るのはおかしい
        - 図が見にくい
        - 学習するほど忘却するのは何故か
            - 「想定外で、課題だと感じている」
                - 相当な課題ですね

### 増岡
- 雑草とニラとで特に注意すべき点は
- カラーの方が情報が多いのでは  
    - 「雑草とニラで色は同じなので特に重要な情報ではない」

### 松本
- 論文の何を入力するのかわからなかった
    - 概要
- 概要内の目的、アプローチを検出してそこだけを使うとよいのでは
    - ミス回答「全文を入力します」
    - 「自分で決めると偏見が入ってしまう、GANで自動化したい」
- 概要にはタイトルに使う言葉が入っているはず
    - タイトル考えてから書く概要は順番が逆なのでは
- a new approach for the ばかりなのは、教師あり学習に失敗しているのでは
    - GANで具体的にどうできるかを検討しています
        - 予備実験でうまくいかないと大変だよ
        - うまくいかない原因をもっと分析してみて

### モ
- どこの画像を一時停止するのか
    - 「10分割り」
        - 「悪かった」
        - 「別のやり方を考えるつもり」
- 全フレームなのか1フレームなのかがブレてるよ
- 画像以外の情報とは
    - 「視聴時間、動画時間、カテゴリ」
        - かなり強力な情報だけど、実験では使ってなかったんだ。
            - 概要に書いておいて
- 回答が長い
- 特徴Ａ，Ｂ、Ｃはどう決めるのか
    - CNNとVideo2Vec
    - 数値列なので分解して取り出しにくいのでは
        - だからWord2Vecを使うのでは
            - 「卒研２で検討します」

### 原田
- 二次元でやると言っているのに、なぜy=xの一次元で行うのか
    - 「最も簡単な手法でやろうと思った」
    - 低次元すぎるのでは
        - 「低次元だと思うので高次元で試したい」
            - 回答の最後が無駄にながかった印象
            - 先生がもういいと言わんばかりに遮ろうとしていた
- 競馬予測とはどういうこと
    - 欠損値が多い
    - 例があると嬉しい
- かなり落ちて応答していて好印象
- 結局欠損を何を埋めるのか
    - 「欠損値が非常に多いので、高い精度でできないと、予測に使えない」
        - 回答になっていない？
- 手法を追究すれば走破時間の「精度」が上がるんですか
    - 「はい」
- 若干音質が悪いが概ね良好

### 山中
- 体調悪そう？緊張？
- 助詞の発声がすぼんでいる
- ポップノイズ多め
- 「まあ」が多い 
- 従来手法jで、GAを採用とした理由
    - 「目的にあるように、微分を用いずに誤認識を起こす摂動を求めるためにGAが適切だと考えた」
        - 損失関数と微分を用いてもいいはずなのになぜ
            - 無回答
            - 木村先生「モデルの損失関数が公開されていないため」
                - 「損失関数を用いるのが困難なため」
 

## 杉本研究室

### 石槻 日常的なイベントの因果関係と推移関係に関する知識の獲得
- ある出来事が起きたときに次にどんな出来事が起きるか
- 先行研究
    - 日本語意味解析SAGE
    - イベントの分散表現
- 頻度ベース
    - 発展しにくい
- イ形容詞かナ形容詞
- 

### 野田 ツイートコーパスを用いた顔文字推薦システムの提案
- アンケートのコーパス
    - 文脈を学習すればよいのでは？
- 文をポジネガ、感情、コミュニケーション、動作で学習
- 木村先生「LSTMは長文に絶えない」
    - 顔文字より30文字以上前は一応学習して忘れてもいいかも

### 野本 登標準語から方言への変換による親しみやすい文の生成
- 方言は単語単位で自然な変換ができない
- 集める量は？

### 渡部 対話におけるユーザの感情を考慮した川柳生成
- 品詞パターン
    - 意味の解析ができない？
    - 川柳らしさはどこから
    - ユーモアはどこから
- 否定語の考慮をしてね

### 橋野 ニュース記事と株価推移データを用いた株価予測
- 株価とニュースのＭＬ
- BERT
- LSTMもかなりうまくいってそう
    - 本当？
        - 今頃暴落しているのでは
- なぜ失敗したBERTを使うのか
    - BERTなしでいいのでは
- 
- 

### 曹金 Twitterにおける感情分析を用いた世論の抽出と分析
- 

### 牧 Twitterからの話題語に関する意見の抽出と可視化
- BSディベート
- 議論の余地の残る問題
- 対象、属性、効果
    - プリウス、デザイン、かっこいい
- 主観的な情報⊃評判情報
- SVM
- LDA
- 意見文をクラスタリング
- 形態素解析
- 典型意見と特異意見
- 五十嵐先生「オリンピックという単語だけでは主張がわからないのでは」
- 木村先生「ツイートから意見を収集する目的は
    - 世論を知って何が美味しいのか

### 杉田 商品に関する属性と評価表現のレビューからの抽出
- レビューに頼らない属性？
- 属性、評価表現、対表現
- 先行研究
    - SVM
- 照応解析
    - 先行詞の特定
- 分かち書き
- NNでできることを一生懸命MLしている？
- 素性

### 永松 ユーザ特性とオノマトペを利用した映画推薦システム
- オノマトペで感情を表す？
    - 特殊なオノマトペ
- 1つのオノマトペでは意味が多すぎる
    - ドキドキ
        - 恋愛
        - ホラー
- オノマトペだけでは何万と映画が出てくるのでは


## 先生メモ

### 志田 渉	
- 入力画像はサイドミラーではなく別のカメラか。
- ヘッドライトが別々に認識されたらクラスタリングでまとまると考えてよいのか。
- 監視対象が限られているので簡単なタスクに見えるがどうか？街灯などをはじくのはどんな理屈か。							

### 増岡 紳吾
- 実用的な面白い研究だと思う。
- 植物の範囲を決めたり、二値分類をしたりすることは多くの研究で
- 行われているが、増岡君の研究で注意しなくてはいけない点はどこにあるか。
- 分類するうえでの工夫は？
- カラーとグレースケールの比較などしてみるとよい。
- 質疑の対応ははっきり話ができていた				
 
### 片岡 凪
- 同じトピックに対してポジティブな意見とネガティブな意見が分けて見れるといいが、
- クラスタリングによっては意見が固まってしまって立場の違いが見えなくなってはしまわないか。
- 先行研究で似た記事を集めるが出来事と主張が混ざってしまうとあるが、
- 混ざっていることが分けられれば良いのではないか？
- 発表時間が６分だったので、スケジュールなどの説明ができるとよかった				

### 松本 陸
- タイトルを出力を行うにあたって、論文全文を入力するか？
- アブストラクトのなかにもいろいろ書かれているが、タイトルに関係する部分は部分的であるだろう。
- その部分だけ注目してタイトル生成は行わないのか？
- 予備実験からタイトルを抽出すれば簡単にできそうだが、特定の文字列が出力されるのは教師あり学習が
- ちゃんとできていないのでは？
- 予備実験がうまくいかなかった理由を検討すべきでは？
- うまくいかない原因をつぶしてから次のステップに行くべき				

### モチンハン
- 手法のモデルの入力がわからない。
- 動画のワンフレームか、どんな基準でとってくるのか。
- 画像以外の情報としては何を考えているか。
- 何を入力したいのかが概要に書かれていないのでしっかり
- 書いておくべき。
- 評価実験はどのように行うか。
- 特徴A、Cなどはどうやって決める？
- まとめは一通り読んでください				

### 平山 明香里
- 二つのタスクがそこそこ両方できないとよくないだろう。ラムダを強くしたらどうなるのか。
- ラムダが非常に大きくなればタスクAの結果が変わらないはずなので理由をしっかり検討する必要がある。
- エポックが増えたら正解率が下がる
- のは学習がうまくいっていない？
- より簡単なデータセット（例えば2次元データ）で確かめてみるとよいかも。

### 土屋 ゆり
- 目的がわからない。
- 画像に移っている人物の誰が今しゃべっているかを推定したいのか。
- その時の手がかりのなかの音は、強さ？
- グラフの縦軸は何を表しているか。内容を見ていない。
- 汎用性があるのだろうか？
- 姿勢の違いはどう扱うのか？
- 適切に質疑にこたえられていた				

### 亀川 朋生
- 式３にF_s - F_t  > 0の条件が必要ないのか。
- 人間に認識されないことが大事なので、それに対応する条件が必要。
- εを変えて実験を行ってみたか？
- 最適化関数としてどのようなものをとると適切か（どういうものにすると原理的に人間に認識されにくいか）を考えましょう				

### 原田 佳英
- 予備実験で2次元のデータを使っているが、なぜy=xの一次元のデータを用意したのか。
- 競馬データを用いた層は時間の予測とは？
- どういうデータか例が示されているとよかった。
- 欠損値をどう使うのか？
- y=xにしたのは、2次元だとyの推定にxしか使えないので相関が強いものを使ったためです。				

### 山中 悠太
- 今回の摂動を起こすのにＧＡを採用した理由は何か。
- 損失関数や出力値の微分を用いてはいけないのはなぜか。
- 一般のニューラルネットワークではどのような損失関数が使われているかは不明であるから、という回答はできる				


## 反省会

### 片岡
- 6分だった
- 階層クラスタリングは上手くいかないことを覚悟
    - 予備実験を早くして早く分析
- ハプニングしてたベルを頼る

### 亀川
- 

### 志田
- 伝わりづらい内容こそ絵を

### 土屋
- 

### 平山
- MNISTよりも簡単なデータで確かめてみては
- 二次元座標の直線の左右でデータあり、なしとしてみる
- 軽いと重みの確認がしやすい

### 増岡
- 例外を洗い出す

### 松本
- 仮定しも問題か簡単に
    - 他に労力を割く
- GANの前にTransformeをを工夫
- 片岡「冠詞のAの頻度が高く、Aの続きでA New Approachとなる確率が高いからでは」
    - A などをストップワードとしたり、重みを減らしてみては

### モ
- 

### 原田
- 

## 先輩レビュー
- 不真面目
    - 院生のレビューは閉じた
- 真面目
    - 内容に関して
    - 緊張しても伝えようとする意識を持ち続けて
        - 特にここを伝えたいという抑揚

## 気になったこと
- コサイン類似度
    - カウントベースの分野の派生
    - データ工学の派生から自然言語処理

## 業務連絡
- 学会発表してくれると嬉しい
    - 電子情報通信学会
        - 3月
    - 情報処理学会
        - 5年ほど発表してない
- 勉強会
    - LSTMを完成
    - 火曜の午前
- お盆は休む
- 8月下旬に報告会を再開
    - 23日？
    - ユナイト
    - 明日