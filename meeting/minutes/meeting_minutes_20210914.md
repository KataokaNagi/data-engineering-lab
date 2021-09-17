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

# 報告会 議事録 2021年09月14日

## 報告

### 片岡
- 本当に700件に50万文字？
    - 日本語で195万文字
    - 16バイトで割ってみる
- データセットサーチ
    - 既に日本語に変換されてる英語を使ってみては
    - 理想的には同じ翻訳機を使ってる複数言語
- モデルの重みの保存
    - テンサーフローは手動で設定が必要なはず
    - 自分のクラス
        - クラウドピックル
        - DLには向かない？
            - テンサーフローは不明
            - パイトーチは
                - 横展開
            - kerasにSaveというメソッドがある
                - 公式ドキュメント
    - 卒研１の分類をかけてみる

### 亀川
- 

### 志田
- 関連研究は1週間強で
- CUDAの設定が完了

### 土屋
- リモートの設定
    - xrdpがうまくいかない
    - vncも微妙
- 環境のバックアップは大事
- CUDAの設定が完了

### 平山
- 

### 増岡
- データ拡張（Data Augumentation）の調査
    - Mixup
    - Cutout
    - CutMix
        - これらより良い物を作るのが研究
- 画像処理ライブラリは何を使うか
    - OpenCV
        - C++なのでメモリ開放に注意が必要
    - pillow
        - python

### 松本
- 

### モ
- https://ainow.ai/2020/03/02/183280/

### 原田
- 

## 気になったこと
- 

## 業務連絡
- 木曜に先生と先輩が研究室掃除
    - IPアドレスを公開
    - NASの再起動
    - labという名前で
