#!/bin/bash
#
# @file      preprocess_04_awk-for-debater-dataset.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     apply awk on each dataset
# @date      2021-12-03 04:27:12
# @version   1.0
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

# const of dir
AWK_DIR="./preprocess_04_for-debater-dataset.awk"
DATA_DIRS=(
    "./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims_preprocess-01_extract-column-c.txt"
    "./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence_preprocess-01_extract-column-c.txt"
)
DEST_DIRS=(
    "./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims_preprocess-02_awk.txt"
    "./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence_preprocess-02_awk.txt"
)

# debug [-d] or not
do_debug=false
while getopts d OPT
do
    case $OPT in
        d) do_debug=true
        ;;
        \?) echo "you can use -d option for debug"
        ;;
    esac
done

for i in {0..1}
do
    # make command
    dest_dir="${DEST_DIRS[$i]}"
    if "${do_debug}"; then
        dest_dir="${dest_dir/.txt/_debug.txt}"
    fi

    # exe command
    mawk -f "${AWK_DIR}" "${DATA_DIRS[$i]}" > "${dest_dir}"
done

# mawk -f preprocess_04_for-debater-dataset.awk ./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims_preprocess-01_extract-column-c.txt > ./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims_preprocess-02_awk.txt
# mawk -f preprocess_04_for-debater-dataset.awk ./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence_preprocess-01_extract-column-c.txt > ./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence_preprocess-02_awk.txt
