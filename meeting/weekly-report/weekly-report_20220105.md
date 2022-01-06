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

# 週次報告書 2022年01月05日
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
- covidのEとCを比較
- epochを変えて比較
    - 4epochs(前回)
        - {'mcc': 0.8164008811069239, 'tp': 379, 'tn': 791, 'fp': 60, 'fn': 45, 'auroc': 0.9706338824468438, 'auprc': 0.9305744848173877, 'eval_loss': 0.2970533335633263, 'acc': 0.9176470588235294}
    - 3epoch
        - {'mcc': 0.8306606574490791, 'tp': 389, 'tn': 788, 'fp': 63, 'fn': 35, 'auroc': 0.9674314901447797, 'auprc': 0.8984210954225702, 'eval_loss': 0.2356283680874185, 'acc': 0.9231372549019607}
    - 2epochs
        - {'mcc': 0.8173129764924434, 'tp': 382, 'tn': 788, 'fp': 63, 'fn': 42, 'auroc': 0.9713835554175998, 'auprc': 0.9251588809193649, 'eval_loss': 0.2068871846249749, 'acc': 0.9176470588235294}
- imbalanced dataは再現率が良い
    - 少数派のクラスのインスタンスを検出したいという状況では、たいていの場合適合率よりも再現率を強く考慮
        - 検出という文脈では、負例に誤ったラベルを付けるよりも、正例を見逃す方がコストがかかるから
        - https://qiita.com/r-takahama/items/631a59953fc20ceaf5d9
- MCC(マシューズ相関係数)
    - どのクラスが正であるかに依存しない
    - 少数クラスを正にすることを考慮することに不慣れならおすすめ
    - 正負が不均衡なデータでの２値分類モデルの精度の評価にはマシューズ相関係数を使用するのが一般的
    - https://www.datarobot.com/jp/blog/matthews-correlation-coefficient/
    - 実際いくつが良いのか
    - 一見良さそうでも悪く出すことも
        - 式の意味を上手く言えない
        - https://qiita.com/mmmmm1202/items/a4628bc549288f4dee33
- 少数派のCを正例として精度を検証
    - 再現率が2割超えない...
    - 手動ラベルを調節する予定
    - 上層NNだけ学習するべき？
