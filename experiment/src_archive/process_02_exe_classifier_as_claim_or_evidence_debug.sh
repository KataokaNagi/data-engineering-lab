#!/bin/bash
#
# @file      process_02_exe_classifier_as_claim_or_evidence.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     execute process_02_exe_classifier_as_claim_or_evidence with multi files
# @date      2021-12-05 04:38:15
# @version   1.1
# @history   add log option
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

SRC_DIR="process_02_exe_classifier_as_claim_or_evidence_debug.py"
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
    cmd="python3 ${SRC_DIR} ${ARTICLES_DIRS[$i]} ${DEST_DIRS[$i]}"

    if "${do_debug}"; then
        cmd="${cmd} --debug"
    fi

    if "${do_log}"; then
        cmd="${cmd} ${log_cmd}"
    fi

    eval "${cmd}"
done
