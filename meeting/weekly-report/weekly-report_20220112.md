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

# 週次報告書 2022年01月12日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 

## 2. 実施内容

### 目次
- 2.1 
- 2.2 
- 2.3 

### 2.1 

![](img/)
<div style="text-align: center;">
図. 
</div>
<br>
<br>

### 2.2 


### 2.3 


## 3. 次回までに実施予定であること
- 

## 4. メモ
- 計画
    - 概要提出まで
        - 7-20日
        - 本論3日
        - 概要3日
        - 実験6日
            - 1日でNN組み直し
            - 3日でクラスタリング
            - 2日で評価実験
        - 死が見える
    - 本論提出まで
        - 21-31日
        - 本論
        - 1日3ページと修正
    - 先生不在の5日間
        - 最悪本論
            - 謝辞
            - 微調整
        - スライド作成
        - 発表練習
        - 評価実験の続き
    - 先生がいる2日間
        - 本論最終チェック
- 卒論書き進め
    - 死ぬ気で2日で13ページ進めた
        - 参考文献2ページを含む
    - 45ページくらい書くことになりそう
        - 死ぬ気で書いても6日
        - 提案手法以外のページにどれくらいかかるかわからない
    - AttentionとTransformerいらんかったかも
        - モデルと式の説明は書き過ぎ？
        - 本研究に関係が薄い？
            - モデルを理解している必要は多少ある
        - 時間ないよ～
- 先生のクラスタリングの論文を参照
    - 出来事
        - 同じ出来事を集めたい
            - 別の出来事とは異なり具合は二の次
            - homo-geneity
    - 主張
        - 違う主張を見たい
            - 同じ主張が集まっているかは二の次
            - 多様性のベンチマーク
            - completeness
    - covidに限定したデータであるため、一般のデータと単純比較はできない
        - covidで別の手法を行い、多様性を評価
            - そんな時間はない
    - 人間の評価は必要
- 設計の再確認
    - [](./weekly-report_20211201.md)
- 再現率の改善
    - 手動ラベルの再検討
        - 判断基準もメモ
    - いい感じに機能してはいると思うんだけどな
        - 正例が少なすぎて正確な評価ができていない？
            - 140以上はしんどいよ～
        - 手動ラベルが間違っている？
    - 3層NNの実装
    - epoch数を変えて確認
        - 3エポックが良さそう
    - IBMがニュースにうまく適用できない可能性
        - 元はWiki
        - 文章の数が違う
        - 1つの記事に主張が0なケース
            - 客観的なニュース
            - ブレが多い主張はニュースで少ないほど良い
    - 分析
        - P（主張の正解ラベル）が6で少なすぎる
            - 3記事164文では不足？
        - 正解率は極めて高い
            - 出来事は出来事だと区別できている
            - 出来事多め、主張少なめで正しい
            - IBMは1:2だがニュースは15:148~1:10
        - 再現率はかなり低い
            - 3エポックがマシ
            - インバランスデータでは重要なことが多い
            - 主張だと検索できていないものがある
                - 主張の見逃しは少し嫌
            - https://zellij.hatenablog.com/entry/20120214/p1
        - 適合率はかなり高い
            - 主張だと検索・判断したものは大体（全て）主張
            - 主張でないありがたい
        - F値は0.57
            - 3エポックのみ最悪を免れている
            - 不均衡な判断になっているため、あまり参考にならない
        - MCC（マシューズ相関係数）は0.61
            - 少数クラスのため、参考にするとい
            - FP=0と偏っているため、参考にするとよい
            - 3エポックはまあ良い結果
            - 0.6なので最悪ではないが良くもない
            - https://www.datarobot.com/jp/blog/matthews-correlation-coefficient/
        - IBMはかなり性能がいい
            - IBMに過学習
        - eval_lossは小さいが、1エポックから上がっている
            - 過学習している証拠
            - あまりエポック数を回したくない
            - 本当は2層NNを追加する必要がある
- 3エポックで分類を実行
    - 20220109.2:10実行
    - 恐らく3日ほどかかる
        - 概要、本論、実装の時間
- クラスタリングの実装
    - 記事IDは文章分割の前処理時点で割り振るべきだった
    - 主張がない記事を削る必要がある
    - 主張がない記事が多すぎてクラスのサイズが小さくなりそう
        - 何もしなくても多様性高くなってしまう
        - クラス内が似たものにならなくなりそう
    - mean poolingをしたいのでc embeddingは全国一気にやりたい
