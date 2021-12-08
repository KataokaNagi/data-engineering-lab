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

# 週次報告書 2021年12月08日
AL18036 片岡 凪

## 1. 今回の報告会までに実施する予定だったこと
- 卒論の目次作成
- IBMの前処理
- 分類結果を吟味
    - 前処理の有無
    - ~~エポック数を変えて~~
- ~~クラスタリングの実装~~
    - 出来事の文章の特徴量ベクトルを作成
    - 主張の文の特徴量ベクトルを作成
    - 3カ国の記事を結合して保存
    - [e-feature-array]を基に記事（行）をクラスタリング
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
- ~~評価方法の検討~~

## 2. 実施内容

### 目次
- 2.1 IBM Debater Datasertを前処理して比較
- 2.2 モデルの最適化（半ば断念）
- 2.3 目次の作成

### 2.1 IBM Debater Datasertを前処理して比較

前回報告した出来事と主張の分類では、前処理していないIBM Debater Datasertで分類器を学習し、前処理したcovid-19-articlesを分類していた。
この前処理の有無によって精度が下がっていると考え、IBM Debater Datasertにもcovid-19-articlesとほぼ同様の前処理を行い、分類を行った。
IBM Debater Datasertに限り、[REF]タグの除去や文末のピリオドの追加を行っている。

<!-- 分類の結果、前処理しない分類では少なかった「主張と分類する例」が6件増加し、その他の分類結果は一致した。 -->
<!-- 6件の主張の分類のうち2件は正答しており -->
<!-- 主張とも言えなくもない文はあったか -->

分類の結果、2件の誤分類が増加し、正しい分類は39件中26件（66.7%）となった。
分類モデルの適合率が99.8%であり、過学習が疑われるため、エポック数を減らす予定である。

※前回の分類で39件中21件（約53.8％）のエラー（正解は46.2%）とお伝えしてしまいましたが、正しくは39件中11件（約28.2％）のエラー（正解は71.8%）でした。


記事ID | 推測 | 未処理 10エポ | 10エポ | 5エポ | 3エポ |
|:----:|:----:|:----:|:----:|:----:|:----:|
| IN-1 | E | E | E |  |  |
| IN-2 | E | E | C |  |  |
| IN-3 | E | E | E |  |  |
| IN-4 | E | E | E |  |  |
| IN-5 | E | E | E |  |  |
| IN-6 | E | E | C |  |  |
| IN-7 | E | E | E |  |  |
| IN-8 | E | E | E |  |  |
| IN-9 | E | E | E |  |  |
| IN-10 | C | E | E |  |  |
| JP-1 | E | E | E |  |  |
| JP-2 | E | E | E |  |  |
| JP-3 | E | E | E |  |  |
| JP-4 | C | E | C |  |  |
| JP-5 | E | E | C |  |  |
| JP-6 | E | E | E |  |  |
| JP-7 | E | E | E |  |  |
| JP-8 | E | C | C |  |  |
| JP-9 | E | E | E |  |  |
| JP-10 | E | E | C |  |  |
| JP-11 | E | E | E |  |  |
| JP-12 | E | E | E |  |  |
| JP-13 | C | E | E |  |  |
| JP-14 | E | E | E |  |  |
| JP-15 | E | C | C |  |  |
| JP-16 | E | E | E |  |  |
| JP-17 | E | E | E |  |  |
| KR-1 | E | E | E |  |  |
| KR-2 | E | E | E |  |  |
| KR-3 | C | E | E |  |  |
| KR-4 | C | E | E |  |  |
| KR-5 | E | E | E |  |  |
| KR-6 | E | E | E |  |  |
| KR-7 | C | E | E |  |  |
| KR-8 | C | E | C |  |  |
| KR-9 | C | E | E |  |  |
| KR-10 | E | E | E |  |  |
| KR-11 | E | E | E |  |  |
| KR-12 | C | E | E |  |  |
| 正解数 | 39 | **28** | 26 |  |  |
| 正解率 | 100 | 71.8 | 66.7 |  |  |
| acc | - | 99.6 | 99.5 |  |  |
| prc | - | 99.996 | 99.8 |  |  |


### 2.2 モデルの最適化（半ば断念）

