#!/bin/bash
#
# @file      process_01_train_classifier_as_claim_or_evidence
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     execute process_01_train_classifier_as_claim_or_evidence
# @date      2021-12-05 05:07:12
# @version   1.0
# @history   add
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

SRC_DIR="process_01_train_classifier_as_claim_or_evidence.py"

# do logging [-l] or not
do_log=false
while getopts ":l-" OPT
do
    case $OPT in
        l) do_log=true
        ;;
        -)
            case "${OPTARG}" in
                log)
                    do_log=true
                    ;;
            esac
            ;;
        \?) echo "you can use -l option for logging"
        ;;
    esac
done

# make log_cmd
date=`date "+%Y%m%d-%H%M%S"`
log_dir="./logs/${SRC_DIR/.py/_${date}.log}"
log_cmd="2>&1 | tee ${log_dir}"

# make & exe cmd
cmd="python3 ${SRC_DIR}"
if "${do_log}"; then
    cmd="${cmd} ${log_cmd}"
fi
echo "${cmd}"
eval "${cmd}"
