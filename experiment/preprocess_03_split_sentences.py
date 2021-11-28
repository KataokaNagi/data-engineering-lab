"""
@file      preprocess_03_split_sentences.py
@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     split sentences with '#' by periods other than appreviate periods
@date      2021-11-17 09:56:09
@version   1.0
@see       https://stackoverflow.com/questions/66238613/sentence-segmentation-with-trailing-whitespaces-in-stanza-stanford-corenlp
@copyright This file includes the work that is distributed in the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
@copyright (c) 2021 Kataoka Nagi This src is released under the Apache License 2.0, see LICENSE.
"""


def main():
    import sys
    import argparse
    import re
    import time
    import stanza
    stanza.download('en')

    # option
    use_spacy = True
    use_stanza = not use_spacy
    do_debug = False
    num_debug = 10

    # consts of dir
    DATASET_DIRS = [
        "./covid-19-news-articles/india-articles_preprocess_02_awk.txt",
        "./covid-19-news-articles/japan-articles_preprocess_02_awk.txt",
        "./covid-19-news-articles/korea-articles_preprocess_02_awk.txt"
        # "./covid-19-news-articles/uk-articles_preprocess_02_awk.txt"
    ]
    dist_dirs = [
        "./covid-19-news-articles/india-articles_preprocess_03_spilt-sentences.txt",
        "./covid-19-news-articles/japan-articles_preprocess_03_spilt-sentences.txt",
        "./covid-19-news-articles/korea-articles_preprocess_03_spilt-sentences.txt"
        # "./covid-19-news-articles/uk-articles_preprocess_03_spilt-sentences.txt"
    ]

    # debug option
    arg_parser = argparse.ArgumentParser(description='-d: debug')
    arg_parser.add_argument(
        "-d",
        "--debug",
        help="optional debug",
        action="store_true")
    arg_parser.add_argument(
        "--spacy",
        help="optional debug",
        action="store_true")
    arg_parser.add_argument(
        "--stanza",
        help="optional debug",
        action="store_true")
    arg = arg_parser.parse_args()
    do_debug = arg.debug
    if arg.stanza:
        use_spacy = False
        use_stanza = True
    if arg.spacy:
        use_spacy = True
        use_stanza = False

    # edit DIST_DIRS according to options
    for i, _ in enumerate(dist_dirs):
        if use_spacy:
            dist_dirs[i] = re.sub("\\.txt", "_with-spacy.txt", dist_dirs[i])
        if use_stanza:
            dist_dirs[i] = re.sub("\\.txt", "_with-stanza.txt", dist_dirs[i])

        if do_debug:
            dist_dirs[i] = re.sub("\\.txt", "_debug.txt", dist_dirs[i])

    # prepare for stanza or spacy
    processors = \
        'tokenize' if use_stanza \
        else \
        {'tokenize': 'spacy'} if use_spacy \
        else \
        print("unsuspected processors", file=sys.stderr)
    nlp = stanza.Pipeline(lang="en", processors=processors)

    # time mesurement: start
    start_time = time.time()

    # open dataset
    for dir_idx, _ in enumerate(DATASET_DIRS):
        with open(DATASET_DIRS[dir_idx], 'r') as fi, open(dist_dirs[dir_idx], 'w+') as fw:
            cnt_line = 1
            for line in fi:
                # split sentences
                doc = nlp(line)
                spilit_sentences = [
                    sentence.text for sentence in doc.sentences]
                spilit_sentences = "#".join(
                    spilit_sentences).strip().strip('#')
                spilit_sentences += '\n'

                # write
                fw.write(spilit_sentences)

                # debug
                if do_debug:
                    if cnt_line > num_debug:
                        break
                    print("cnt_line:", cnt_line, spilit_sentences)
                    cnt_line += 1

    # print time
    print(time.time() - start_time)


if __name__ == "__main__":
    main()
