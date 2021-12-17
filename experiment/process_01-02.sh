#!/bin/bash
#
# @file      process_01-02.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @note      exe all bash of process_02
# @date      2021-12-16 09:16:14
# @version   1.0
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

bash process_01_train_classifier_as_claim_or_evidence.sh -l
bash process_02_exe_classifier_as_claim_or_evidence.sh -ld
bash process_02_mv_and_rename_debug_files.sh "$1"
bash process_02_replace_sharp_with_return.sh "$1"
