# -*- coding: utf-8 -*-
"""process_03_articles_features_calculator.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     calc articles features with S-BERT
@note      in : e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n
@note      out: article-n;[e-embedding];[c-embedding];[all-embedding]#e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n
@note      python3 process_03_articles_features_calculator.py [in-dir] [dist-dir]
@note      mean pooling
@date      2022-01-09 05:29:45
@version   1.0
@history   add
@see       [SentenceTransformers Documentation](https://www.sbert.net/)
@see       [はじめての自然言語処理 第9回 Sentence BERT による類似文章検索の検証](https://www.ogis-ri.co.jp/otc/hiroba/technical/similar-document-search/part9.html)
@copyright (c) 2021 Kataoka Nagi

"""

from utils.log import Log as log
import time
import datetime
from argparse import ArgumentParser
from re import sub
from sentence_transformers import SentenceTransformer

NUM_DEBUG = 3
MODEL_NAME = 'paraphrase-MiniLM-L6-v2'


def main():

    exe_time_dir = "./covid-19-news-articles/exe-time/exe-time_process_03_articles_features_calculator.txt"

    # debug option
    arg_parser = ArgumentParser(description='execute S-BERT')
    arg_parser.add_argument(
        "articles_dir",
        help="article directory's path",
        type=str)
    arg_parser.add_argument(
        "dest_dir",
        help="destination directory's path",
        type=str)
    arg_parser.add_argument(
        "nation_name",
        help="IN/JP/KR",
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
        exe_time_dir = sub("\\.txt", "_debug.txt", exe_time_dir)

    log.d("*** import articles ***")

    # [[e;feature-x;feature-y;sent-1, c;feature-x;feature-y;sent-2, ...], ...]
    articles_informed_sentences = []

    with open(arg.articles_dir, "r", encoding="utf_8") as f:
        articles_informed_sentences = [
            article.strip().split('#') for article in f.readlines()]
        log.v("articles:")
        log.v(articles_informed_sentences[0])
        log.v(articles_informed_sentences[1])
        log.v(articles_informed_sentences[2])
        log.v()

    if do_debug:
        articles_informed_sentences = articles_informed_sentences[:NUM_DEBUG]

    # separate class info & sentence
    # & cat sentences each articles (all sentences, evidence sentences, claims sentences)

    articles_class_infos = []  # [[e;f-x;f-y, ...], ...]
    articles_sentences = []  # [[sent-1, ...], ...]
    cat_sentences = []  # ["sent-1 sent-2 ...", ...]
    evidence_cat_sentences = []  # ["sent-e1 sent-e2 ...", ...]
    claims_cat_sentences = []  # ["sent-c1 sent-c2 ...", ...]

    # [e;feature-x;feature-y;sent-1, c;feature-x;feature-y;sent-2, ...]
    for informed_sentences in articles_informed_sentences:

        class_infos = []  # [e;-x;-y, ...]
        sentences = []  # [sent-1, ...]
        cat_sentence = ""  # "sent-1 sent-2 ..."
        cat_evidence_sentence = ""  # "sent-e1 sent-e2 ..."
        cat_claims_sentence = ""  # "sent-c1 sent-c2 ..."

        # e;feature-x;feature-y;sent-1
        for informed_sentence in informed_sentences:

            # [e, f-x, f-y, sent-1]
            splits_with_semicolon = informed_sentence.split(';')

            class_info = ';'.join(splits_with_semicolon[:-1])  # e;f-x;f-y
            sentence = splits_with_semicolon[-1]  # sent-1

            cat_sentence += " " + sentence
            if(class_info[0] == "e"):
                cat_evidence_sentence += " " + sentence
            elif (class_info[0] == "c"):
                cat_claims_sentence += " " + sentence
            else:
                log.e("unsuspected classinfo[0]: ", class_info[0])
                log.e("suspected classinfo[0] is 'e' or 'c'")
                exit()

            class_infos.append(class_info)
            sentences.append(sentence)

        articles_class_infos.append(class_infos)
        articles_sentences.append(sentences)

        # delete str if all is space
        evidence_sentence = re.sub(' {2,}', '', evidence_sentence).strip()
        claims_sentence = re.sub(' {2,}', '', claims_sentence).strip()

        cat_sentences.append(cat_sentence.strip())
        evidence_cat_sentences.append(evidence_sentence)
        claims_cat_sentences.append(claims_sentence)

    log.v("articles_class_infos[0]: ", articles_class_infos[0])
    log.v("articles_sentences[0]: ", articles_sentences[0])
    log.v("cat_sentences[0]: ", cat_sentences[0])
    log.v("evidence_cat_sentences[0]: ", evidence_cat_sentences[0])
    log.v("claims_cat_sentences[0]: ", claims_cat_sentences[0])
    log.v()

    log.d("*** substitute articles' sentences for S-BERT ***")

    # set model
    log.d(MODEL_NAME)
    model = SentenceTransformer(MODEL_NAME)

    # time mesurement: start
    start_time = time.time()

    # embed
    all_sentences_embeddings = model.encode(cat_sentences)
    evidence_sentences_embeddings = model.encode(evidence_cat_sentences)
    claims_sentences_embeddings = model.encode(claims_cat_sentences)

    log.v("all_sentences_embeddings[0]", all_sentences_embeddings[0])
    log.v("all_sentences_embeddings.shape", all_sentences_embeddings.shape)
    log.v()

    log.v("evidence_sentences_embeddings[0]", evidence_sentences_embeddings[0])
    log.v("evidence_sentences_embeddings.shape",
          evidence_sentences_embeddings.shape)
    log.v()

    log.v("claims_sentences_embeddings[0]", claims_sentences_embeddings[0])
    log.v("claims_sentences_embeddings.shape",
          claims_sentences_embeddings.shape)
    log.v()

    # print time
    embed_time = time.time() - start_time
    log.d("embed time (sec):", embed_time)

    log.d("*** import articles ***")

    # cat articles_class_infos, each embeddings, and articles_sentences
    # adding article ID (1-1, 1-2, ..., 2-1, 2-2, ...)
    # article-n;e-embedding;c-embedding;all-embedding#e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n
    cats_class_embed_sentence = []
    nation_name = arg.nation_name

    for article_idx, _ in enumerate(articles_sentences):

        article_id = nation_name + str(article_idx)
        a_embed = all_sentences_embeddings[article_idx]
        e_embed = evidence_sentences_embeddings[article_idx]
        c_embed = claims_sentences_embeddings[article_idx]
        informed_sentences = articles_informed_sentences[article_idx]

        cat = [article_id, a_embed, e_embed, c_embed, informed_sentences]
        joined = "#".join(cat).strip().strip('#')

        cats_class_embed_sentence.append(joined + "\n")

    log.v("cats_class_embed_sentence[0]:", cats_class_embed_sentence[0])
    log.v()

    log.d("*** write destination data & embed time ***")

    # write dist
    with open(dest_dir, "w+", encoding="utf_8") as f:
        f.writelines(cats_class_embed_sentence)

    # write time
    with open(exe_time_dir, "a+", encoding="utf_8") as f:
        f.write(str(datetime.datetime))
        f.write(" embed_time(sec): ")
        f.write(str(embed_time))
        f.write("\n")


if __name__ == "__main__":
    main()
