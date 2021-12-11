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

# 論文要約 『Show Me Your Evidence - an Automatic Method for Context Dependent Evidence Detection」, Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, Lisbon, Portugal』

- [1]R. Rinott, L. Dankin, C. Alzate Perez, M. M. Khapra, E. AharoniとN. Slonim, 「Show Me Your Evidence - an Automatic Method for Context Dependent Evidence Detection」, Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, Lisbon, Portugal, 2015, pp. 440–450. doi: 10.18653/v1/D15-1050.


<!-- -------------------- -->

## 概要
- 議論は主張->出来事
    - ニュースと逆？
        - 文化に寄りそう
- 主張を裏付ける根拠を非構造化テキストから検出
- 意思決定支援
- 説得力向上
- ベンチマークデータセットの紹介
- 統計モデルのトレーニングとその性能評価
- スーパーバイズド学習に基づくシステム

<!-- -------------------- -->

## 図表
- トピック、主張、出来事の例
    - 論文に使えそう
- 各CDEタイプに含まれるトピックの数
    - E/C=2-3
- CDEDシステムの概略
    - 記事の解析
    - トピックと主張の解析
    - ランク付けされた主張を出力
- 各CDEタイプのマクロ平均MRR（Mean recipro-cal rank）
- マクロ平均のMRR
- タイプStudyのクレーム選択閾値に応じたMRRと平均通過クレーム数の割合
- 「貿易対援助」というテーマでの「援助は非効率的」という主張の上位候補

<!-- -------------------- -->

## はじめに
- 大目的
    - 調べたトピックに関連する議論を自動的に提案
- 論証の最小限の定義（Walton, 2009）
    - 主張（別名：結論、命題）
    - 証拠（別名：前提）
    - 証拠から主張への推論
- フリーテキスト内のエビデンスを識別する能力が必要
    - 証拠検出というタスクを正式に定義
    - 解決するためのアーキテクチャを紹介
    - 手動でラベル付けされたデータを使ってその性能を実証
- 3つの概念(Aharoni et al., 2014)
    - トピック: 議論の枠組みとなる短いフレーズ
    - 主張：トピックを直接サポートまたはテストする一般的で簡潔なステートメント
        - 一般的？
        - 簡潔？
    - Context Dependent Evidence (CDE): トピックの文脈の中で主張を直接サポートするテキストセグメント
- 具体的なトピック、関連する主張、詩的に関連する文書が与えられたと仮定する（Cartright et al.2011; Levy et al.2014）
- 主張は異なる種類の証拠を用いて裏付けることができる(Rieke and Sillars, 2001; Seech, 2008)
- 有効・非有効な CDE
    - 証拠タイプでも主張を裏付けるものではない可能性
    - 主張をサポートしているが、トピックの文脈では無関係
    - 主張を含んでいても、それを裏付ける新しい情報を加えていない場合
- 教師あり学習に依存したパイプラインアーキテクチャを紹介
    - 異なるトピックで学習したモデルが、全く新しいトピックでもそれなりの性能を発揮
- 応用例
    - 弁護士
    - 新しい政策を検討する政治家
    - 意思決定
    - 議論の準備
- 

### 関連研究
- 

### データ
- (Aharoni et al., 2014)の手順で収集
- 5人のアノテーターのうち3人以上が賛同したラベル
- Wikipediaの記事トピックと関連する主張
- アノテーターは対応する証拠をマーク
- さまざまな領域をカバー
    - 無神論から将来のエネルギー供給における風力発電の役割まで
    - Debatabase3から無作為に
    - 無作為に選ばれた39個のトピック
- 274の記事から合計3,057個の異なるCDE
- CDEでない文章が多い
- CDEの長さは、1文未満のものからパラグラフ以上のものまで様々
    - 90％は最大で3文
- ウィキペディアでは、StudyタイプとExpertタイプのCDEがAnecdotal CDEに比べてはるかに多い
    - 科学的ではないコーパスで変化？
- 異なるトピック間のばらつきは非常に大きい
    - Expert CDEを持つクレームの割合
        - ギャンブルを禁止するトピックでは10％
        - メキシコの麻薬戦争に対する米国の責任というトピックでは95％
- Expert、Study、Anecdotal
    - 30、37、22のトピック


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
- 漠然とした出来事というより、主張がある前提の根拠？
    - ～だからだ。とかに敏感？

<!-- -------------------- -->

## 重要ピックアップ
- 
