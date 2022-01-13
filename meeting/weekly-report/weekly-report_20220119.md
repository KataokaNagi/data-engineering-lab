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

# 週次報告書 2022年01月19日
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
- 概要書
    - 先生のご助言を反映
    - 数値ベクトル
        - Google Scholor 20件中2件
        - 存在しない用語っぽい
        - 線形代数の本に数ベクトルがあった
            - ブリタニカ事典曰く実数
        - 実ベクトル空間はあったが実ベクトルは見当たらない
- 分類の実行が終了
    - 20220109 2:10 - 20220113 10:00
    - predict_time(sec): 213516.61013507843
    - predict_time(sec): 110484.236577034
    - predict_time(sec): 44781.080478191376
    - 計368781.9272s
    - 6146.365453m
    - 102.4394242h
    - 78457記事
        - インド47342記事
        - 日本21039記事
        - 韓国10076記事
    - 4.700433705086863 s/記事
- 出来事のembed
    - 20220113 10:00 - 24:00?
    - 1939MiB
    - 60記事で24秒
        - 78457記事で31382.8s=8.7h
    - embed_time(sec): 47.06882643699646
    - embed_time(sec): 24.006435871124268
    - embed_time(sec): 12.368020057678223
- 国の結合とidづけ
    - 6.45128870010376s
- 評価方法の調査
    - h, c
    - 相関係数
    - カイ二乗分布
- 実装
    - **主張の文の特徴量ベクトルを作成**
        - process_05_sentences_features_calculator.py
        - india-articles_process-05_calced-sentences-features.txt
        - #e:sent-1#c:sent-2...\n
        - S-BERTにsent-nを入れて特徴量を算出
        - article-n;[e-feature-array];[c-feature-array];[all-feature-array]#article-n;sentence-n;e;feature-x;feature-y;[feature-array];sent-1#article-n;sentence-n;c;feature-x;feature-y;[feature-array];sent-2...\n とする
            - 各文に特徴量を追加
            - 各文に番号を追加
            - #eのfeatureは不要だが、もしかしたら使うかも
        - txt保存
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