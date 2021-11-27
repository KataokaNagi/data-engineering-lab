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

# 週次報告書 2021年12月01日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- EvidenceとClaimの分類
- クラスタリングの実装

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
        - process_01_classifier_as_claim_or_evidence.py
        - india-articles_process-01_classified-claim-or-evidence.txt
        - 日本記事を3か国の記事に変更
            - for with openではなく、複数のファイル名を指定して実行
                - 別にファイル名のtxtファイルを作成
                - 長くて指定が面倒なのでやっぱりfor with open
                    - no time
        - #を元にリストに格納
        - 分類
            - 時間かかるからpyにした方がいいかも
        - #e;[ec-score-array];sent-1#c;[ec-score-array];sent-2...\n のtxt
            - DeepL翻訳で10記事ほどチェック
            - 文頭、文末はシャープがないことに注意
        - ニュートラルも含めることを考えつつ
        - シャッフルを消す
            - 前処理前の記事との紐づけのため
            - 本当は必要
    - 出来事の文章の特徴量ベクトルを作成
        - process_02_articles_features_calculator.py
        - india-articles_process-02_calced-articles-features.txt
        - 出来事の文のみを結合
            - 一応主張、全文も作っておく
        - SBERTに入れる
        - 文頭にarticle-n;[e-feature-array];[c-feature-array];[all-feature-array]#を追加
    - 主張の文の特徴量ベクトルを作成
        - process_03_sentences_features_calculator.py
        - india-articles_process-03_calced-sentences-features.txt
        - #e:sent-1#c:sent-2...\n
        - S-BERTにsent-nを入れて特徴量を算出
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#article-n;sentence-n;e;[ec-score-array];[feature-array];sent-1#article-n;sentence-n;c;[ec-score-array];[feature-array];sent-2...\n とする
            - 各文に特徴量を追加
            - 各文に番号を追加
            - #eのfeatureは不要だが、もしかしたら使うかも
        - txt保存
    - 3カ国の記事を結合して保存
        - process_04_nations_articles_concatenator.py
        - process-04_concatenated-nations-articles.txt
        - 国情報を付与
            - nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;[ec-score-array];[feature-array];sent-1#nation-name;article-n;sentence-n;c;[ec-score-array];[feature-array];sent-2...\n
    - [e-feature-array]を基に記事（行）をクラスタリング
        - process_05_articles_cluster_generator.py
        - クラスタごとに名前を付けて保存
            - process-05_generated-articles-cluster_n.txt
        - アルゴリズムはオプションで変更
            - ファイル名の末尾にアルゴリズム名
        - クラスタの粒度
    - ある記事のある文章から、似た文章とその文章が書かれた記事が参照できるか
        - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
        - 主張の文のクラスタリング
        - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
        - クラスタごとの主張の差異を分析
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
        - process-06_find-articles-cluster-of-selected-sentence-info.sh
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
        - process-07_sentences_cluster_generator.py
        - クラスタごとに名前を付けて保存
            - process-07_generated-sentences-cluster_n.txt
        - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
            - デバッグのため、後で実装
        - その記事クラスタファイルを開く
        - #で分割し、cの区分のみを1つのリストに格納
        - リストの要素を[feature-array]を基にクラスタリング
        - クラスタリング手法を変えやすいように
            - オプションで変更
            - 変更できるライブラリ
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
        - process-08_find-sentences-cluster-of-selected-sentence-info.sh
    - 評価
        - 論文を読んで決める
    - まとめ
        - sent-1#sent-2#...\n
        - e;[ec-score-array];sent-1#c;[ec-score-array];sent-2...\n 
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#e;[ec-score-array];sent-1#c;[ec-score-array];sent-2...\n
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#article-n;sentence-n;e;[ec-score-array];[feature-array];sent-1#article-n;sentence-n;c;[ec-score-array];[feature-array];sent-2...\n
        - nation-name;article-n;[e-feature-array];[c-feature-array];[all-feature-array]#nation-name;article-n;sentence-n;e;[ec-score-array];[feature-array];sent-1#nation-name;article-n;sentence-n;c;[ec-score-array];[feature-array];sent-2...\n
        - process-05_generated-articles-cluster_n.txt
        - process-06_find-articles-cluster-of-selected-sentence-info.sh
        - process-07_sentences_cluster_generator.py
        - process-08_find-sentences-cluster-of-selected-sentence-info.sh
  