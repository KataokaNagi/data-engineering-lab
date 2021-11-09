#!/bin/bash
#
# @file      preprocess_02.awk
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     apply sed on each articles
# @date      2021-11-10 04:50:13
# @version   1.0
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 
gawk -f preprocess_02.awk India-Articles_preprocess-01_extract-column-c.csv > India-Articles_preprocess_02_awk.txt
gawk -f preprocess_02.awk Japan-Articles_preprocess-01_extract-column-c.csv > Japan-Articles_preprocess_02_awk.txt
gawk -f preprocess_02.awk Korea-Articles_preprocess-01_extract-column-c.csv > Korea-Articles_preprocess_02_awk.txt
# gawk -f preprocess_02.awk UK-Articles_preprocess-01_extract-column-c.csv > UK-Articles_preprocess_02_awk.txt