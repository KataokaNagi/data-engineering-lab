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

# 論文要約 『Clustering Categorical Data Using Silhouette Coefficient as a Relocating Measure』

- [1]S. AranganayagiとK. Thangavel, 「Clustering Categorical Data Using Silhouette Coefficient as a Relocating Measure」, International Conference on Computational Intelligence and Multimedia Applications (ICCIMA 2007), 12月 2007, vol. 2, pp. 13–17. doi: 10.1109/ICCIMA.2007.328.
- 20220117参照


<!-- -------------------- -->

## 概要
- カテゴリデータをクラスタリングするための新しいアルゴリズム
    - 非類似度の最小値に基づいてグループ化
    - シルエット係数を用いて再配置

<!-- -------------------- -->

## 図表
- Zoo Datasetでのシルエット係数のプロット
- Mushroom Datasetでのシルエット係数のプロット

<!-- -------------------- -->

## はじめに
- データセットの属性
    - 数値的なカテゴリ
    - 数値とカテゴリの両方
- クラスタリングの基本原理
    - 距離メトリックまたは類似性メトリックの概念に依存
- クラスタリングに関する初期の研究
    - 2点間の距離を定義するために固有の幾何学的特性を利用できる数値データに焦点
    - 男性と女性の間の距離を求めることはできない
    - K-Means
- 本論文
    - カテゴリクラスタリングアルゴリズム
        - 非類似度行列と近傍概念を用いた
        - 効率的な
        - 凝集型クラスタリング手法
    - 近傍行列に基づいてクラスタが統合
    - 配置されたオブジェクトはシルエット係数を用いて再配置

<!-- -------------------- -->

## 関連研究
- クラスタリングに関する過去の研究成果
    - K- PrototypesアルゴリズムはK-meansに基づくが、数値データの制限を取り除いたものである。これは数値データとカテゴリデータの両方に適用可能である。K-modesアルゴリズムは、モードを使用してデータをクラスタリングするために使用される。Expectation Maximization (EM) アルゴリズムは、一般的な反復クラスタリング技術です[9]。ROCK (Robust hierarchical Clustering with linKs) は凝集型階層型クラスタリングアルゴリズムを応用したもので、タプル間のリンク数で定義される基準関数を発見的に最適化するものです。非公式には、2つのタプル間のリンク数は、データセット内でそれらが持つ共通の近傍性の数である[2,7]。Clustering Categorical Data Using Summaries (CACTUS)は、データベースを縦に分割し、これらのタプルの投影の集合を属性の組だけにクラスタリングしようとするものです[10]。 COOLCATアルゴリズムは、クラスタリングにおいて、エントロピー測定を使用する。LIMBOアルゴリズムは、情報ボトルネックを指標として、カテゴリデータをクラスタリングする[11]。 また，非類似度指標を変化させることで，ファジーKモード，K-representative，K-histogramが開発されている．ファジーKモードでは，ハードセントロイドの代わりにソフトセントロイドが用いられる[3]．Ohm mar sen らによる K-representative[8] アルゴリズムでは、相対度数という尺度が用いられている。K-representative では、クラスタ内の属性値の頻度をクラスタ 長で割った値を指標としている。また、K-histograms[11]では、クラスタ内の属性値の頻度をデータセット内の属性値の頻度で割った値が指標として用いられる。

<!-- -------------------- -->

## 定義と表記

（中略）

### シルエット係数 
- シルエット係数
    - クラスタの妥当性を示す指標である。 
    - （Sil(i) = (b(i) - a(i)) / max( b(i) , a(i)) 
    - a(i)
        - i と私が属するクラスターの他のオブジェクトとの平均非類似度
    - D(i,C)
        - すべての他のクラスタ C について，C のすべてのオブザベーションに対するi の平均非類似度
    - b(i) 
        - D(i,C) の最小値
            - I と隣接クラスタC の間の非類似度
    - Sil(i) 
        - 負の場合，オブジェクトは間違ったクラスタに配置される
        - 0付近であれば、オブジェクトはクラスタの間にある[9]。

### 
- 

### 
- 

<!-- -------------------- -->

##
- 

### 
- 

### 
- 

### 
- 

<!-- -------------------- -->

## おわりに
- 

### 
- 

### 
- 

### 
- 

<!-- -------------------- -->

## 片岡所感
- 

<!-- -------------------- -->

## 重要ピックアップ
- 
