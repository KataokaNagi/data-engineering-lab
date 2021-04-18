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

# 論文要約 『XAI(eXplainable AI)技術の研究動向』

- [1]正史恵木, 「XAI(eXplainable AI)技術の研究動向」, 日本セキュリティ・マネジメント学会誌, vol. 34, no. 1, pp. 20–27, 2020, doi: 10.32230/jssmjournal.34.1_20.

$\LaTeX$

<!-- -------------------- -->

## 要旨
- XAI
    - トランスペアレント型
        - 過程と構造が解釈可能
    - ブラックボックス型
        - 既存のモデルの説明
        - 本稿
- Shapley値
- Influence Function

<!-- -------------------- -->

## はじめに
- モデルの説明技術で攻撃できてしまう

<!-- -------------------- -->

## XAIの整理
- ブラックボックス型の分類
    - 局所説明
        - 個々の予想
        - アウトカム説明、インスタンス説明
        - 因子型
            - 各特徴量をどの程度重視したか
        - 事例型
            - 似た特徴量を推測？
        - 知識型
            - 重視する特徴量が専門家と同じか
        - 反実型
            - 予測が変わる特徴量はどれか
    - 大域説明
        - 判断傾向
        - 有効/無効なケース
        - 差別、バイアス
        - モデル検査
            - 局所説明の統計分析
        - モデル説明
            - 簡易モデルに近似・射影

<!-- -------------------- -->

## 技術マップ
- 局所説明
    - Loss関数
        - 微分可能型
        - 微分不可型
    - 因子型と事例型は多い
    - 因子型
        - 微分可能
            - DNN, CNNを逆方向に解析
        - 微分不可能
            - LIME
                - モデルの内部構造に依存しない
                - 勾配ブースティングにも使える
                    - 弱分類器の誤差を引き継いで小さく（Qiita等より）
        - どれも主観評価
            - 協力ゲーム理論のShapley値を活用
                - 主流
                - 応用
                    - 統計検定手法
                    - 高速近似解放
    - 事例型
        - 微分可能
            - Influence Function
                - 誤判定を起こした教師データを定量化

<!-- -------------------- -->

## 局所説明の代表技術
- Shapley値
    - 異なる入力に対する出力の差
        - $f(x)-f\left(x^{\star}\right)=\phi_{1}\left(x, x^{\star}, f\right)+\cdots+\phi_{m}\left(x, x^{\star}, f\right)$
    - への要請
        - 各特徴量の貢献度の差の総和となる
        - 出力の差が起きない2入力の貢献度の差はゼロ
        - 出力の差が等しい2セットの2入力の貢献度の差は等しい
        - 線形結合した予測器の貢献度も線形結合
    - これらの要件を満たす多少複雑な式が求まった
        - $\phi_{i}\left(x, x^{\star}, f\right)=\sum_{S \subseteq M \backslash\{i\}} a_{S}\left\{f\left(z_{S \cup\{i\}}\right)-f\left(z_{s}\right)\right\}$
        - $a_{S}=\frac{|S| !(m-|S|-1) !}{m !}$
        - 純粋数学による導出？
    - 貢献度が独立に分けられたときを前提にしている？
    - 直近の差分しか見ていないと、上がってめちゃ下がる問題が解けないのでは？
    - MNISTのピクセルごとの判別根拠のネガポジを可視化
        - 攻撃可能
- Influence Function
    - 教師データの変化と最適値の変化で同様に定式化
        - $\widehat{\boldsymbol{\theta}}=\operatorname{argmin}_{\boldsymbol{\theta}} \boldsymbol{L}(\boldsymbol{\theta})$
        - $\mathcal{L}(\theta)=\frac{1}{n} \sum_{i}^{n} L\left(z^{(i)} ; \theta\right)$
    - 誤差関数が微分可能なときに、大変な再学習をせずに近似式で最適値の変化を求める手法
    - かなり複雑な式
        - $I\left(z^{\text {test }}, z^{(k)}\right) \sim-\frac{1}{n} \sum_{i=1}^{p} v_{i}\left(z^{\text {test }}\right) u_{i}\left(z^{(k)}\right)$
        - $v_{i}(z)=\left[\begin{array}{c}
\partial L(z, \theta) \\
\partial \theta_{i}
\end{array}\right]_{\theta=\widehat{\theta}}$
        - $u_i$ は $\sum_{j=1}^{p} u_{j}\left[\begin{array}{l}
\partial^{2} \mathcal{L}(\theta) \\
\partial \theta_{i} \partial \theta_{j}
\end{array}\right]_{\theta=\widehat{\theta}}+v_{i}\left(z^{(k)}\right)=0$ の解
    - 教師データの改善
    - 教師データをこっそり変えて攻撃が可能になってしまった

<!-- -------------------- -->

## 所感
- タイトルとは合わない狭く深くのレビュー論文
- カタカナで語義の対応がわかる
    - 鵜呑みに注意
- 文字の係りが複数あって読みにくい
- 数学的発明の手順
    - 問題の定式化
    - 式の要件を列挙
    - 要件を全て満たす式を導出