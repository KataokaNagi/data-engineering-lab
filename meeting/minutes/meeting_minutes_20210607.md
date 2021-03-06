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

# 報告会 議事録 2021年06月07日

## 報告

### 片岡
- ググれば出る
- そのニーズを持つ人が見ればよい
- 他のニュースサイトに多様性を学んでもらう
- 学術的な
- ダイレクトにフィルターバブルを解決する問題であればよいのでは
- 大阪東京でも存在
- 同じ地域でも存在
- 企業間でも存在
    - 全部包括できる手法はないか
- 比較するのが良いのか
- 違うのはわかるが
- 見に行くアクションに繋がる
- 報道の違いを見せるのが啓蒙に繋がるのか
- 片方でしか報道していない場合
- 視野を広げたい人、広げたくない人の対象
- 片側の国で報道されていなかったら対を調べようもない
    - CNNのような世界標準と他を比較する
        - CNNも全てを表示できないので根本解決にはならない
- 対象は絞らないと難しい
- 反対側の意見を確認する
- 国の間の問題が明らかじゃないところも見てみたい
- 国の間がバブルの厚みが増しやすい
- 言語が異なると調べるハードルが上がる
- 数値でパッと表示された方が疲れがない
    - 最適化の代替
- アクションに繋げたい
    - 1リンクだと繋がらない？
- 先入観を植え付ける可能性があるのが恐い
- 分析手法に
- 国の文化が横並びに比較できるのか不安
    - 企業もだめそう
- TVとニュースサイトの比較
- 国は政治問題になるから怪しい？
- 分析結果をリプライするbot
- デンドログラムごとにリンク
- 推薦システム
    - 先輩 ホテルのコメントの皮肉文
- ~~他の〇〇はこう書いてる~~
    - ~~ポップアップで全体表示~~
- 実装から入らないように
- CNNとNHKならOK BBC

### 亀川
- 休み
    - 振替（20210609）
        - AEsの問題点
            - 人間と機械とで判断方法が異なる
            - 攻防のいたちごっこ
                - なぜそうなるかを詰める
                - 入力の微妙な差が出力に大きな差
                    - 人間と機械とのギャップ
            - ATベースの防御が最も有効
                - AEsには頑健だが、標準画像に弱い
                - 訓練していないAEsには弱い
        - なぜオントロジーが必要になるのか詰める

### 志田
- 夜間の車両検知
    - CNNの検知制度を予備実験
    - 夜間+雨の反射も考慮？
        - 前処理で外しても良い
    - 白飛び
    - 光の強度から距離が出せるか
- 夜間の光で歩行者が消える「蒸発現象（グレア現象）」もこわい
    - https://www.ms-ins.com/labo/higoro/article/20181025.html
    - データセットの国は

### 土屋
- 身振り手振り、顔の動きは難しそう
    - 視線、顔や身体の向きを利用
    - 周囲の人物からの注目、頷きを利用
- 全方向カメラマイクで集団会議のリアルタイム分析
    - VFOA（視覚的注目度）
    - VAD（誰が話したか）
    - DOA
    - 話者認識
    - 音源クラスタリング
- 日本の会議は資料ばかり見ている
    - ブレストなどを想定するとよさそう
- 聞き手の頷きを利用？
    - 聞き手がリアクションしない可能性も考慮

### 平山
- スケジュール立てた
    - 手法の考案も追加
- 式が分からない
    - 背後の目的は難しくないことが多い
        - これを前提に推測
- 自分で実装してみている
    - python
    - 実装よりまず論文を読むと良い

### 増岡
- 画像解析による雑草検出
    - 安価な設備
    - 対象植物に特化
        - 対象の植物の葉以外の緑を雑草とする
            - 緑なら雑草？
                - 実も緑である可能性
                - ゴーヤの隣のネギが雑草に
    - セマンティックセグメンテーションが近い？

### 松本
- 論文タイトル推薦
    - 特定フレーズの抽出
        - we
        - in this paper
            - 概要でなく前提を話されることも
            - AbstructとIntroductionだけで良さそう
            - 手法は入れるか迷う
    - ROUGE
        - 元と生成の一致度
        - 調べて教えて
    - PEGASUS
        - Transformerの要約
    - いきなりクローリングせずにまずは手動
        - バグがあるとこわい
        - DOS攻撃してIP BANされた経験も
        - 手動でもBANされるので注意

### モ
- 画像認識を利用した動画推薦
    - 動画の魅力
        - 趣味は関係ない
        - サムネなどから気を引くか
        - 何を認識すると優先度が高くなる
    - 内容面白いのにサムネがダメで推薦されないのは残念
        - Video2Vecは間に合うかわからない？
            - 3年やるから頑張れば？

### 原田
- 欠損値の対処
    - MissForest法
        - ランダムフォレスト
        - 反復ごとに
        - 欠損の数が違う
    - ハナンさんの論文を読んで
    - 古いのでDLでできないか考える
    - 1度批判的に読む

## 気になったこと
- 

## 業務連絡
- 相談会出れない
- 水曜3限は空いている

