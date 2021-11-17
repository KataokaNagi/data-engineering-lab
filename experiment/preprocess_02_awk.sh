#!/bin/bash
#
# @file      preprocess_02_awk.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     apply sed on each articles
# @date      2021-11-10 04:50:13
# @version   1.1
# @history   make dir name more dinamic
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

# debug [-d] or not
do_debug=false
while getopts d OPT
do
    case $OPT in
        d) do_debug=true
        ;;
        \?) echo "u can use -d option for debug"
        ;;
    esac
done

# const of dir
AWK_DIR="./preprocess_02.awk"
DATA_SUBDIR_1="./covid-19-news-articles/"
NATIONS=(
    "India"
    "Japan"
    "Korea"
    "UK"
)
DATA_SUBDIR_2="-Articles_preprocess-01_extract-column-c.csv"
DIST_SUBDIR="-Articles_preprocess_02_awk.txt"

# make command
# for i in {1..4}
for i in {1..3} # except UK
do
    data_dir="${DATA_SUBDIR_1}${NATIONS["$1"]}${DATA_SUBDIR_2}"
    dist_dir="${DATA_SUBDIR_1}${NATIONS["$1"]}${DIST_SUBDIR}"
    if "${do_debug}"; then
        dist_dir="${dist_dir/.txt/_debug.txt}"
    fi

    mawk -f "${AWK_DIR}" "${data_dir}" > "${dist_dir}"
done

# mawk -f preprocess_02.awk India-Articles_preprocess-01_extract-column-c.csv > India-Articles_preprocess_02_awk.txt
# mawk -f preprocess_02.awk Japan-Articles_preprocess-01_extract-column-c.csv > Japan-Articles_preprocess_02_awk.txt
# mawk -f preprocess_02.awk Korea-Articles_preprocess-01_extract-column-c.csv > Korea-Articles_preprocess_02_awk.txt
# mawk -f preprocess_02.awk UK-Articles_preprocess-01_extract-column-c.csv > UK-Articles_preprocess_02_awk.txt
