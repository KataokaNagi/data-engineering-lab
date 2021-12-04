#!/bin/bash
#
# @file      preprocess_03_split_sentences.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @note      bash preprocess_03_split_sentences.sh [-d] [-l] [-s|-]
# @note      python3 preprocess_03_split_sentences.py [--debug] [--stanza|--spacy] []
# @date      2021-12-05 04:46:49
# @version   1.0
# @history   add (no tested)
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

SRC_DIR="preprocess_03_split_sentences.sh.py"

date=`date "+%Y%m%d-%H%M%S"`
log_dir="./logs/${SRC_DIR/.py/_${date}.log}"
log_cmd="2>&1 | tee -a ${log_dir}"

# debug [-d] or not
do_debug=false
do_log=false
use_stanza=false
use_spacy=false
while getopts ":dl-:" OPT
do
    case $OPT in
        d) do_debug=true
        ;;
        l) do_log=true
        ;;
        -)
            case "${OPTARG}" in
                stanza)
                    use_stanza=true
                    ;;
                spacy)
                    use_spacy=true
                    ;;
            esac
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

if "${use_stanza}"; then
    cmd="${cmd} --stanza"
fi

if "${use_spacy}"; then
    cmd="${cmd} --spacy"
fi

eval "${cmd}"
