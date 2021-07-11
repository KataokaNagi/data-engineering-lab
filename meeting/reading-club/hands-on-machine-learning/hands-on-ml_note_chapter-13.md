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

# scikit-learn、Keras、TensorFlowによる実践機械学習 第2版 第13章 読書メモ
- p.409- TensorFlowによるデータのロードと前処理

<!-- 目次: 右クリックから Markdown:TOC Insert/Update [Ctrl+M T]  -->

## 第13章 導入

#### TensorFlowのデータAPI
- DNNの大規模なデータセットに対応
- データの入手元と変換方法をのみを指示
- 以下はTF（Tensorflow）が代行
    - マルチスレッド管理
    - キューイング
    - バッチへの分割
    - プリフェッチ

#### データAPIでの入力形式
- 拡張前
    - CSVなどのテキストファイル
    - レコードが固定長のバイナリファイル
    - レコードが可変長のTFRecord形式
        - 柔軟で効率が良い
        - 通常はプロトコルバッファを格納（オープンソースのバイナリフォーマット）
- その他、BigQueryなどに拡張可能

#### 前処理
- 主な対象
    - スケールの異なる数値フィールド群
    - テキスト特徴量
    - カテゴリ特徴量
- 主な対処
    - 正規化
    - ワンホットエンコーディング
    - バッグオブワーズエンコーディング
    - 埋め込み（embedding）（後述）

#### 便利なTFライブラリ
- TF Transform (tf.Transform)
    - 訓練前：訓練セット全体を高速なバッチモードで前処理
    - 訓練後：TF関数として訓練済みモデルに組み込んで前処理
        - 本番環境で新たなインスタンスをその場で処理可能
- TF Datasets（TFDS）
    - 大規模なデータセットがダウンロード可能な関数を提供
    - データAPIで上記関数を操作可能なデータセットオブジェクトを提供

<!-- -------------------------------------------------- -->

## 13.1 データAPI
#### データセット
<!-- コード -->
- ディスクなどから少しずつ読み出していくデータ要素のシーケンス
- 例：from_tensor_slices(X)
    - テンソルXの第1次元のスライスであるデータセットを返す
    - つまり、tfのスライスをDatasetのスライスに変換？
    <!-- - X = tf.range(10) を書かずにtf.data.Dataset.**range(10)**としてよい -->

<!-- -------------------------------------------------- -->

### 13.1.1 変換の連鎖
#### 別のデータセットに変換するメソッド 1/4
- repeat(n)
    - 同じスライスをn回連結
    - コピーではない（高速かつ小容量？）
- batch(n)
    - スライスをn個ずつのスライスに分割
    - 最後のバッチがn個未満の場合、引数にdrop_remainder=Trueで削除可能

