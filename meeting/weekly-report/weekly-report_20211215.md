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

# 週次報告書 2021年12月15日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 分類
    - Epoc数の変更と分析
- ~~クラスタリングの実装~~
    - 出来事の文章の特徴量ベクトルを作成
    - 主張の文の特徴量ベクトルを作成
    - 3カ国の記事を結合して保存
    - [e-feature-array]を基に記事（行）をクラスタリング
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定

## 2. 実施内容

### 目次
- 2.1 学習を最適化するwandbの修正
- 2.2 IBMのデータセットの論文を参照
- 2.3 エポック数を減らして主張と出来事の分類
- 2.4 IBMのデータセットをStanzaで文章分割
- 2.5 IBMのデータセットの重複データを削除

### 2.1 学習を最適化するwandbの修正
先週格闘した学習を最適化するwandbのエラーが宣言関係の凡ミスであり、修正後に出た新たなエラーと再度格闘した。
最終的に以下のエラーを解決する有効な手段が見つからず、再度断念することとなった。

```
ERROR Detected 3 failed runs in the first 60 seconds, killing sweep. wandb: To disable this check set WANDB_AGENT_DISABLE_FLAPPING=true
```

WANDB_AGENT_DISABLE_FLAPPINGが公式ドキュメントで見当たらず、エラー全体を調査しても解決に至った例が見当たらなかった。

なお、SimpleTransformersはデフォルトでAdamWが利用されているようであり、学習率の調整は不要だと判断した。

### 2.2 IBMのデータセットの論文を参照
主張と出来事の分類ラベルについて、データセット作成者の基準を知るべく作成者の論文を半分ほど参照した。

[1]R. Rinott, L. Dankin, C. Alzate Perez, M. M. Khapra, E. AharoniとN. Slonim, 「Show Me Your Evidence - an Automatic Method for Context Dependent Evidence Detection」, Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, Lisbon, Portugal, 2015, pp. 440–450. doi: 10.18653/v1/D15-1050.

IBMのデータセットは、主張の文とそれを裏付ける根拠の文というニュアンスでデータを集めていた。
また、トピックを「議論の枠組みとなる短いフレーズ」、主張を「トピックを直接サポートまたはテストする一般的で簡潔なステートメント」、根拠を「トピックの文脈の中で主張を直接サポートするテキストセグメント」と定義していた。
> - Topic: a short phrase that frames the discussion.
> - Claim: a gen-eral, concise statement that directly supports or con-tests the topic.
> - Context Dependent Evidence (CDE): a text segment that directly supports a claim in the con-text of the topic

私の研究では「人によって意見の変わらない事実」を出来事とし、「その出来事に対する意見」を主張としており、出来事（根拠）と主張を考える順序が逆である。
また、IBMのいう主張をサポートする文というのは、人によって意見の変わる事柄を許容しており、私の基準とは少し差異がある。

論文で作成されたシステムでは、Wikipediaの広い分野の記事を解析し、別で入力された主張の文との関連度でランク付けされた主張のリストを出力していた。
記事の種類は異なるが、目的が本研究と類似したデータセットである。

データセットは、弁護士や政治家の意志決定支援、説得力向上、議論の準備など、広い応用が可能であるとしている。
本研究での分類とは異なる応用例が出されており、本研究に適用できるかはこの記述からは推測できない。

総合的に理想のデータとは言えないが、「人によって意見の変わらない事実」を出来事とし、「その出来事に対する意見」を主張とする基準でどの程度適用できるかを検証しがいのあるデータだと考えた。

### 2.3 エポック数を減らして主張と出来事の分類
先週の分類をエポック数を減らして実行した。
1エポックで過学習かと思えるレベルの適合率99.94になり、39件中28件（71.8%）と最も高い正答率となった。

しかしこの後、出来事の文が1行に数文あり、重複行も多いことに気付き、追加の前処理が必要だと考えた。

