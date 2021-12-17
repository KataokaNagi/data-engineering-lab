#!/bin/bash
#
# @file      process_02_mv_and_rename_debug_files
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @note      change const
# @date      2021-12-11 05:18:46
# @version   1.0
# @history   add
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

NUM_EPOCHS="$1"

# mv covid-19-news-articles/*process-02* covid-19-news-articles/archive/process-02_classified-claim-or-evidence_preprocessed-by-04_debug/
# eval rename '"s/g.txt/g_${NUM_EPOCHS}-epochs.txt/"' covid-19-news-articles/archive/process-02_classified-claim-or-evidence_debug/*.txt

mv covid-19-news-articles/*process-02* covid-19-news-articles/archive/process-02_classified-claim-or-evidence_preprocessed-by-06_debug/
eval rename '"s/g.txt/g_${NUM_EPOCHS}-epochs.txt/"' covid-19-news-articles/archive/process-02_classified-claim-or-evidence_preprocessed-by-06_debug/*.txt