- TODO
    - 全体的に
        - printデバッグを増やす
            - オリジナルのprint_debug()を作成
                - import
            - xqq君のjavaコードを参照
        - オプションでアルゴリズムを可変に
        - 後で何かやりたくなったときにできるように余分に処理しとく
        - こまめに記事をバックアップ
    - 主張と出来事の分類
        - process_01_train_classifier_as_claim_or_evidence.py
        - process_02_exe_classifier_as_claim_or_evidence.py
        - india-articles_process-01_classified-claim-or-evidence.txt
        - 日本記事を3か国の記事に変更
            - for with openではなく、複数のファイル名を指定して実行
                - 別にファイル名のtxtファイルを作成
                - 長くて指定が面倒なのでやっぱりfor with open
                    - no time
        - #を元にリストに格納
        - 分類
            - 時間かかるからpyにした方がいいかも
        - #e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n のtxt
            - DeepL翻訳で10記事ほどチェック
            - 文頭、文末はシャープがないことに注意
        - ニュートラルも含めることを考えつつ
        - シャッフルを消す
            - 前処理前の記事との紐づけのため
            - 本当は必要
    - 出来事の文章の特徴量ベクトルを作成
        - process_03_articles_features_calculator.py
        - india-articles_process-03_calced-articles-features.txt
        - 出来事の文のみを結合
            - 一応主張、全文も作っておく
            - 文の間にスペースを挿入
        - SBERTに入れる
        - 文頭にarticle-n;[e-feature-array];[c-feature-array];[all-feature-array]#を追加
        - 記事にcが存在しない場合'-'を代入
        - 記事にeが存在しない場合'-'を代入
    - **主張の文の特徴量ベクトルを作成**
        - process_04_sentences_features_calculator.py
        - india-articles_process-04_calced-sentences-features.txt
        - #e:sent-1#c:sent-2...\n
        - S-BERTにsent-nを入れて特徴量を算出
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n とする
            - 各文に特徴量を追加
            - 各文に番号を追加
            - #eのfeatureは不要だが、もしかしたら使うかも
        - txt保存
    - 3カ国の記事を結合して保存
        - process_05_nations_articles_concatenator.py
        - process-05_concatenated-nations-articles.txt
        - 国情報を付与
            - nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#nation-name;article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
    - [e-feature-array]を基に記事（行）をクラスタリング
        - process_06_articles_cluster_generator.py
        - クラスタごとに名前を付けて保存
            - process-06_generated-articles-cluster_n.txt
        - アルゴリズムはオプションで変更
            - ファイル名の末尾にアルゴリズム名
        - クラスタの粒度
    - ある記事のある文章から、似た文章とその文章が書かれた記事が参照できるか
        - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
        - 主張の文のクラスタリング
        - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
        - クラスタごとの主張の差異を分析
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
        - process-07_find-articles-cluster-of-selected-sentence-info.sh
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
        - process-08_sentences_cluster_generator.py
        - クラスタごとに名前を付けて保存
            - process-08generated-sentences-cluster_n.txt
        - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
            - デバッグのため、後で実装
        - その記事クラスタファイルを開く
        - #で分割し、cの区分のみを1つのリストに格納
        - リストの要素を[feature-array]を基にクラスタリング
        - クラスタリング手法を変えやすいように
            - オプションで変更
            - 変更できるライブラリ
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
        - process-09_find-sentences-cluster-of-selected-sentence-info.sh
    - 評価
        - 論文を読んで決める
    - まとめ
        - sent-1#sent-2#...\n
        - e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n 
        - article-n;[e-feature-array](;[c-feature-array];[all-feature-array])#e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n
        - article-n;[e-feature-array](;[c-feature-array];[all-feature-array])#article-n;sentence-n;e;feature-x;feature-y;;sent-1#article-n;sentence-n;#c;feature-x;feature-y;[feature-array];sent-2...\n
        - nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#nation-name;article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n
        - process-06_generated-articles-cluster_n.txt
        - process-07_find-articles-cluster-of-selected-sentence-info.sh
        - process-08_sentences_cluster_generator.py
        - process-09_find-sentences-cluster-of-selected-sentence-info.sh