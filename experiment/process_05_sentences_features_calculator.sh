#!/bin/bash
#
# @file      process_05_sentences_features_calculator.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     execute process_05_sentences_features_calculator.py
# @date      2022-01-14 05:00:51
# @version   1.0
# @history   add
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

SRC_DIR="process_05_sentences_features_calculator.py"

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

cmd="python3 ${SRC_DIR}"

if "${do_debug}"; then
    cmd="${cmd} --debug"
fi

if "${do_log}"; then
    cmd="${cmd} ${log_cmd}"
fi

echo "${cmd}"
eval "${cmd}"