エポック数を少なくすることを考えた際、ライブラリによって自動で最適化できないかと考えた。
軽く調査を行ったところ、用いたTransformerライブラリに適した[Weights＆Biases(wandb)](https://note.com/npaka/n/n298f269c2275)というサービスを見つけた。
wandbでは、エポック数だけでなく最適な学習率まで定めることができ、分類精度の向上が期待できる。

短いコードですぐに実装できたが、以下のエラーが発生した。
モデルの初期化の際に多数の重みが設定されていないことや、ダウンストリームタスクで訓練していない（？）ことや、DataFrame型の引数指定が正しくないなどのエラーである。

いくつかの技術記事や公式リファレンスで記述の差が激しい事や、見慣れないエラーが多いことから、修正には長い時間がかかると判断した。
報告会や相談会ですぐに解決しない場合、実装は後回しにし、5, 3 (, 7)エポックを試す予定である。
7エポックは、5エポックから3エポックにした際に精度が低減した場合に実行する。

```
*** train & evaluate model ***
Create sweep with ID: gb4a5zpd
Sweep URL: https://wandb.ai/kataoka-nagi/RTE%20-%20Hyperparameter%20Optimization/sweeps/gb4a5zpd
NUM_EPOCHS: 10
MODEL_SEED: 2021
CLASSIFICATION_MODEL_TYPE: roberta
CLASSIFICATION_MODEL_NAME: roberta-base
wandb: Tracking run with wandb version 0.12.7
wandb: Syncing run wild-durian-1
wandb: ⭐️ View project at https://wandb.ai/kataoka-nagi/RTE%20-%20Hyperparameter%20Optimization
wandb: 🚀 View run at https://wandb.ai/kataoka-nagi/RTE%20-%20Hyperparameter%20Optimization/runs/25olfk2s
wandb: Run data is saved locally in /home/nagi/Documents/git/data-engineering-lab/experiment/wandb/run-20211206_083148-25olfk2s
wandb: Run `wandb offline` to turn off syncing.
Some weights of the model checkpoint at roberta-base were not used when initializing RobertaForSequenceClassification: ['roberta.pooler.dense.weight', 'roberta.pooler.dense.bias', 'lm_head.bias', 'lm_head.layer_norm.weight', 'lm_head.dense.weight', 'lm_head.layer_norm.bias', 'lm_head.dense.bias', 'lm_head.decoder.weight']
- This IS expected if you are initializing RobertaForSequenceClassification from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
- This IS NOT expected if you are initializing RobertaForSequenceClassification from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).
Some weights of RobertaForSequenceClassification were not initialized from the model checkpoint at roberta-base and are newly initialized: ['classifier.dense.weight', 'classifier.out_proj.weight', 'classifier.out_proj.bias', 'classifier.dense.bias']
You should probably TRAIN this model on a down-stream task to be able to use it for predictions and inference.
/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_model.py:586: UserWarning: Dataframe headers not specified. Falling back to using column 0 as text and column 1 as labels.
  "Dataframe headers not specified. Falling back to using column 0 as text and column 1 as labels."
INFO:simpletransformers.classification.classification_utils: Converting to features started. Cache is not used.

Traceback (most recent call last):
  File "process_01_train_classifier_as_claim_or_evidence.py", line 253, in <module>
    main()
  File "process_01_train_classifier_as_claim_or_evidence.py", line 214, in main
    wandb.agent(sweep_id, train(train_df, eval_df, model_args))
  File "process_01_train_classifier_as_claim_or_evidence.py", line 243, in train
    overwrite_output_dir=True)
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_model.py", line 593, in train_model
    train_examples, verbose=verbose
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_model.py", line 1806, in load_and_cache_examples
    no_cache=no_cache,
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_utils.py", line 258, in __init__
    data, tokenizer, args, mode, multi_label, output_mode, no_cache
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_utils.py", line 197, in build_classification_dataset
    labels = [args.labels_map[label] for label in labels]
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_utils.py", line 197, in <listcomp>
    labels = [args.labels_map[label] for label in labels]
KeyError: 1.0
Traceback (most recent call last):
  File "process_01_train_classifier_as_claim_or_evidence.py", line 253, in <module>
    main()
  File "process_01_train_classifier_as_claim_or_evidence.py", line 214, in main
    wandb.agent(sweep_id, train(train_df, eval_df, model_args))
  File "process_01_train_classifier_as_claim_or_evidence.py", line 243, in train
    overwrite_output_dir=True)
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_model.py", line 593, in train_model
    train_examples, verbose=verbose
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_model.py", line 1806, in load_and_cache_examples
    no_cache=no_cache,
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_utils.py", line 258, in __init__
    data, tokenizer, args, mode, multi_label, output_mode, no_cache
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_utils.py", line 197, in build_classification_dataset
    labels = [args.labels_map[label] for label in labels]
  File "/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_utils.py", line 197, in <listcomp>
    labels = [args.labels_map[label] for label in labels]
KeyError: 1.0
wandb: Waiting for W&B process to finish, PID 6393... (failed 1). Press ctrl-c to abort syncing.
wandb: - 0.00MB of 0.00MB uploaded (0.00MB deduped)
wandb: \ 0.00MB of 0.00MB uploaded (0.00MB deduped)
wandb: | 0.00MB of 0.01MB uploaded (0.00MB deduped)
wandb: / 0.00MB of 0.01MB uploaded (0.00MB deduped)
wandb: - 0.00MB of 0.01MB uploaded (0.00MB deduped)
wandb: \ 0.01MB of 0.01MB uploaded (0.00MB deduped)
wandb: | 0.01MB of 0.01MB uploaded (0.00MB deduped)
wandb: / 0.01MB of 0.01MB uploaded (0.00MB deduped)
wandb: - 0.01MB of 0.01MB uploaded (0.00MB deduped)
wandb: \ 0.01MB of 0.01MB uploaded (0.00MB deduped)
wandb: | 0.01MB of 0.01MB uploaded (0.00MB deduped)
wandb:                                                                                
wandb: Synced 5 W&B file(s), 0 media file(s), 0 artifact file(s) and 0 other file(s)
wandb: Synced wild-durian-1: https://wandb.ai/kataoka-nagi/RTE%20-%20Hyperparameter%20Optimization/runs/25olfk2s
wandb: Find logs at: ./wandb/run-20211206_083148-25olfk2s/logs/debug.log
wandb: 
```

（↓主要なエラーのDeepL翻訳）
```
roberta-baseのモデルチェックポイントのいくつかの重みが、RobertaForSequenceClassificationの初期化時に使用されませんでした。['roberta.pooler.dense.weight', 'roberta.pooler.dense.bias', 'lm_head.bias', 'lm_head.layer_norm.weight', 'lm_head.dense.weight', 'lm_head.layer_norm.bias', 'lm_head.dense.bias', 'lm_head.decoder.weight'] 。
- これは、他のタスクや他のアーキテクチャでトレーニングされたモデルのチェックポイントからRobertaForSequenceClassificationを初期化している場合に期待されます（例えば、BertForPreTrainingモデルからBertForSequenceClassificationモデルを初期化する場合）。
- これは、全く同一であると予想されるモデルのチェックポイントからRobertaForSequenceClassificationを初期化している場合（BertForSequenceClassificationモデルからBertForSequenceClassificationモデルを初期化している場合）には期待できません。
RobertaForSequenceClassificationのいくつかの重みは、roberta-baseのモデルのチェックポイントからは初期化されず、新たに初期化されます。['classifier.dense.weight', 'classifier.out_proj.weight', 'classifier.out_proj.bias', 'classifier.dense.bias'] 。
このモデルを予測や推論に使えるようにするには、ダウンストリームタスクでTRAINする必要があるでしょう。
/home/nagi/Documents/git/data-engineering-lab/experiment/venv/lib/python3.6/site-packages/simpletransformers/classification/classification_model.py:586: UserWarningです。Dataframeのヘッダが指定されていません。0列目をテキスト、1列目をラベルとして使用することに戻ります。
  "Dataframe headers not specified. 列 0 をテキストとして、列 1 をラベルとして使用することに戻ります。"
INFO:simpletransformers.classification.classification_utils: 機能への変換を開始しました。キャッシュは使用されません。
```



### 2.3 目次の作成
卒業論文の目次の草案を作成した。
作成にあたり、報告書や報告会の議事録、中村先輩と加瀬先輩と疋田先輩の卒論、井尻先生の卒論のテンプレートを参照した。

※括弧内はメモです（節タイトルではありません）
※i -> n.1, a -> n.m.1 と読み替えてください

1.  目次
2.  序論
    1.  研究背景
    2.  研究目的
    3.  本論文の構成
3.  本研究で用いる知識・技術
    1.  ニュース推薦システム
    2.  ニュース推薦システムが生むバイアス
        1.  エコーチェンバー問題
        2.  フィルターバブル問題
    3.  機械学習
        1.  ニューラルネットワーク
        2.  教師あり学習
        3.  Attention（LSTMに触れる）
        4.  Transformer（教師あり分類にも触れる）
        5.  BERT
        6.  RoBERTa（BERTとの比較など）
    4.  文章分類
        1.  テキストの前処理
        2.  単語埋め込み
        3.  Transformer分類器
        4.  分類モデルの評価（acc, prcなどの議論）
    5.  文章の類似度の算出
        1.  Sentence-BERT
        2.  コサイン類似度
    6.  クラスタリング
        1.  非階層クラスタリング
        2.  階層的クラスタリング
        3.  Ward法 
        4.  （その他使用した手法）
        5.  t-SNE (使うかも)
4.  関連研究
    1.  ニュース推薦システムのバイアスの解決
        1.  Breaking the filter bubble: democracy and design
            1.  （UIでバブルの可視化）（結局表示されるものにバイアスがかかる、行動に繋がらない）
            2.  （トピックモデル、LSI, LDAの議論）
    2.  話題の定量化によるニュース推薦手法
        1.  トピックマップ
        2.  Labeled Bilingual Topic Model for Cross-Lingual Text Classification and Label Recommendation
            1.  （LDAの利用）
        <!-- 2.  LSI -->
    1.  （要追加調査：比較評価できる推薦手法）（出来事、主張に着目するシステムなど）
        1.  Investigating COVID-19 News Across Four Nations A Topic Modeling and Sentiment Analysis Approach
            1.  トピックモデル、top2vec, roberta
    <!-- 6.  tf-idf -->
    <!-- SCDV -->
5.  提案手法
    1.  使用する語彙と基準の定義
        1.  文と文章
        2.  出来事の文
        3.  主張の文
        4.  文が示す話題の類似度
    2.  記事の出来事と主張のクラスタを用いた多言語ニュース推薦
        1.  内容
        2.  クラスタリングの順序の検討
6.  実装
    1.  システムの設計指針（入出力、使い方など）
    2.  システム構成（モジュールの説明）
    3.  実装環境（PCスペック、ライブラリバージョンなど）
    4.  データの前処理
        1. 自然言語処理のためのテキストの前処理（前処理の種類、なぜ前処理するのか、awkの正規表現などの議論）
        2. 省略のピリオドに注意した文章の分割（Stanza, spacyの議論）
    5.  出来事の文と主張の文の分類
        1. Simple Transformer
    6.  出来事の文章のクラスタリング
        1.  (要検討)
    7.  主張の文のクラスタリング
        1.  (要検討)
7.  実験
    1.  データセットの選定
        1.  出来事の文と主張の文の分類器の学習データ（IBM Debater Datasetの議論）
        2.  分類とクラスタリングを行うデータ（covid-19-articlesの議論）
            <!-- 1.  Japanese fakenews dataset -->
    2.  出来事の文と主張の文の分類
        1.  実験方法
        2.  実験結果
        3.  （試行錯誤）
    3.  出来事の文章のクラスタリング
        1.  実験方法
        2.  実験結果
        3.  （試行錯誤）
    4.  主張の文のクラスタリング
        1.  実験方法（クラスタの階層の基準ごとの評価）
        2.  実験結果
        3.  （試行錯誤）
    5.  （他の研究との比較実験）
        1.  実験方法
        2.  実験結果
        3.  （試行錯誤）
8.  結果と考察
    1.  既存手法との比較
    2.  提案手法の実用性
        1.  入力と出力の妥当性
        2.  処理速度（分散システムの議論も）
    3.  （結果を基に検討）
9.  まとめと展望
    1.  （結果を基に検討）
    2.  データセットの相性（ディベートとニュース）
10. 謝辞
11. 参考文献


## 3. 次回までに実施予定であること
- 知人＆LINE探し
- 分類
    - Epoc数の変更と分析
- クラスタリングの実装
    - 出来事の文章の特徴量ベクトルを作成
    - 主張の文の特徴量ベクトルを作成
    - 3カ国の記事を結合して保存
    - [e-feature-array]を基に記事（行）をクラスタリング
    - 出来事の記事クラスタからnation-name;article-n;sentence-nで記事を特定
    - 指定した記事クラスタファイルの文を、cの[feature-array]でクラスタリング
    - 主張の文クラスタからnation-name;article-n;sentence-nで文とそのクラスタを特定
- 評価方法の検討

## 4. メモ
- IBMの前処理
    - shを作成
    - awkを作成
        - covidとの差分
            - [REF や [REF] などの除去
            - 末尾にピリオドを追加
    - 学習
        - 10-epoc
            - {'mcc': 0.9885047024316609, 'tp': 444, 'tn': 946, 'fp': 5, 'fn': 2, 'auroc': 0.9993704997807358, 'auprc': 0.9981418495989224, 'eval_loss': 0.04455929614907031, 'acc': 0.9949892627057981}
    - 学習の最適化
        - Weights＆Biases(wandb)の利用
            - https://note.com/npaka/n/n298f269c2275
- 目次
    - 先輩の論文を参照
        - tmp/senior-thesis-idx
    - 報告書と議事録を振り返る
- 104の彼と間接的に連絡
    - ~~105~~
    - ~~107~~
    - 自己紹介でサークルとか言ってたっけ
