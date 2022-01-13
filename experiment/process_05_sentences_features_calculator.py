# -*- coding: utf-8 -*-
"""process_05_sentences_features_calculator.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     calc claims sentences features with S-BERT
@note      in : nation-n;article-n;[e-embedding]#nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1#...\n
@note      out: nation-id;article-id;[e-embedding]#nation-id;article-id;sentence-id;e;feature-x;feature-y;sent-1#nation-id;article-id;sentence-id;c;feature-x;feature-y;[feature-array];sent-2...\n
@note      python3 process_05_sentences_features_calculator.py
@date      2022-01-14 03:15:49
@version   1.0
@history   add
@see       [SentenceTransformers Documentation](https://www.sbert.net/)
@copyright (c) 2021 Kataoka Nagi

"""

from utils.log import Log as log
import time
import datetime
from argparse import ArgumentParser
import re
from sentence_transformers import SentenceTransformer

NUM_DEBUG = 20
MODEL_NAME = 'paraphrase-MiniLM-L6-v2'


def main():
    articles_dir = "./covid-19-news-articles/process-04_concatenated-nations-articles.txt"
    dest_dir = "./covid-19-news-articles/process-05_calced-sentences-features.txt"
    exe_time_dir = "./covid-19-news-articles/archive/exe-time/exe-time_process_05_sentences_features_calculator.txt"

    # debug option
    arg_parser = ArgumentParser(description='execute S-BERT')
    arg_parser.add_argument(
        "-d",
        "--debug",
        help="optional debug",
        action="store_true")
    arg = arg_parser.parse_args()
    do_debug = arg.debug

    # edit DEST_DIRS according to options
    if do_debug:
        articles_dir = re.sub("\\.txt", "_debug.txt", articles_dir)
        dest_dir = re.sub("\\.txt", "_debug.txt", dest_dir)
        exe_time_dir = re.sub("\\.txt", "_debug.txt", exe_time_dir)

    log.d("*** import articles ***")

    # nation-n;article-n;[e-embedding]
    # nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1#...\n
    article_info_or_sentences = []

    with open(articles_dir, "r", encoding="utf_8") as f:
        article_info_or_sentences = f.readlines()
        log.v("articles:")
        log.v(article_info_or_sentences[0])
        log.v(article_info_or_sentences[1])
        log.v(article_info_or_sentences[2])
        log.v()

    # extract claim sentences
    claim_sentences = []  # [sent-c1, sent-c2, ...]
    CLAIM__SENTENCE_IDX = 6
    CLASS_IDX = 3

    # nation-n;article-n;[e-embedding]
    # nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1#...\n
    for article_info_or_sentence in article_info_or_sentences:

        splits_with_semicolon = article_info_or_sentence.split(';')
        len_splits_with_semicolon = len(splits_with_semicolon)

        # article info
        if len_splits_with_semicolon == 3:
            pass
        # sentence info
        elif len_splits_with_semicolon == 7:
            ec_class = splits_with_semicolon[CLASS_IDX]
            if ec_class == 'c':
                claim_sentence = splits_with_semicolon[CLAIM__SENTENCE_IDX]
                claim_sentences.append(claim_sentence)
            elif ec_class == 'e':
                pass
            else:
                log.e("unsuspected ec_class: ", ec_class)
                exit()
        # error
        else:
            log.e(
                "unsuspected len_splits_with_semicolon: ",
                len_splits_with_semicolon)
            exit()

    log.v("claim_sentences[0]: ", claim_sentences[0])
    log.v()

    log.d("*** substitute articles' sentences for S-BERT ***")

    # set model
    log.d("MODEL_NAME:", MODEL_NAME)
    model = SentenceTransformer(MODEL_NAME)

    # time mesurement: start
    start_time = time.time()

    # embed
    claim_sentences_embeddings = model.encode(claim_sentences)
    log.v("claim_sentences_embeddings[0]", claim_sentences_embeddings[0])
    log.v("claim_sentences_embeddings.shape",
          claim_sentences_embeddings.shape)
    log.v()

    # print time
    embed_time = time.time() - start_time
    log.d("embed time (sec):", embed_time)

    log.d("*** import articles ***")

    # cat claim_sentences_embeddings & article_info_or_sentences
    # out:
    # nation-id;article-id;[e-embedding]#nation-id;article-id;sentence-id;e;feature-x;feature-y;sent-1#nation-id;article-id;sentence-id;c;feature-x;feature-y;[feature-array];sent-2...\n
    cats_embed_and_origin_line = []
    embed_iter = 0

    # nation-n;article-n;[e-embedding]
    # nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1#...\n
    for line_idx, article_info_or_sentence in enumerate(
            article_info_or_sentences):

        splits_with_semicolon = article_info_or_sentence.split(';')
        len_splits_with_semicolon = len(splits_with_semicolon)

        # article info
        if len_splits_with_semicolon == 3:
            pass
        # sentence info
        elif len_splits_with_semicolon == 7:
            ec_class = splits_with_semicolon[CLASS_IDX]
            if ec_class == 'c':
                embed_list = [str(e)
                              for e in claim_sentences_embeddings[embed_iter]]
                embed_str = ' '.join(embed_list)
                embed_iter += 1

                splits_with_semicolon.insert(CLAIM__SENTENCE_IDX, embed_str)

                article_info_or_sentences[line_idx] = ";".join(
                    splits_with_semicolon)

                if do_debug:
                    log.v("embed_list:", embed_list)
                    log.v("embed_str:", embed_str)
                    log.v("splits_with_semicolon:", splits_with_semicolon)
                    log.v(
                        "article_info_or_sentences[line_idx]:",
                        article_info_or_sentences[line_idx])

            elif ec_class == 'e':
                pass
            else:
                log.e("unsuspected ec_class: ", ec_class)
                exit()
        # error
        else:
            log.e(
                "unsuspected len_splits_with_semicolon: ",
                len_splits_with_semicolon)
            exit()

    log.v("article_info_or_sentences[0]: ", article_info_or_sentences[0])
    log.v("article_info_or_sentences[1]: ", article_info_or_sentences[1])
    log.v("article_info_or_sentences[28]: ", article_info_or_sentences[28])
    log.v()

    # write dist
    with open(dest_dir, "w+", encoding="utf_8") as f:
        f.writelines(article_info_or_sentences)

    # write time
    with open(exe_time_dir, "a+", encoding="utf_8") as f:
        f.write(str(datetime.datetime))
        f.write(" embed_time(sec): ")
        f.write(str(embed_time))
        f.write("\n")


if __name__ == "__main__":
    main()
