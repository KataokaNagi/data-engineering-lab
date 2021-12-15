#!/bin/bash
#
# @file      preprocess_06_rm_duplicate_sentences.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @note      bash preprocess_06_rm_duplicate_sentences.sh [-l]
# @note      python3 preprocess_05_split_sentences_for_debater_dataset.py [txt_dir] [dist_dir]
# @date      2021-12-15 21:06:09
# @version   1.0
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

SRC_DIR="preprocess_06_rm_duplicate_sentences.py"
DATA_DIRS=(
    "./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims_preprocess-04_make-new-line-with-sharp.txt"
    "./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence_preprocess-04_make-new-line-with-sharp.txt"
)
DIST_DIRS=(
    "./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims_preprocess-05_rm-duplicate-sentences.txt"
    "./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence_preprocess-05_rm-duplicate-sentences.txt"
)

date=`date "+%Y%m%d-%H%M%S"`
log_dir="./logs/${SRC_DIR/.py/_${date}.log}"
log_cmd="2>&1 | tee -a ${log_dir}"

# logging option
do_log=false
while getopts ":l" OPT
do
    case $OPT in
        l) do_log=true
        ;;
        \?) echo "you can use -l option for logging"
        ;;
    esac
done

for i in {0..1}
do
    cmd="python3 ${SRC_DIR} ${DATA_DIRS[$i]} ${DIST_DIRS[$i]}"

    if "${do_log}"; then
        cmd="${cmd} ${log_cmd}"
    fi

    echo "${cmd}"
    eval '${cmd}'
done