記事ID | 推測 | 未処理 10エポ | 10エポ | 5エポ | 3エポ | 2エポ | 1エポ |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| IN-01 | E | E | E | E | E | E | E |
| IN-02 | E | E | C | C | E | E | E |
| IN-03 | E | E | E | E | E | E | E |
| IN-04 | E | E | E | E | E | E | E |
| IN-05 | E | E | E | E | E | E | E |
| IN-06 | E | E | C | C | E | E | E |
| IN-07 | E | E | E | E | E | E | E |
| IN-08 | E | E | E | E | E | E | E |
| IN-09 | E | E | E | E | E | E | E |
| IN-10 | C | E | E | E | E | E | E |
| JP-01 | E | E | E | E | E | E | C |
| JP-02 | E | E | E | E | E | E | E |
| JP-03 | E | E | E | E | E | E | E |
| JP-04 | C | E | C | C | C | C | C |
| JP-05 | E | E | C | C | E | C | E |
| JP-06 | E | E | E | E | E | E | E |
| JP-07 | E | E | E | E | E | E | E |
| JP-08 | E | C | C | C | C | C | C |
| JP-09 | E | E | E | E | E | E | E |
| JP-10 | E | E | C | C | C | C | C |
| JP-11 | E | E | E | C | E | E | E |
| JP-12 | E | E | E | E | E | E | E |
| JP-13 | C | E | E | C | E | E | E |
| JP-14 | E | E | E | E | E | E | E |
| JP-15 | E | C | C | C | C | C | C |
| JP-16 | E | E | E | E | E | E | E |
| JP-17 | E | E | E | E | E | E | E |
| KR-01 | E | E | E | E | E | E | E |
| KR-02 | E | E | E | E | E | E | E |
| KR-03 | C | E | E | E | E | E | E |
| KR-04 | C | E | E | E | E | E | E |
| KR-05 | E | E | E | E | E | E | E |
| KR-06 | E | E | E | E | E | E | E |
| KR-07 | C | E | E | E | E | E | E |
| KR-08 | C | E | C | C | E | C | C |
| KR-09 | C | E | E | E | E | E | E |
| KR-10 | E | E | E | E | E | E | E |
| KR-11 | E | E | E | E | E | E | E |
| KR-12 | C | E | E | E | E | E | E |
| 正解数 | 39 | 28 | 26 | 26 | 27 | 27 | 28 |
| 正解率 | 100 | 71.8 | 66.7 | 66.7 | 69.2 | 69.2 | 71.8 |
| acc | - | 99.6 | 99.5 | 99.3 | 99.4 | 99.4 | 99.4 |
| prc | - | 99.996 | 99.8 | 99.95 | 99.95 | 99.96 | 99.94 |


### 2.4 IBMのデータセットをStanzaで文章分割
covid-19-articlesの文章分割で利用したコードを改変し、IBMのデータセットの文章をStanzaによって分割した。

### 2.5 IBMのデータセットの重複データを削除
DataFrame型の機能を利用し、重複データを削除する実装を進めている。

## 3. 次回までに実施予定であること
- 分類
    - IBMのデータセットの重複データを削除
    - Epoc数の変更と分析
- クラスタリングの実装
    - 出来事の文章の特徴量ベクトルを作成
    - 主張の文の特徴量ベクトルを作成
    - 3カ国の記事を結合して保存
    - [e-feature-array]を基に記事（行）をクラスタリング
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
- 論文執筆
- 評価方法の検討

## 4. 気になったこと
本の図表をスキャンして論文に記載することは可能か

## 5. メモ
- simpletransformerの中身はpytorch
- wandbの修正
    - trainの引数をグローバル変数に
        - 記事に合わせた
        - Dataframeのエラーが消えた
    - train()内のmodel変数がmain()で未定義だった
    - paramのエラーだと思っていたものは関係ない警告だった
        - Some weights of the model checkpoint at roberta-base were not used when initializing RobertaForSequenceClassification: ['roberta.pooler.dense.bias', 'roberta.pooler.dense.weight', 'lm_head.layer_norm.bias', 'lm_head.dense.bias', 'lm_head.decoder.weight', 'lm_head.dense.weight', 'lm_head.layer_norm.weight', 'lm_head.bias']
        - https://github.com/huggingface/transformers/issues/5421
            - この警告は、トレーニング中、損失を計算するためにプーラーを使用していないことを意味します。あなたがどのようにモデルを微調整しているのかわかりませんが、プーラー層を使用していないのであれば、この警告を気にする必要はありません。
    - this is just a remark by the Huggingface library - no need to worry. We are using the BERT implementation of Huggingface internally. You are doing everything correctly here. When executing the train code (as you do), you train JEREX (and fine-tune into BERT) on a down-stream task (end-to-end relation extraction) and you can then use the model for prediction.
        - 関係ない警告である可能性あり
            - https://github.com/lavis-nlp/jerex/issues/2
    - overwrite_output_dirのエラー
        - Output directory (outputs/) already exists and is not empty. Set overwrite_output_dir: True to automatically overwrite.
        - ClassificationModelではTrueにはしている
        - 削除すれば良さそう
            - https://meknowledge.jpn.org/2021/06/09/nlp-disease-prediction/
    - 'NoneType' object has no attribute 'eval_model'
        - オプティマイズに評価は不要なのでコメントアウト
    - global変数はNone代入ではなくglobal [var] で宣言？
        - それでもmodelがないと言われる
        - main()を削除
    - ERROR Detected 3 failed runs in the first 60 seconds, killing sweep. wandb: To disable this check set WANDB_AGENT_DISABLE_FLAPPING=true
        - 標準出力に詳細がない
        - pl v1.5.0のエラー？
            - https://github.com/PyTorchLightning/pytorch-lightning/discussions/9589
    - 環境差があるらしいのでColabに移植したがまたエラー
    - ClassificationModelにadamの引数があるらしい
        - adam_epsilon 	float 	1e-8 	Epsilon hyperparameter used in AdamOptimizer.
        - optimizer 	str 	“AdamW” 	Should be one of (AdamW, Adafactor)
        - https://simpletransformers.ai/docs/usage/
        - 既にAdamWが設定されていそう？
            - Configuration options in Simple Transformers are defined as either dataclasses or as Python dicts. The ModelArgs dataclass contains all the global options set to their default values, as shown below.
    - wandbのアルゴリズム
        - ベイズ最適化
    - 成功失敗がわかる
        - https://wandb.ai/home
    - 断念
