# -*- coding: utf-8 -*-
"""process_02_exe_classifier_as_claim_or_evidence.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     execute transformer txt classifier as claim or evidence
@note      [sent-1#sent-2#...\n, ...] -> [e;[ec-score-array];sent-1#c;[ec-score-array];sent-2...\n, ...]
@note      python3 process_02_exe_classifier_as_claim_or_evidence.py ARTICLE_DIR DEST_DIR [-d]
@date      2021-12-01 00:38:55
@version   1.0
@see       transformer_classifier_as_claim_or_evidence.ipynb
@see       [hands-on-ml 16章 Sentiment Analysys](https://github.com/ageron/handson-ml2/blob/master/16_nlp_with_rnns_and_attention.ipynb)
@copyright This file includes the work that is distributed in the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
@copyright This file includes the work that is distributed in the [CC BY-CA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
@copyright (c) 2021 Kataoka Nagi This src is released under the Apache License 2.0 & CC BY-CA 3.0, see LICENSE.

"""

from utils.log import Log as log
import time
from argparse import ArgumentParser
from re import sub
from simpletransformers.classification import ClassificationModel

CLASSIFICATION_MODEL_TYPE = 'roberta'
MODEL_DIR = "outputs/"
NUM_DEBUG = 1


def main():
    """## 英記事で分類

        # データのインポート
        - preprocessed covid-19-news-articles
    """

    # debug option
    arg_parser = ArgumentParser(description='execute simple transformer')
    arg_parser.add_argument(
        "articles_dir",
        help="article directory's path",
        type=str)
    arg_parser.add_argument(
        "dest_dir",
        help="destination directory's path",
        type=str)
    arg_parser.add_argument(
        "-d",
        "--debug",
        help="optional debug",
        action="store_true")
    arg = arg_parser.parse_args()
    do_debug = arg.debug

    # edit DEST_DIRS according to options
    dest_dir = arg.dest_dir
    if do_debug:
        dest_dir = sub("\\.txt", "_debug.txt", dest_dir)

    log.d("*** import articles ***")

    articles_sentences = []  # [articles][sentences]

    with open(arg.articles_dir, "r", encoding="utf_8") as f:
        articles_sentences = [
            article.strip().split('#') for article in f.readlines()]
        log.v("articles_sentences:")
        log.v(articles_sentences[0])
        log.v(articles_sentences[1])
        log.v(articles_sentences[2])
        log.v()

    if do_debug:
        articles_sentences = articles_sentences[:NUM_DEBUG]

    """## 分類器へ代入"""
    log.d("*** substitute articles' sentences for model ***")

    # open model
    model = ClassificationModel(
        CLASSIFICATION_MODEL_TYPE,
        MODEL_DIR
    )

    # predict
    predicts = [[model.predict([sentence]) for sentence in article]
                for article in articles_sentences]

    log.v("predicts:", predicts, '\n')
    log.v("predicts[0]:", predicts[0], '\n')
    log.v("predicts[0][0]:", predicts[0][0], '\n')
    log.v("predicts[0][0][0]:", predicts[0][0][0], '\n')
    log.v("predicts[0][0][0][0]:", predicts[0][0][0][0], '\n')
    log.v("predicts[0][0][1]:", predicts[0][0][1], '\n')
    log.v("predicts[0][0][1][0]:", predicts[0][0][1][0], '\n')
    log.v("type(predicts[0][0][1][0]):", type(predicts[0][0][1][0]), '\n')
    x, y = predicts[0][0][1][0]
    log.v("x, y = predicts[0][0][1][0]")
    log.v("x:", x)
    log.v("y:", y)
    # log.v("predicts[0][0][1][0][0]:", predicts[0][0][0][0][0], '\n') # error
    # log.v("predicts[0][0][1][0][0][0]:", predicts[0][0][1][0][0][0], '\n')
    # log.v("predicts[0][0][1][0][0][0]:", predicts[0][0][1][0][0][1], '\n')

    """### 文章と分類結果の対応"""

    LABEL_IDX = 0
    FEATURE_IDX = 1

    CLAIMS_LABEL = 1
    EVIDENCE_LABEL = 0

    # cat label and sentences
    classified_articles_sentences = []

    for article_idx, article in enumerate(articles_sentences):

        classified_sentences = []

        for sentence_idx, sentence in enumerate(article):
            pred_label = predicts[article_idx][sentence_idx][LABEL_IDX][0]
            feature_x, feature_y = predicts[article_idx][sentence_idx][FEATURE_IDX][0]
            feature_x, feature_y = str(feature_x), str(feature_y)

            if pred_label == CLAIMS_LABEL:
                classified_sentences.append(
                    "c;" + feature_x + ";" + feature_y + ";" + sentence)
            else:
                classified_sentences.append(
                    "e;" + feature_x + ";" + feature_y + ";" + sentence)

        joined = "#".join(
            classified_sentences).strip().strip('#')
        classified_articles_sentences.append(joined + "\n")

    log.v(
        "classified_articles_sentences[0]:",
        classified_articles_sentences[0])

    # write
    with open(dest_dir, "w+", encoding="utf_8") as f:
        f.writelines(classified_articles_sentences)


if __name__ == "__main__":
    main()
