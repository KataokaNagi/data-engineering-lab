# -*- coding: utf-8 -*-
"""process_01_classifier_as_claim_or_evidence.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@date      2021-11-17 09:56:09
@version   1.0
@see       transformer_classifier_as_claim_or_evidence.ipynb
@see       [hands-on-ml 16章 Sentiment Analysys](https://github.com/ageron/handson-ml2/blob/master/16_nlp_with_rnns_and_attention.ipynb)
@copyright This file includes the work that is distributed in the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
@copyright This file includes the work that is distributed in the [CC BY-CA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
@copyright (c) 2021 Kataoka Nagi This src is released under the Apache License 2.0 & CC BY-CA 3.0, see LICENSE.

"""

from utils.log import Log as log
import requests
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import random
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
import sklearn
import time

CLAIMS_DIR = "./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims.txt"
EVIDENCE_DIR = "./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence.txt"

CLAIMS_LABEL = 1
EVIDENCE_LABEL = 0

SHUFFLE_SEED = 2021
EVAL_RATE = 0.2

NUM_EPOCHS = 10
MODEL_SEED = 2021
CLASSIFICATION_MODEL_TYPE = 'roberta'
CLASSIFICATION_MODEL_NAME = 'roberta-base'

ARTICLES_DIRS = [
    "./covid-19-news-articles/india-articles_preprocess_03_spilt-sentences_with-stanza.txt",
    "./covid-19-news-articles/japan-articles_preprocess_03_spilt-sentences_with-stanza.txt",
    "./covid-19-news-articles/korea-articles_preprocess_03_spilt-sentences_with-stanza.txt"
    # "./covid-19-news-articles/uk-articles_preprocess_03_spilt-sentences_with-stanza.txt"
]

DIST_DIRS = [
    "./covid-19-news-articles/india-articles_preprocess_03_spilt-sentences.txt",
    "./covid-19-news-articles/japan-articles_preprocess_03_spilt-sentences.txt",
    "./covid-19-news-articles/korea-articles_preprocess_03_spilt-sentences.txt"
    # "./covid-19-news-articles/uk-articles_preprocess_03_spilt-sentences.txt"
]