- エポック変更
    - 5エポック
        - {'mcc': 0.9835173305141509, 'tp': 440, 'tn': 947, 'fp': 4, 'fn': 6, 'auroc': 0.9997783781999595, 'auprc': 0.9995269343803318, 'eval_loss': 0.04620989467784446, 'acc': 0.9928418038654259}
    - 3エポック
        - {'mcc': 0.985164001344327, 'tp': 440, 'tn': 948, 'fp': 3, 'fn': 6, 'auroc': 0.9997972396297501, 'auprc': 0.9995704548694677, 'eval_loss': 0.03722071185545896, 'acc': 0.9935576234788833}
    - 2エポック
        - {'mcc': 0.9868462989086224, 'tp': 443, 'tn': 946, 'fp': 5, 'fn': 3, 'auroc': 0.9997948819510263, 'auprc': 0.999562300340803, 'eval_loss': 0.034398133022561006, 'acc': 0.9942734430923408}
    - 1エポック
        - {'mcc': 0.9885396559460051, 'tp': 445, 'tn': 945, 'fp': 6, 'fn': 1, 'auroc': 0.9997147208744159, 'auprc': 0.9993830203229274, 'eval_loss': 0.03136897643986491, 'acc': 0.9949892627057981}
- IBMの論文
    - [1]R. Rinott, L. Dankin, C. Alzate Perez, M. M. Khapra, E. AharoniとN. Slonim, 「Show Me Your Evidence - an Automatic Method for Context Dependent Evidence Detection」, Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing, Lisbon, Portugal, 2015, pp. 440–450. doi: 10.18653/v1/D15-1050.
- C-Eのデータに改行が必要

記事ID | 推測 | 未処理 10エポ | 10エポ | 5エポ | 3エポ | 2エポ | 1エポ |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| IN-01 | E | E | E | E | E | E | E |
| IN-02 | E | E | C | C | E | E | E |
| IN-03 | E | E | E | E | E | E | E |
| IN-04 | E | E | E | E | E | E | E |
| IN-05 | E | E | E | E | E | E | E |
| IN-06 | E | E | C | C | E | E | E |
| IN-07 | E | E | E | E | E | E | E |
| IN-08 | E | E | E | E | E | E | E |
| IN-09 | E | E | E | E | E | E | E |
| IN-10 | C | E | E | E | E | E | E |
| JP-01 | E | E | E | E | E | E | C |
| JP-02 | E | E | E | E | E | E | E |
| JP-03 | E | E | E | E | E | E | E |
| JP-04 | C | E | C | C | C | C | C |
| JP-05 | E | E | C | C | E | C | E |
| JP-06 | E | E | E | E | E | E | E |
| JP-07 | E | E | E | E | E | E | E |
| JP-08 | E | C | C | C | C | C | C |
| JP-09 | E | E | E | E | E | E | E |
| JP-10 | E | E | C | C | C | C | C |
| JP-11 | E | E | E | C | E | E | E |
| JP-12 | E | E | E | E | E | E | E |
| JP-13 | C | E | E | C | E | E | E |
| JP-14 | E | E | E | E | E | E | E |
| JP-15 | E | C | C | C | C | C | C |
| JP-16 | E | E | E | E | E | E | E |
| JP-17 | E | E | E | E | E | E | E |
| KR-01 | E | E | E | E | E | E | E |
| KR-02 | E | E | E | E | E | E | E |
| KR-03 | C | E | E | E | E | E | E |
| KR-04 | C | E | E | E | E | E | E |
| KR-05 | E | E | E | E | E | E | E |
| KR-06 | E | E | E | E | E | E | E |
| KR-07 | C | E | E | E | E | E | E |
| KR-08 | C | E | C | C | E | C | C |
| KR-09 | C | E | E | E | E | E | E |
| KR-10 | E | E | E | E | E | E | E |
| KR-11 | E | E | E | E | E | E | E |
| KR-12 | C | E | E | E | E | E | E |
| 正解数 | 39 | 28 | 26 | 26 | 27 | 27 | 28 |
| 正解率 | 100 | 71.8 | 66.7 | 66.7 | 69.2 | 69.2 | 71.8 |
| acc | - | 99.6 | 99.5 | 99.3 | 99.4 | 99.4 | 99.4 |
| prc | - | 99.996 | 99.8 | 99.95 | 99.95 | 99.96 | 99.94 |
