#!/bin/bash
#
# @file      process_02_exe_classifier_as_claim_or_evidence.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     execute process_02_exe_classifier_as_claim_or_evidence with multi files
# @date      2021-12-01 06:05:33
# @version   1.0
# @history   added
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

ARTICLES_DIRS=(
    "./covid-19-news-articles/india-articles_preprocess_03_spilt-sentences_with-stanza.txt"
    "./covid-19-news-articles/japan-articles_preprocess_03_spilt-sentences_with-stanza.txt"
    "./covid-19-news-articles/korea-articles_preprocess_03_spilt-sentences_with-stanza.txt"
    # "./covid-19-news-articles/uk-articles_preprocess_03_spilt-sentences_with-stanza.txt"
)
DEST_DIRS=(
    "./covid-19-news-articles/india-articles_process-02_classified-claim-or-evidence.txt"
    "./covid-19-news-articles/japan-articles_process-02_classified-claim-or-evidence.txt"
    "./covid-19-news-articles/korea-articles_process-02_classified-claim-or-evidence.txt"
    # "./covid-19-news-articles/uk-articles_process-02_classified-claim-or-evidence.txt"
)

for i in {0..2}
do
    python3 process_02_exe_classifier_as_claim_or_evidence.py "${ARTICLES_DIRS[$i]}" "${DEST_DIRS[$i]}"
done

# debug
# for i in {0..2}
# do
#     python3 process_02_exe_classifier_as_claim_or_evidence.py "${ARTICLES_DIRS[$i]}" "${DEST_DIRS[$i]}" -d
# done
