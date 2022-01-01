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

# 週次報告書 2021年12月29日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 先生のクラスタリングの論文を拝読

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
- 最小二乗法か交差エントロピーか
    - num_label>1で交差になる
    - 多ラベル分類でも2カラム
        - https://simpletransformers.ai/docs/multi-class-classification/
- バッチ増やした物のeval_lossを見る
    - 4epochs
        - {'mcc': 0.8164008811069239, 'tp': 379, 'tn': 791, 'fp': 60, 'fn': 45, 'auroc': 0.9706338824468438, 'auprc': 0.9305744848173877, 'eval_loss': 0.2970533335633263, 'acc': 0.9176470588235294}
    - 12epochs
        - {'mcc': 0.8061959453861247, 'tp': 377, 'tn': 787, 'fp': 64, 'fn': 47, 'auroc': 0.961162505820012, 'auprc': 0.8900233134115612, 'eval_loss': 0.5898509680812367, 'acc': 0.9129411764705883}
        - lossが上がってしまっている
        - Cが4つ
    - 19epochs
        - 
- クロスバリデーション
    - 自分のモデルでは時間かかりすぎる？
    - 軽くググった感じ用意されてない
- weightリストの要素の対応
    - ref
        - 各ロスの係数にしている
        - どのロスに対応しているかは不明
        - https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html
    - src
        - https://pytorch.org/docs/stable/_modules/torch/nn/modules/loss.html#CrossEntropyLoss
- running lossの平均化の方法
- 基準
    - 片岡
        - 人によってブレがあるか否か
    - IBM
        - 主張を「トピックを直接サポートまたはテストする一般的で簡潔なステートメント」
            - ブレありうる
        - 根拠を「トピックの文脈の中で主張を直接サポートするテキストセグメント」
            - ブレありうる
            - 出来事＝claim, 主張=evidence が逆では
            - トピック自体に偏りがある場合に危険
        - 主張：根拠＝１：２の割合に近くなる
            - 主張の方がトピックをよく代表している？
            - 同じ主張の異なる根拠を集めても面白くない。。。
                - Cの否定語同士の類似度が高くなったら嬉しい
                    - 階層で分けられたらもっと嬉しい
            - この主張の定義だと、主張が無限にあるわけではない？
- ibmとcovidの一部を日訳
    - [covid](../../experiment/covid-19-articles/archive/en.txt)
    - [covid](../../experiment/covid-19-articles/archive/en.txt)
    - [ibm](../../experiment/)
- 正解ラベルの確認、記憶
    - C-Eをセットでラベリングされている
        - CEの繋がりが強いので、EでクラスタリングしたらCも似たようになる？
    - C
        - 主語がデカい
            - 筆者の考え
            - 固有名詞、特定の１つでない
        - 論文の文頭にきそう
        - 長い文もある
        - 言い切り
        - 「また、」
        - ～だったら～
        - ～でしょう
        - ～は当然だ
        - 事実を語るだけでなく、事実に対する説明を行っている
    - E
        - 指示語
        - その結果
            - Cによる影響
        - 数字
        - 事実
        -   判明した
        - 補助的でベクトルの異なる情報が多い
        - ～を求めている
        - を遺憾に思う
        - 主張がある事実を客観視する文
            - メインの主張ではないのかも
            - 主張の文節の後に事実の文節
        - 別の人も似たようなことを言っている　という文
            - メインの主張と似た事を挿すため、代表の主張にする必要はない
            - 出来事のクラスタリングに混ぜるのも悪すぎはしない？
            - 誰かが何かを話しているという「事実」
        - 決意表明157
        - 100文に2文ほど1行2文が存在
            - DeepLによるエラー
- covidのラベル付け
    - cが少ない
        - 書き方によっては主張がない記事がありそう
        - 他者の主張を記事の主張にしたいときCが0となり、システムの目的にそぐわない？
            - 客観視できている記事は偏見がないから無視してよい
    - 記事の代表テーマを扱うわけではないことがある
    - etc.で分割エラー
    - 主語が連続し、省略される際に分類エラーを起こす可能性
    - 別の地域の似た制度に関する情報が得られる可能性
    - 主張に反論する意見をうまく抽出できない可能性
    - 金融系は事実ばかり
- 出来事と主張の文の別のデータセットを調査
    - opinion fact
        - google dataset search 59件は微妙
            - Fact vs Opinion_April 1, 2020_13.02.tab
                - 短い
                - 口語的すぎる
        - paperswitchcode
            - fact verification 5件
                - 事実か否かではない
            - text 3件
                - 裁判やツイート
        - google search
            - [要約問題](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi1k9ybjYb1AhVYk1YBHRWuCP4QFnoECAcQAQ&url=https%3A%2F%2Fgithub.com%2Fmatatusko%2Fopinion-or-fact-sentence-classifier&usg=AOvVaw0WzfQpX_JSP74rfJmKN3l8)
            - [映画](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi1k9ybjYb1AhVYk1YBHRWuCP4QFnoECAkQAQ&url=https%3A%2F%2Fgithub.com%2FMuraliKrishna26%2FOpinion-and-Fact-Classification&usg=AOvVaw1P6yi7OFnmocpa-zcm11el)
    - opinion
        - MPQA
- クラスタリングの論文
- 発表タイトル
    - 主張と根拠のクラスタを用いた偏見を生みにくいニュース推薦手法の提案