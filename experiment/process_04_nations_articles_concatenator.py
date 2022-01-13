# -*- coding: utf-8 -*-
"""process_04_nations_articles_concatenator.py

@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     cat 3 nations file adding sentence id
@note      in: nation-n;article-n;[e-embedding]#e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n
@note      out: nation-n;article-n;[e-embedding]#nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1#...\n
@note      python3 process_04_nations_articles_concatenator.py
@date      2022-01-09 12:49:03
@version   1.0
@history   add
@copyright (c) 2021 Kataoka Nagi

"""

# from experiment.process_02_exe_classifier_as_claim_or_evidence import NUM_DEBUG
from utils.log import Log as log
import time
import datetime
from argparse import ArgumentParser
import re
import itertools

NATION_NAMES = [
    "IN",
    "JP",
    "KR",
    # "UK"
]

NUM_DEBUG = 20


def main():
    articles_dirs = [
        "./covid-19-news-articles/india-articles_process_03_calced-articles-features.txt",
        "./covid-19-news-articles/japan-articles_process_03_calced-articles-features.txt",
        "./covid-19-news-articles/korea-articles_process_03_calced-articles-features.txt"
        # , "./covid-19-news-articles/uk-articles_preprocess_03_calced-articles-features.txt"
    ]
    dest_dir = "./covid-19-news-articles/process-04_concatenated-nations-articles.txt"
    exe_time_dir = "./covid-19-news-articles/archive/exe-time/exe-time_process_04_nations_articles_concatenator.txt"

    # debug option
    arg_parser = ArgumentParser(
        description='process-04_concatenated-nations-articles')
    arg_parser.add_argument(
        "-d",
        "--debug",
        help="optional debug",
        action="store_true")
    arg = arg_parser.parse_args()
    do_debug = arg.debug

    # edit DEST_DIRS according to options
    if do_debug:
        for i, _ in enumerate(articles_dirs):
            articles_dirs[i] = re.sub("\\.txt", "_debug.txt", articles_dirs[i])
        dest_dir = re.sub("\\.txt", "_debug.txt", dest_dir)
        exe_time_dir = re.sub("\\.txt", "_debug.txt", exe_time_dir)

    # time mesurement: start
    start_time = time.time()

    log.d("*** import articles ***")

    # nation-n;article-n;[e-embedding]#e;feature-x;feature-y;sent-1#c;feature-x;feature-y;sent-2...\n
    nations_articles_informed_sentences = []

    for _, articles_dir in enumerate(articles_dirs):
        with open(articles_dir, "r", encoding="utf_8") as f:

            articles_informed_sentences = []
            for line in f.readlines():
                if not line or line == "":
                    # EOF
                    pass
                elif (line[:2] == "IN") or (line[:2] == "JP") or (line[:2] == "KR"):
                    # IN;0;[ 2.50864863e-01  9.60696563e-02 -3.66732895e-01
                    # -4.08190429e-01
                    articles_informed_sentences.append(line.rstrip())
                elif line[0] == ' ':
                    #  6.89589903e-02 -1.89311713e-01 -8.00815299e-02 -2.10148841e-01
                    articles_informed_sentences[-1] += line.rstrip()
                else:
                    log.e("unexpected line:", line)

            log.v("articles_informed_sentences:")
            log.v(articles_informed_sentences[0])
            log.v(articles_informed_sentences[1])

            articles_informed_sentences = [article.strip().split(
                '#') for article in articles_informed_sentences]
            # [[nation-n;article-n;[e-embedding], e;feature-x;feature-y;sent-1, ...], [...], ...]

            log.v("articles_informed_sentences (split with #):")
            log.v(articles_informed_sentences[0])
            log.v(articles_informed_sentences[1])

            # put on ids to each sentences (nation-n;article-n;sentence-id)
            for i, informed_sentences in enumerate(
                    articles_informed_sentences):

                nation_and_article_ids = informed_sentences[0].split(';')[:2]
                # [nation-n, article-n]
                ids = nation_and_article_ids + [i]
                # [nation-n, article-n, sentence-n]

                informed_sentences_with_id = [
                    ';'.join(
                        ids + i_s) for i_s in informed_sentences]
                # [nation-n;article-n;sentence-id;nation-n;article-n;e-embedding, nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1, ...]

                articles_informed_sentences[i] = informed_sentences[0] + \
                    informed_sentences_with_id[1:]
                # [nation-n;article-n;e-embedding, nation-n;article-n;sentence-id;e;feature-x;feature-y;sent-1, ...]

            nations_articles_informed_sentences.append(
                articles_informed_sentences)
            # [[[nation-n;article-n;e-embedding, e;feature-x;feature-y;sent-1, ...], [...], ...], [...], ...]

            log.v("articles_informed_sentences:")
            log.v(articles_informed_sentences[0])
            log.v(articles_informed_sentences[1])
            log.v(articles_informed_sentences[2])
            log.v()

    if do_debug:
        nations_articles_informed_sentences = [articles_informed_sentences[:NUM_DEBUG]
                                               for articles_informed_sentences in nations_articles_informed_sentences]

    log.d("*** write destination data & embed time ***")

    # write dist
    with open(dest_dir, "w+", encoding="utf_8") as f:
        cat_nations_articles_informed_sentences = [
            (i_s for i_s in a_i_s) for a_i_s in nations_articles_informed_sentences]
        f.writelines(cat_nations_articles_informed_sentences)

    # print time
    exe_time = time.time() - start_time
    log.d("exe time (sec):", exe_time)

    # write time
    with open(exe_time_dir, "a+", encoding="utf_8") as f:
        f.write(str(datetime.datetime))
        f.write(" exe_time(sec): ")
        f.write(str(exe_time))
        f.write("\n")


if __name__ == "__main__":
    main()
