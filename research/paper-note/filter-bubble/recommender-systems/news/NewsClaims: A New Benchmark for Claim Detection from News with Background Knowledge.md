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

# 論文要約 『NewsClaims: A New Benchmark for Claim Detection from News with Background Knowledge』

- 20220110参照
- [1]R. G. Reddyほか, 「NewsClaims: A New Benchmark for Claim Detection from News with Background Knowledge」, arXiv:2112.08544 [cs], 12月 2021, 参照: 1月 10, 2022. [Online]. Available at: http://arxiv.org/abs/2112.08544

<!-- -------------------- -->

## 概要
- ニュース領域
- 知識認識型クレーム検出のためのベンチマーク
    - NEWSCLAIMS
- クレーム検出問題再定義
    - クレームに関連する背景属性の抽出を含むよう
- 529のクレームを公開
    - 103のニュース記事に対してアノテーション
- 未見のトピックのクレーム検出システムのベンチマーク
- 様々なゼロショットおよびプロンプトベースのベースラインの包括的な評価

<!-- -------------------- -->

## 図表
- 主張の記事の例
- クレーム検出タスクとサブタスク
    - 主張範囲
    - 主張姿勢
    - 主張対象
    - 主張者
- 各トピックのクレームに対応するクレームオブジェクト
- クレーム頻度、トピック、クレームソースの分布に関するデータセットの統計情報
- ゼロショットでトピック分類を行う場合のテンプレートと例
    - 事前学習したMNLI（コーパス）モデルを使用
    - 最もエンタテインメント性の高い仮説に対応するトピックを請求文のトピックとする
- 事前学習済みMNLIモデルの活用例
    - 異なる設定におけるゼロショット姿勢検出のため
    - 仮説が構築の様子
- クレーム検出システムの性能
    - ニュース記事
        - コロナウイルス関連
    - ClaimBuster
    - ClaimBuster＋Zero-shot MNLI
    - Human
- 主張オブジェクト抽出サブタスクに対する異なる数発システムの F1
- 主張クラスと反論クラスのF1とスタンス検出の精度
- クレームの境界の識別性能
- クレーマー抽出のF1
- 請求項が請求項文の中にある場合（文中）と文の外にある場合（文外）の抽出のF1性能


<!-- -------------------- -->

## はじめに
- ニュースなどの主張の検出
    - 誤報を検出に必要
- ニュース記事
    - 様々な主張の形式
        - ジャーナリストによる直接の主張
        - 著名人による引用
        - 報道された発言
- 現在の論証マイニング（Eger et al., 2017; Stab et al., 2018）のアプローチ
    - 主張とその前提の検出ばかりに焦点
        - sup-port/refute関係など
- コードとデータ
    - https://github.com/uiucnlp/NewsClaims/
- 

### 
- 

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

## 
- 

### 
- 

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