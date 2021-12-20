# -*- coding: utf-8 -*-
"""process_01_train_classifier_as_claim_or_evidence.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     train transformer txt classifier as claim or evidence
@note      [sent-1#sent-2#...\n, ...] -> [e;[ec-score-array];sent-1#c;[ec-score-array];sent-2...\n, ...]
@note      python3 process_01_train_classifier_as_claim_or_evidence.py
@date      2021-12-04 06:20:06
@version   1.1
@history   apply for preprocess data
@see       transformer_classifier_as_claim_or_evidence.ipynb
@see       [hands-on-ml 16章 Sentiment Analysys](https://github.com/ageron/handson-ml2/blob/master/16_nlp_with_rnns_and_attention.ipynb)
@copyright This file includes the work that is distributed in the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
@copyright This file includes the work that is distributed in the [CC BY-CA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
@copyright (c) 2021 Kataoka Nagi This src is released under the Apache License 2.0 & CC BY-CA 3.0, see LICENSE.

"""

from utils.log import Log as log
import numpy as np
import random
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
import sklearn
import time

CLAIMS_DIR = "./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims_preprocess-05_rm-duplicate-sentences.txt"
EVIDENCE_DIR = "./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence_preprocess-05_rm-duplicate-sentences.txt"

EVIDENCE_LABEL = 0
CLAIMS_LABEL = 1

SHUFFLE_SEED = 2021
EVAL_RATE = 0.2

NUM_EPOCHS = 100
MODEL_SEED = 2021
CLASSIFICATION_MODEL_TYPE = 'roberta'
CLASSIFICATION_MODEL_NAME = 'roberta-base'
BEST_MODEL_DIR = 'outputs/best_model'
USE_EARLY_STOPPING = True


def main():
    claims = []
    evidences = []

    # load
    log.d("*** load data of claim & evidence***")

    # import claim data
    with open(CLAIMS_DIR, "r", encoding="utf_8") as f:
        sentences = f.readlines()
        log.v("claims.txt lines:")
        log.v(sentences[0])
        log.v(sentences[1])
        log.v(sentences[2])
        log.v()
        for sentence in sentences:
            claims.append(sentence.rstrip("\n"))
        if claims[-1] is None or len(claims[-1]) == 0:
            claims.pop(-1)

    # import evidence data
    with open(EVIDENCE_DIR, "r", encoding="utf_8") as f:
        sentences = f.readlines()
        log.v("evidence.txt lines:")
        log.v(sentences[0])
        log.v(sentences[1])
        log.v(sentences[2])
        log.v()
        for sentence in sentences:
            evidences.append(sentence.rstrip("\n"))
        if evidences[-1] is None or len(evidences[-1]) == 0:
            evidences.pop(-1)

    # print debug
    log.v("claims:")
    log.v(claims[0])
    log.v(claims[1])
    log.v()

    log.v("evidence:")
    log.v(evidences[0])
    log.v(evidences[1])

    """### ラベリング"""
    log.d("*** labeling claim & evidence ***")
    log.v("CLAIMS_LABEL:", CLAIMS_LABEL)
    log.v("EVIDENCE_LABEL:", EVIDENCE_LABEL)

    if (CLAIMS_LABEL):
        claims_labels = np.ones(len(claims)).tolist()
    else:
        claims_labels = np.zeros(len(claims)).tolist()

    if (EVIDENCE_LABEL):
        evidence_labels = np.ones(len(evidences)).tolist()
    else:
        evidence_labels = np.zeros(len(evidences)).tolist()

    log.v(claims_labels[0])
    log.v(evidence_labels[0])

    claims_dataset = []
    evidence_dataset = []

    for idx in range(len(claims)):
        claims_dataset.append([claims[idx], claims_labels[idx]])

    for idx in range(len(evidences)):
        evidence_dataset.append([evidences[idx], evidence_labels[idx]])

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

    # 不均衡なデータの調整用
    cnt_train_label_0 = 0
    cnt_train_label_1 = 0
    LABEL_IDX = 1

    for data in train_dataset:
        label = data[LABEL_IDX]
        if label == 0:
            cnt_train_label_0 += 1
        elif label == 1:
            cnt_train_label_1 += 1
        else:
            log.e("unsuspected label")
            exit()

    claims_per_evidence = float(cnt_train_label_1) / float(cnt_train_label_0)

    log.v("cnt_train_label_0:", cnt_train_label_0)
    log.v("cnt_train_label_1:", cnt_train_label_1)
    log.v("claims_per_evidence:", claims_per_evidence)

    # モデルの作成
    log.d("NUM_EPOCHS:", NUM_EPOCHS)
    log.d("MODEL_SEED:", MODEL_SEED)
    model_args = ClassificationArgs()
    model_args.num_train_epochs = NUM_EPOCHS
    # model_args.reprocess_input_data = True
    model_args.manual_seed = MODEL_SEED
    model_args.best_model_dir = BEST_MODEL_DIR
    model_args.use_early_stopping = USE_EARLY_STOPPING

    log.d("CLASSIFICATION_MODEL_TYPE:", CLASSIFICATION_MODEL_TYPE)
    log.d("CLASSIFICATION_MODEL_NAME:", CLASSIFICATION_MODEL_NAME)
    log.d("USE_EARLY_STOPPING:", USE_EARLY_STOPPING)

    model = ClassificationModel(
        model_type=CLASSIFICATION_MODEL_TYPE,
        model_name=CLASSIFICATION_MODEL_NAME,
        use_cuda=True,
        args=model_args,
        weight=[1, claims_per_evidence],
        # weight=[claims_per_evidence, 1],
    )

    # !rm - rf outputs/

    # 学習
    start_time = time.time()
    model.train_model(train_df, overwrite_output_dir=True)
    log.d("train time (sec):", time.time() - start_time)

    # 評価
    result, model_outputs, wrong_predictions = model.eval_model(eval_df)

    # スコア計算
    result, model_outputs, wrong_predictions = model.eval_model(
        eval_df, acc=sklearn.metrics.accuracy_score)


if __name__ == "__main__":
    main()