#### 別のデータセットに変換するメソッド 2/4
- [map](https://qiita.com/conf8o/items/0cb02bc504b51af09099)(lambda x: xの式)
    - 要素をラムダ式で柔軟に変換するなど
    - TF関数に変換可能なラムダ式のみ対応（12章）
    - [引数num_parallel_calls=tf.data.experimental.AUTOTUNEで並列・高速化](https://tensorflow.classcat.com/2019/03/23/tf20-alpha-guide-data-performance/)

#### 別のデータセットに変換するメソッド 3/4
- unbach()
    - bach()で作ったデータセットを解体
    - 試験段階のメソッドで、collabではエラー
- apply()
    - \[\]で囲まれたデータセット全体に適用
    - 引数にdataset.unbach()などを用いる

#### 別のデータセットに変換するメソッド 4/4
- filter(lambda x: xを用いたbool演算)
    - ラムダ式がtrueの要素xのみを用いる
- take(n)
    - 戦闘からn個の要素を用いる

<!-- -------------------------------------------------- -->

### 13.1.2 データのシャッフル
#### Datasetのシャッフル
- shuffle(buffer_size=n, seed=m)
    - 要素のシャッフル
    - 独立同分布（同一の分布から独立に抽出された状態）でよく機能する勾配降下法などで使用（4章）
    - 大規模なデータからサイズnのバッファを経由してシャッフル
    - 大規模データセットに見合った大きいバッファサイズが必要
    - RAMの容量に注意
    - shuffle()後にrepeat(3)しても、3回とも異なるリピートとなる
        - 引数reshuffle_each_iteration=Falseで同じリピートにできる

#### 便利なシャッフル
- list_files(DATA_FILE_PATH, seed=n)
    - データをシャッフルしてロード
    - 引数suffle=Falseも指定可能
- interleave(lambda file_name: ラムダ式, cycle_length=n)
    - n個のファイルを同時に無作為に読み出す
    - n個のデータセットをもつ1個のデータセットを作成
    - n個のデータセット間の同じ長さの部分が互い違いになる
        - [引数num_parallel_calls=tf.data.experimental.AUTOTUNEで初めて並列化する](https://tensorflow.classcat.com/2019/03/23/tf20-alpha-guide-data-performance/)
- コードでは、ファイルパスが尽きるまで5個ずつ取り出しインターリーブしている

<!-- -------------------------------------------------- -->

### 13.1.3 データの前処理
#### csvデータのスケーリング
- TFで上手く平均0、分散1に統一したい
- tf.io.decode_csv(LINE, record_defaults=\[...\])
    - 第1引数：CSVの1行
    - 第2引数：1行の列数とデータ型がわかる初期値を格納した配列
        - 敢えて0.を入れると欠損時に例外を吐く
    - 1次元テンソル\[\[...\], ..., \[...\]\]を返す
        - tf.stack(fields\[スライス表現\])で\[..., ..., ...\]に直す

<!-- -------------------------------------------------- -->

### 13.1.4 １つにまとめる
#### これまでの処理を関数化
- 新要素は最後の行のprefetch(1)のみ（後述）
<!-- コード -->

<!-- -------------------------------------------------- -->

### 13.1.5 プリフェッチ
#### プリフェッチによる並列化
- prefetch(n)
    - n個のバッチをCPUとGPUで並列・高速化
    - 一般にn=1でよい
    - GPUのRAMの容量や帯域幅（速度）が重要
    - 引数num_parallel_calls=tf.data.experimental.AUTOTUNE
        - CPU内で並列化
        - nを自動調節

#### その他の便利な関数
- cache()
    - データセットがメモリに入る程度に小さいときに高速化
    - ロード前処理とシャッフルの間で実行
- concatenate()
- zip()
- window()
- reduce()
- shard()（破片）
- flat_map()
- padded_batch()
- from_generator()
- from_tensors()

<!-- -------------------------------------------------- -->

### 13.1.6 tf.kerasのもとでのデータセットの使い方
#### データセットの応用
- 種々のデータセットの作成
    <!-- - コード -->
- モデルの構築と訓練
    <!-- - コード -->
- テストの評価と新インスタンスの予測
    <!-- - コード -->
<!-- - numpy配列も使用可能 -->

#### 独自のTF訓練関数（12章と同様）
- p,401の自動微分のコードと比較するとよい

<!-- -------------------------------------------------- -->

## 13.2 TFRecord形式
#### TFRecord 概要
- データのロードやパースがボトルネックなら用いる
- 大規模なデータの効率的な格納・読み出しが可能
- 可変長バイナリレコードのシーケンス
    - 長さ情報
    - 長さ情報のCRCチェックサム
    - 実データ
    - 実データのチェックサム

#### TFRecordの利用
- 書き込み
    <!-- - コード -->
- 読み出し
    <!-- - コード -->
- 出力
    <!-- - コード -->

<!-- -------------------------------------------------- -->

### 13.2.1 TFRecordファイルの圧縮
#### TFRecordファイルの圧縮
- 送受信に便利
- option引数で指定
- 解凍

<!-- -------------------------------------------------- -->

### 13.2.2 プロトコルバッファ入門
#### protobuf（プロトコルバッファ）
- 通常のTFRecordで使われるシリアライズ化されたバイナリ形式
- 可搬性と拡張性に優れる
- protoc：protobufコンパイラ
- .protocファイル内の定義例

#### Pythonのprotobufアクセスクラスの使用例
- personインスタンスの可視化や読み書き
- SerializeToString()でシリアライズ
- ParseFromString()でデシリアライズ

#### protobufとTFとの関係
- protocファイルで定義したPersonクラスはTFオペレーションでない
    - TF関数に単純に組み込めない
    - tf.py_function()で組み込むと速度と可搬性が落ちる
    - TFで定義された特別なprotobuf定義で解決する
- その他詳細
    - https://developers.google.com/protocol-buffers/

#### 
- 

<!-- -------------------------------------------------- -->

（片岡担当分ここまで）

### 13.2.3 TensorFlow Protobuf
### 13.2.4 Exampleのロードとパース
### 13.2.5 SequenceExample protobufを使ったリストの処理
## 13.3 入力特徴量の前処理
### 13.3.1 ワンホットベクトルを使ったカテゴリ特徴量のエンコード
### 13.3.2 埋め込みを使ったカテゴリ特徴量のエンコード
### 13.3.3 Kerasの前処理層
## 13.4 TF Transform
## 13.5 TFDSプロジェクト
## 13.6 演習問題
1. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
2. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
3. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
4. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
5. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
6. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
7. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
8. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
9. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
- 

13. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
11. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
12. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
13. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
14. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
15. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
16. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
17. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
18. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
19. 
    - 片岡の解答
        - 
    - 本書の解答
        - 
20. 
    - 片岡の解答
        - 
    - 本書の解答
        - 