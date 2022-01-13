#!/bin/bash
#
# @file      process_04_nations_articles_concatenator.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     execute process_04_nations_articles_concatenator with multi files
# @date      2022-01-09 06:03:51
# @version   1.0
# @history   add
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

SRC_DIR="process_04_nations_articles_concatenator.py"

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
