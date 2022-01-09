#!/bin/bash
#
# @file      process_03_articles_features_calculator.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     execute process_03_articles_features_calculator with multi files
# @date      2022-01-09 06:03:51
# @version   1.0
# @history   add
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

SRC_DIR="process_03_articles_features_calculator.py"
NATION_NAMES=(
    "IN"
    "JP"
    "KR"
)
# ARTICLES_DIRS=(
#     "./covid-19-news-articles/india-articles_process-02_classified-claim-or-evidence.txt"
#     "./covid-19-news-articles/japan-articles_process-02_classified-claim-or-evidence.txt"
#     "./covid-19-news-articles/korea-articles_process-02_classified-claim-or-evidence.txt"
#     # "./covid-19-news-articles/uk-articles_process-02_classified-claim-or-evidence.txt"
# )
# DEST_DIRS=(
#     "./covid-19-news-articles/india-articles_preprocess_03_calced-articles-features.txt"
#     "./covid-19-news-articles/japan-articles_preprocess_03_calced-articles-features.txt"
#     "./covid-19-news-articles/korea-articles_preprocess_03_calced-articles-features.txt"
#     # "./covid-19-news-articles/uk-articles_preprocess_03_calced-articles-features.txt"
# )
ARTICLES_DIRS=(
    "./covid-19-news-articles/india-articles_process-02_classified-claim-or-evidence_debug.txt"
    "./covid-19-news-articles/japan-articles_process-02_classified-claim-or-evidence_debug.txt"
    "./covid-19-news-articles/korea-articles_process-02_classified-claim-or-evidence_debug.txt"
    # "./covid-19-news-articles/uk-articles_process-02_classified-claim-or-evidence_debug.txt"
)
DEST_DIRS=(
    "./covid-19-news-articles/india-articles_preprocess_03_calced-articles-features_debug.txt"
    "./covid-19-news-articles/japan-articles_preprocess_03_calced-articles-features_debug.txt"
    "./covid-19-news-articles/korea-articles_preprocess_03_calced-articles-features_debug.txt"
    # "./covid-19-news-articles/uk-articles_preprocess_03_calced-articles-features_debug.txt"
)

date=`date "+%Y%m%d-%H%M%S"`
log_dir="./logs/${SRC_DIR/.py/_${date}.log}"
log_cmd="2>&1 | tee -a ${log_dir}"

# debug [-d] or not
do_debug=false
do_log=false
while getopts ":dl" OPT
do
    case $OPT in
        d) do_debug=true
        ;;
        l) do_log=true
        ;;
        \?) echo "u can use -d option for debug"
        ;;
    esac
done

for i in {0..2}
do
    cmd="python3 ${SRC_DIR} ${NATION_NAMES[$i]} ${ARTICLES_DIRS[$i]} ${DEST_DIRS[$i]}"

    if "${do_debug}"; then
        cmd="${cmd} --debug"
    fi

    if "${do_log}"; then
        cmd="${cmd} ${log_cmd}"
    fi

    echo "${cmd}"
    eval "${cmd}"
done
