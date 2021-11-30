# -*- coding: utf-8 -*-
"""transformer-classifier-as-claim-or-evidence.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pMGac5fPC8rgtZVFGy3JnXqjVQSQyO82

# 予備実験「主張を述べる文章と根拠を述べる文章のTransformer分類器」
- [参考：hands-on-ml 16章 Sentiment Analysys](https://github.com/ageron/handson-ml2/blob/master/16_nlp_with_rnns_and_attention.ipynb)

## セットアップ

### Googleドライブのマウント
"""


def main():
    from google.colab import drive
    drive.mount('/content/drive')

    """### hands-on-ml 16章"""

    # Commented out IPython magic to ensure Python compatibility.
    # # Python ≥3.5 is required
    # import sys
    # assert sys.version_info >= (3, 5)

    # # Is this notebook running on Colab or Kaggle?
    # IS_COLAB = "google.colab" in sys.modules
    # IS_KAGGLE = "kaggle_secrets" in sys.modules

    # if IS_COLAB:
    #     !pip install -q -U tensorflow-addons
    #     !pip install -q -U transformers

    # # Scikit-Learn ≥0.20 is required
    # import sklearn
    # assert sklearn.__version__ >= "0.20"

    # # TensorFlow ≥2.0 is required
    # import tensorflow as tf
    # from tensorflow import keras
    # assert tf.__version__ >= "2.0"

    # if not tf.config.list_physical_devices('GPU'):
    #     print("No GPU was detected. LSTMs and CNNs can be very slow without a GPU.")
    #     if IS_COLAB:
    #         print("Go to Runtime > Change runtime and select a GPU hardware accelerator.")
    #     if IS_KAGGLE:
    #         print("Go to Settings > Accelerator and select GPU.")

    # Common imports
    import numpy as np
    import os

    # # to make this notebook's output stable across runs
    # np.random.seed(42)
    # tf.random.set_seed(42)

    # To plot pretty figures
    # %matplotlib inline
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.rc('axes', labelsize=14)
    mpl.rc('xtick', labelsize=12)
    mpl.rc('ytick', labelsize=12)

    # Where to save the figures
    PROJECT_ROOT_DIR = "."
    CHAPTER_ID = "nlp"
    IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
    os.makedirs(IMAGES_PATH, exist_ok=True)

    def save_fig(
            fig_id,
            tight_layout=True,
            fig_extension="png",
            resolution=300):
        path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
        print("Saving figure", fig_id)
        if tight_layout:
            plt.tight_layout()
        plt.savefig(path, format=fig_extension, dpi=resolution)

    """## データのインポート・前処理

    ### データセット概要
    - [IBM Debater® - Claims and Evidence (EMNLP 2015)](https://www.research.ibm.com/haifa/dept/vst/debating_data.shtml#Download)
        - 作品がCC-BY-SAでリリースされていることを示すライセンス表示
            - 権利者の名前を入れる
            - 加工しても同じライセンスで他人にもシェア
            - 商用利用OK
        - a)ライセンスのテキストへのハイパーリンクまたはURL
        - またはb)ライセンスのコピーのいずれかを含める
        - 文末のカンマやクエスチョンマークは除去済み

    ### インポートとテキスト処理
    - 変数
        - claims_data
            - claims.txtの分割した行のリスト
        - evidence_data
            - evidence.txtの分割した行のリスト
        - claims
            - 主張の文のリスト
        - evidence
            - 根拠の文のリスト
    - 前処理
        - 改行文字の除去
        - タブ文字で分割
        - 大文字を小文字に変換
    """

    CLAIMS_DIR = "/content/drive/MyDrive/lab/experiment/transformer-classifier-as-claim-or-evidence/IBM_Debater_(R)_CE-EMNLP-2015.v3/claims.txt"
    EVIDENCE_DIR = "/content/drive/MyDrive/lab/experiment/transformer-classifier-as-claim-or-evidence/IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence.txt"
    CLAIMS_IDX = 2
    EVIDENCE_IDX = 2

    claims_data = []
    evidence_data = []
    claims = []
    evidence = []

    # read
    with open(CLAIMS_DIR, "r", encoding="utf_8") as f:
        lines = f.readlines()
        print("claims.txt lines:")
        print(lines[0])
        print(lines[1])
        print(lines[2])
        print()
        for line in lines[1:]:
            fields = line.rstrip("\n").split("\t")
            claims_data.append(fields)
            claims.append(fields[CLAIMS_IDX])

    with open(EVIDENCE_DIR, "r", encoding="utf_8") as f:
        lines = f.readlines()
        print("evidence.txt lines:")
        print(lines[0])
        print(lines[1])
        print(lines[2])
        print()
        for line in lines:
            fields = line.rstrip("\n").split("\t")
            evidence_data.append(fields)
            evidence.append(fields[EVIDENCE_IDX].lower())

    # print debug
    print("claims_data:")
    print(claims_data[0])
    print(claims_data[1])
    print()

    print("evidence_data:")
    print(evidence_data[0])
    print(evidence_data[1])
    print()

    print("claims:")
    print(claims[0])
    print(claims[1])
    print()

    print("evidence:")
    print(evidence[0])
    print(evidence[1])

    """### ラベリング"""

    CLAIMS_LABEL = 1
    EVIDENCE_LABEL = 0

    if (CLAIMS_LABEL):
        claims_labels = np.ones(len(claims)).tolist()
    else:
        claims_labels = np.zeros(len(claims)).tolist()

    if (EVIDENCE_LABEL):
        evidence_labels = np.ones(len(evidence)).tolist()
    else:
        evidence_labels = np.zeros(len(evidence)).tolist()

    print(claims_labels[0])
    print(evidence_labels[0])

    claims_dataset = []
    evidence_dataset = []

    for idx in range(len(claims)):
        claims_dataset.append([claims[idx], claims_labels[idx]])

    for idx in range(len(evidence)):
        evidence_dataset.append([evidence[idx], evidence_labels[idx]])

    print(claims_dataset[0])
    print(evidence_dataset[0])

    """### 結合"""

    dataset = claims_dataset + evidence_dataset
    print(dataset[0])
    print(dataset[-1])

    """### シャッフル"""

    import random
    random.seed(10)

    random.shuffle(dataset)
    print(dataset[0])
    print(dataset[-1])

    """### 訓練、評価、テストデータに分割"""

    # VALID_RATE = 0.2
    # TEST_RATE = 0.2

    # dataset_num = len(dataset)
    # valid_num = int(dataset_num * VALID_RATE)
    # test_num = int(dataset_num * TEST_RATE)
    # train_num = dataset_num - valid_num - test_num

    # valid_dataset = dataset[:valid_num]
    # test_dataset = dataset[valid_num:valid_num + test_num]
    # train_dataset = dataset[valid_num + test_num:]

    # print("dataset_num: ", dataset_num)
    # print("valid_num: ", valid_num)
    # print("test_num: ", test_num)
    # print("train_num: ", train_num)

    EVAL_RATE = 0.2

    dataset_num = len(dataset)
    eval_num = int(dataset_num * EVAL_RATE)
    train_num = dataset_num - eval_num

    eval_dataset = dataset[:eval_num]
    train_dataset = dataset[eval_num:]

    print("dataset_num: ", dataset_num)
    print("eval_num: ", eval_num)
    print("train_num: ", train_num)

    """## 分類器の作成
    - [Simple Transformers 入門 (1) - テキスト分類 ](https://note.com/npaka/n/nfe2436ea5301#9VV1a)
    - [Simple Transformers 入門 (10) - ハイパーパラメータの最適化 ](https://note.com/npaka/n/n298f269c2275)

    ### Simple Transformerのインストール
    """

    !pip install transformers
    !pip install simpletransformers

    """### モデルの評価まで"""

    from simpletransformers.classification import ClassificationModel, ClassificationArgs
    import pandas as pd
    import logging

    # ログの設定
    logging.basicConfig(level=logging.INFO)
    transformers_logger = logging.getLogger("transformers")
    transformers_logger.setLevel(logging.WARNING)

    # 学習データの作成
    train_df = pd.DataFrame(train_dataset)

    # 評価データの作成
    eval_df = pd.DataFrame(eval_dataset)

    # モデルの作成

    NUM_EPOCHS = 10
    MODEL_SEED = 2021

    model_args = ClassificationArgs()
    model_args.num_train_epochs = NUM_EPOCHS
    # model_args.reprocess_input_data = True
    model_args.manual_seed = MODEL_SEED

    model = ClassificationModel('roberta', 'roberta-base', args=model_args)

    !rm - rf outputs/

    # 学習
    model.train_model(train_df, overwrite_output_dir=True)

    # 評価
    result, model_outputs, wrong_predictions = model.eval_model(eval_df)

    # スコア計算
    import sklearn
    result, model_outputs, wrong_predictions = model.eval_model(
        eval_df, acc=sklearn.metrics.accuracy_score)

    """## 英訳した日本記事でのテスト

    ### データのインポート
    - [ColabにKaggleのデータをダウンロードする](https://qiita.com/fastso/items/43e85fd51d6426d14dd7)
    - [Japanese FakeNews Dataset]()
        - [オープンデータコモンズパブリックドメイン専用およびライセンス（PDDL）v1.0](http://translate.google.com/translate?hl=ja&sl=auto&tl=ja&u=https%3A%2F%2Fopendatacommons.org%2Flicenses%2Fpddl%2F1-0%2F)
            - 受信者は、本作品を商業的に利用したり、技術的な保護手段を用いたり、本データやデータベースを他のデータベースやデータと組み合わせたり、変更や追加を共有したり、秘密にしたりすることができます。
        - 本物はCC BYのウィキニュース
    """

    !pip install kaggle

    from google.colab import files

    uploaded = files.upload()

    for fn in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(
        name=fn, length=len(uploaded[fn])))

    # Then move kaggle.json into the folder where the API expects to find it.
    !mkdir - p ~ / .kaggle / & & mv kaggle.json ~ / .kaggle / & & chmod 600 ~ / .kaggle / kaggle.json

    !kaggle datasets download - d tanreinama / japanese - fakenews - dataset

    !unzip "/content/japanese-fakenews-dataset.zip"

    """### データの前処理"""

    FAKENEWS_DIR = "/content/fakenews.csv"
    # FAKENEWS_DIR = "/content/drive/MyDrive/lab/experiment/transformer-classifier-as-claim-or-evidence/fakenews.csv"

    CONTEXT_IDX = 1
    ISFAKE_IDX = 2
    NEWSTXT_LABEL = 0

    fakenews_data = []
    wikinews_txts = []
    wikinews_sentences = []

    # read
    with open(FAKENEWS_DIR, "r", encoding="utf_8") as f:
        lines = f.readlines()
        print("fakenews.csv lines:")
        print(lines[0])
        print(lines[1])
        print(lines[2])
        print()
        for line in lines[1:]:
            fields = line.rstrip("\n").split(",")
            fakenews_data.append(fields)
            if fields[ISFAKE_IDX] == str(NEWSTXT_LABEL):
                wikinews_txts.append(fields[CONTEXT_IDX])
                wikinews_sentences.append(fields[CONTEXT_IDX].split("。")[:-1])

    # print debug
    print("fakenews_data:")
    print(fakenews_data[0])
    print(fakenews_data[1])
    print()

    print("wikinews_txts:")
    print(wikinews_txts[0])
    print(wikinews_txts[1])
    print()

    print("wikinews_sentences:")
    print(wikinews_sentences[0])
    print(wikinews_sentences[1])
    print()

    len(wikinews_sentences)

    """### DeepL 翻訳
    - [DeepL APIをPythonから利用して日本語の文章を翻訳する](https://deepblue-ts.co.jp/nlp/deepl-api-python/)
    """

    !pip install requests

    import time
    import requests

    DEEPL_API_KEY = 'c3a5e031-5b7b-e534-193e-ac8b826677ac:fx'
    TRANSLATE_NUM = 10
    SLEEP_SEC = 3

    wikinews_txts_en = []

    for txt_idx in range(TRANSLATE_NUM):
        params = {
            "auth_key": DEEPL_API_KEY,
            "text": wikinews_txts[txt_idx],
            "source_lang": 'JA',
            "target_lang": 'EN'
        }
        request = requests.post(
            "https://api-free.deepl.com/v2/translate",
            data=params)
        result = request.json()
        # print(result)
        wikinews_txts_en.append(result["translations"][0]["text"])
        time.sleep(SLEEP_SEC)

    print(wikinews_txts_en[0])

    """### カンマで分割"""

    wikinews_sentences_en = []

    for idx in range(len(wikinews_txts_en)):
        wikinews_sentences_en.append(wikinews_txts_en[idx].split(".")[:-1])

    print("wikinews_sentences_en:")
    print(wikinews_sentences_en[0])
    print(wikinews_sentences_en[1])

    """## 分類器へ代入"""

    predicts = []

    for article_idx in range(len(wikinews_sentences_en)):
        each_articles_preds = []
        for sentence in wikinews_sentences_en[article_idx]:
            # print(sentence)
            # print(model.predict([sentence]))
            pred = model.predict([sentence])
            each_articles_preds.append(pred)
        predicts.append(each_articles_preds)

    print(predicts)

    print(predicts[0])
    for pred in predicts[0]:
        print(pred)

    print(predicts[0][0][0])
    print(predicts[0][0][0][0])

    """### 文章と分類結果の対応"""

    for article_idx in range(len(wikinews_sentences_en)):
        each_articles_preds = []
        print("\n******************************")
        print("article_idx: ", article_idx)
        print("******************************\n")
        for sentence_idx in range(len(wikinews_sentences_en[article_idx])):
            sentence = wikinews_sentences_en[article_idx][sentence_idx]
            if predicts[article_idx][sentence_idx][0][0] == CLAIMS_LABEL:
                print("claim   : ", sentence)
            else:
                print("evidence: ", sentence)

    for article_idx in range(len(wikinews_sentences_en)):
        each_articles_preds = []
        print("\n******************************")
        print("article_idx: ", article_idx)
        print("******************************\n")
        for sentence in wikinews_sentences[article_idx]:
            print(sentence)
        print()
        for sentence_idx in range(len(wikinews_sentences_en[article_idx])):
            sentence = wikinews_sentences_en[article_idx][sentence_idx]
            if predicts[article_idx][sentence_idx][0][0] == CLAIMS_LABEL:
                print("claim   : ", sentence)
            else:
                print("evidence: ", sentence)

    """### ラベルの可視化"""


if __name__ == "__main__":
    main()