def main():
    CLAIMS_IDX = 2
    EVIDENCE_IDX = 2

    claims_data = []
    evidence_data = []
    claims = []
    evidence = []

    # load
    log.d("*** load data of claim & evidence***")

    with open(CLAIMS_DIR, "r", encoding="utf_8") as f:
        articles_sentences = f.readlines()
        log.v("claims.txt lines:")
        log.v(articles_sentences[0])
        log.v(articles_sentences[1])
        log.v(articles_sentences[2])
        log.v()
        for line in articles_sentences[1:]:
            fields = line.rstrip("\n").split("\t")
            claims_data.append(fields)
            claims.append(fields[CLAIMS_IDX])

    with open(EVIDENCE_DIR, "r", encoding="utf_8") as f:
        articles_sentences = f.readlines()
        log.v("evidence.txt lines:")
        log.v(articles_sentences[0])
        log.v(articles_sentences[1])
        log.v(articles_sentences[2])
        log.v()
        for line in articles_sentences:
            fields = line.rstrip("\n").split("\t")
            evidence_data.append(fields)
            evidence.append(fields[EVIDENCE_IDX].lower())

    # print debug
    log.v("claims_data:")
    log.v(claims_data[0])
    log.v(claims_data[1])
    log.v()

    log.v("evidence_data:")
    log.v(evidence_data[0])
    log.v(evidence_data[1])
    log.v()

    log.v("claims:")
    log.v(claims[0])
    log.v(claims[1])
    log.v()

    log.v("evidence:")
    log.v(evidence[0])
    log.v(evidence[1])

    """### ラベリング"""
    log.d("*** labeling claim & evidence ***")
    log.v("CLAIMS_LABEL:", CLAIMS_LABEL)
    log.v("EVIDENCE_LABEL:", EVIDENCE_LABEL)

    if (CLAIMS_LABEL):
        claims_labels = np.ones(len(claims)).tolist()
    else:
        claims_labels = np.zeros(len(claims)).tolist()

    if (EVIDENCE_LABEL):
        evidence_labels = np.ones(len(evidence)).tolist()
    else:
        evidence_labels = np.zeros(len(evidence)).tolist()

    log.v(claims_labels[0])
    log.v(evidence_labels[0])

    claims_dataset = []
    evidence_dataset = []

    for idx in range(len(claims)):
        claims_dataset.append([claims[idx], claims_labels[idx]])

    for idx in range(len(evidence)):
        evidence_dataset.append([evidence[idx], evidence_labels[idx]])

    log.v(claims_dataset[0])
    log.v(evidence_dataset[0])

    """### 結合"""
    log.d("*** cat 2 datasets ***")

    dataset = claims_dataset + evidence_dataset
    log.v(dataset[0])
    log.v(dataset[-1])

    """### シャッフル"""
    log.d("*** shuffle dataset order ***")

    log.d("SHUFFLE_SEED:", SHUFFLE_SEED)
    random.seed(SHUFFLE_SEED)

    random.shuffle(dataset)
    log.v(dataset[0])
    log.v(dataset[-1])

    """### 訓練、評価~~、テストデータ~~に分割"""
    log.d("*** split dataset to eval & train ***")
    log.d("EVAL_RATE:", EVAL_RATE)

    dataset_num = len(dataset)
    eval_num = int(dataset_num * EVAL_RATE)
    train_num = dataset_num - eval_num

    eval_dataset = dataset[:eval_num]
    train_dataset = dataset[eval_num:]

    log.v("dataset_num: ", dataset_num)
    log.v("eval_num: ", eval_num)
    log.v("train_num: ", train_num)

    """## 分類器の作成
    - [Simple Transformers 入門 (1) - テキスト分類 ](https://note.com/npaka/n/nfe2436ea5301#9VV1a)
    - [Simple Transformers 入門 (10) - ハイパーパラメータの最適化 ](https://note.com/npaka/n/n298f269c2275)

    # Simple Transformerのインストール
    """

    # !pip install transformers
    # !pip install simpletransformers

    """### モデルの評価まで"""
    log.d("*** train & evaluate model ***")

    # ログの設定
    logging.basicConfig(level=logging.INFO)
    transformers_logger = logging.getLogger("transformers")
    transformers_logger.setLevel(logging.WARNING)

    # 学習データの作成
    train_df = pd.DataFrame(train_dataset)

    # 評価データの作成
    eval_df = pd.DataFrame(eval_dataset)

    # モデルの作成

    log.d("NUM_EPOCHS:", NUM_EPOCHS)
    log.d("MODEL_SEED:", MODEL_SEED)
    model_args = ClassificationArgs()
    model_args.num_train_epochs = NUM_EPOCHS
    # model_args.reprocess_input_data = True
    model_args.manual_seed = MODEL_SEED

    log.d("CLASSIFICATION_MODEL_TYPE:", CLASSIFICATION_MODEL_TYPE)
    log.d("CLASSIFICATION_MODEL_NAME:", CLASSIFICATION_MODEL_NAME)
    model = ClassificationModel(
        CLASSIFICATION_MODEL_TYPE,
        CLASSIFICATION_MODEL_NAME,
        args=model_args)

    # !rm - rf outputs/

    # 学習
    model.train_model(train_df, overwrite_output_dir=True)

    # 評価
    result, model_outputs, wrong_predictions = model.eval_model(eval_df)

    # スコア計算
    result, model_outputs, wrong_predictions = model.eval_model(
        eval_df, acc=sklearn.metrics.accuracy_score)

    """## 英記事でのテスト

        # データのインポート
        - preprocessed covid-19-news-articles
    """

    """### データの前処理"""
    log.d("*** import articles ***")

    nations_articles_sentences = [
        len(ARTICLES_DIRS)]  # [nation][articles][sentences]

    # read
    for nation_idx, articles_dir in enumerate(ARTICLES_DIRS):
        with open(articles_dir, "r", encoding="utf_8") as f:
            articles_sentences = [
                article.split('#') for article in f.readlines()]
            nations_articles_sentences[nation_idx] = articles_sentences
            log.v("articles_sentences:")
            log.v(articles_sentences[0])
            log.v(articles_sentences[1])
            log.v(articles_sentences[2])
            log.v()

    """## 分類器へ代入"""
    log.d("*** substitute nations' articles' sentences for model ***")

    predicts = []

    for nation_idx, articles_sentences in enumerate(
            nations_articles_sentences):
        for article_idx, sentences in enumerate(
                articles_sentences):
            each_articles_preds = []
            for sentence in articles_sentences[article_idx]:
                # log.v(sentence)
                # log.v(model.predict([sentence]))
                pred = model.predict([sentence])
                each_articles_preds.append(pred)
            predicts.append(each_articles_preds)

    log.v(predicts)

    log.v(predicts[0])
    for pred in predicts[0]:
        log.v(pred)

    log.v(predicts[0][0][0])
    log.v(predicts[0][0][0][0])

    """### 文章と分類結果の対応"""

    for article_idx in range(len(wikinews_sentences_en)):
        each_articles_preds = []
        log.v("\n******************************")
        log.v("article_idx: ", article_idx)
        log.v("******************************\n")
        for sentence_idx in range(len(wikinews_sentences_en[article_idx])):
            sentence = wikinews_sentences_en[article_idx][sentence_idx]
            if predicts[article_idx][sentence_idx][0][0] == CLAIMS_LABEL:
                log.v("claim   : ", sentence)
            else:
                log.v("evidence: ", sentence)

    for article_idx in range(len(wikinews_sentences_en)):
        each_articles_preds = []
        log.v("\n******************************")
        log.v("article_idx: ", article_idx)
        log.v("******************************\n")
        for sentence in nations_articles_sentences[article_idx]:
            log.v(sentence)
        log.v()
        for sentence_idx in range(len(wikinews_sentences_en[article_idx])):
            sentence = wikinews_sentences_en[article_idx][sentence_idx]
            if predicts[article_idx][sentence_idx][0][0] == CLAIMS_LABEL:
                log.v("claim   : ", sentence)
            else:
                log.v("evidence: ", sentence)

    log.w("remove outputs/ if you needed")

    """### ラベルの可視化"""


"""## データのインポート・前処理

# データセット概要
- [IBM Debater® - Claims and Evidence (EMNLP 2015)](https://www.research.ibm.com/haifa/dept/vst/debating_data.shtml#Download)
    - 作品がCC-BY-SAでリリースされていることを示すライセンス表示
        - 権利者の名前を入れる
        - 加工しても同じライセンスで他人にもシェア
        - 商用利用OK
    - a)ライセンスのテキストへのハイパーリンクまたはURL
    - またはb)ライセンスのコピーのいずれかを含める
    - 文末のカンマやクエスチョンマークは除去済み

# インポートとテキスト処理
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

if __name__ == "__main__":
    main()
