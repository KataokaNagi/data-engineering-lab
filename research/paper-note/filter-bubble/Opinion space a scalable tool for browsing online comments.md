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

# 論文要約 『Opinion space: a scalable tool for browsing online comments』

- 20210607
- [1]S. Faridani, E. Bitton, K. RyokaiとK. Goldberg, 「Opinion space: a scalable tool for browsing online comments」, Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, New York, NY, USA, 4月 2010, pp. 1175–1184. doi: 10.1145/1753326.1753502.

<!-- -------------------- -->

## 概要
- ネットのコメント
    - 時間や2段階評価で最適化
        - サイバーポラライぜーションを助長
- Opinion space
    - 多様なコメントを視覚化するオンラインインターフェース
        - 審議型投票
        - 次元削減
        - 協調フィルタリング
    - 洞察力に富んだコメントをハイライト
    - 同じ多様さでも、同意と敬意が向上

## 図
- インタラクティブマップ
    - 各ポイントはユーザーとコメント
    - 緑は肯定、赤は否定
    - 大きいほど評価が大きい
- 5つの意見の賛成度をスライダーで入力
    - テキストも入力
- 賛否と尊敬度のスライダー
- 2dから3dの次元削減
- 時間順にリストアップ
- 時系列にグリッド表示
- 被験者12名の特徴、平均
- 各UIの楽しさ、面白さ、便利さを５段階評価
- 3つのUIの順位付け
- UIへの意見

<!-- -------------------- -->

## DESIGN OF OPINION SPACE 1.0 

### ユーザーの活動 

### コメントの閲覧と評価 
- 加重平均
- PCA
    - 二乗誤差を最小にする投影を見つけ
    - 新しいユーザの位置を一定時間で計算できる
- 検討
    - 因子分析
    - 多次元尺度構成法（MDS）
    - 特異値分解
    - 射影追跡
    - 独立成分分析
    - t-Distributed Stochastic Neighbor Embedding
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

## 議論と結論
- コメントの数が増えるとユーザーは読めない
    - スペースやグリッドの方が注視される
    - スペースの方が同意・尊敬される
    - 

### 今後の課題
- ユーザータイプ
    - 1）最も洞察力のあるコメントを素早く見つけて読みたいカジュアルユーザー
    - 2）他の参加者から尊敬されるような雄弁なコメントを投稿したい「著者」
    - 3）他の多くの人のコメントを評価することで、空間を形成する役割を認めてもらいたい「ゲーマー」

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

