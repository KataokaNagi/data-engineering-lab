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

# 週次報告書 2021年09月21日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 予備実験
    - 既存プログラムのモジュール化
        - 記事のデータセットの調査
        - ~~EvidenceとClaimの分類~~
- ~~思考実験~~
    - 報告会の振り返り
        - 主張と出来事のクラスタリングの順序の是非
        - 分類とクラスタリングの仮説の設定
- ~~研究スケジュールの修正~~

## 2. 実施内容

サークルの予定が多く入り、あまり動けない1週間だった。

### 記事のデータセットの調査

翻訳機の実装を保留し、Google Dataset searchで翻訳済みのデータセットを調査した。
要件として、
1. 収集方法が近しい3言語以上のデータセットであること
2. 一ヵ月以内の狭い範囲の網羅性の高いデータセットであること
3. 人気記事などの変なソートが入っていない or 入っていても除去できるデータセットであること

を意識した。

「news lingual」「news translation」で検索した50件ほどの全てのデータセットを調査したが、期待するデータセットは得られなかった。
「FLORES-101」というFBが2021年に作成したデータセットは、引用件数が340件と多く、ベンチマークのコードがあり、100言語の記事を有しているが、要件2を満たしていない。
同データセットで取り上げられていたが、FBが開発したM2M-100というオープンソースの多言語翻訳機はもしかしたら利用することがあるかもしれないと考えた。
副産物として「Youtube-Dataset for Language Identification in Speech Signals」というYoutubeの動画データセットを見つけ、土屋さんの研究に利用できるかもしれないと考えた。

100件以上ヒットした「news language」の検索結果では、今まで調査したデータセットとは別のデータセットも散見された。
今後は、この検索結果で調査したり、要件1の制限を緩和して2言語のデータセットを複数利用してみたり、FLORES-101がどれだけ研究目的に合っているかを詳しく確認したり、研究目的に合う翻訳機を調査したりしたい。

## 3. 次回までに実施予定であること
- 予備実験
    - 既存プログラムのモジュール化
        - 記事のデータセットの調査
        - EvidenceとClaimの分類
    - クラスタリングの実装
- 思考実験
    - 報告会の振り返り
        - 主張と出来事のクラスタリングの順序の是非
        - 分類とクラスタリングの仮説の設定
- 研究スケジュールの修正

## 4. 雑多メモ
- データセット
    - 要件
        - 多言語
        - 狭い同時期
        - ソートが少ない
    - 調べたカテゴリ
        - 表形式
        - テキスト
        - アーカイブ
        - その他
    - 調べたワード
        - news
            - 100件以上
        - news world
            - 100件以上
        - news lingual
            - 5件
        - news translate
            - 32件
        - news translation
            - 40件
    - 絶対使えないもの以外
        - Internet news data with readers engagement
            - 読者のエンゲージメントを強化した様々な出版社の最も人気のある記事
            - 201909-11
            - 人気のソートは不要
        - Popular News articles
            - 7つのカテゴリ
            - **12の言語**
            - Webhose
            - 201702-03
        - News Aggregator
            - カテゴライズ済み
            - 202101？
        - A Data set for Information Spreading over the News
            - スポーツ、災害、気候のみ
            - ドメインのギャップという同目的
            - 2016-2020
        <!-- - News Articles
            - メディアバイアス用
            - 201612-201703
            - 英記事のみ？ -->
        - World news articles
            - 引用154
            - 世界の英記事
        - WMT 2018 News Dataset
            - 7言語の英訳
            - プロの翻訳
                - 手動は目的と違う
            - 1500の文章
            - 数十のニュースサイト
        - Parallel Global Voices (English - Dutch) (Processed)
            - 40以上の言語
            - 201507-08？
                - 出版日でなくクローリング日？
        - **FLORES-101**
            - Helping build better translation systems around the world
            - kaggle
            - 引用341件
            - 多言語 対 多言語の翻訳のため
            - ローリソース言語に焦点
                - アムハラ、モンゴル、ウルドゥー
        - Youtube-Dataset for Language Identification in Speech Signals
            - 土屋さんの研究に使えるかも
- M2M-100
    - FB
    - 100言語翻訳機
    - OSS
