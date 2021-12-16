#!/bin/bash
#
# @file      process_02_replace_sharp_with_return
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @note      change const
# @date      2021-12-16 09:16:14
# @version   1.0
# @history   add
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

FILE_DIRS=(
    "./covid-19-news-articles/archive/process-02_classified-claim-or-evidence_preprocessed-by-06_debug/india-articles_process-02_classified-claim-or-evidence_debug_3-epochs.txt"
    "./covid-19-news-articles/archive/process-02_classified-claim-or-evidence_preprocessed-by-06_debug/japan-articles_process-02_classified-claim-or-evidence_debug_3-epochs.txt"
    "./covid-19-news-articles/archive/process-02_classified-claim-or-evidence_preprocessed-by-06_debug/korea-articles_process-02_classified-claim-or-evidence_debug_3-epochs.txt"
)

for i in {0..2}
do
    echo "" >> "${FILE_DIRS[$i]}"
    cat "${FILE_DIRS[$i]}" | sed -e 's/#/\n/g' >> "${FILE_DIRS[$i]}"
done
