#!/bin/bash
#
# @file      printe_tools.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     print pc spec, programming lang versions, & module versions
# @note      print into tools.log
# @date      2022-01-25 13:53:46
# @version   1.0
# @history   add
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

DIST_DIR="tools.log"

date=`date "+%Y%m%d-%H%M%S"`
log_dir="./logs/${DIST_DIR/.log/_${date}.log}"
log_cmd="2>&1 | tee -a ${log_dir}"

CMDS=(
    # cpu
    "cat /proc/cpuinfo"
    # gpu
    "lspci | grep VGA"
    "nvidia-smi"
    # mem
    "cat /proc/meminfo"
    # "sudo dmidecode --type memory"
    # os
    "uname -a"
    "cat /etc/lsb-release"
    # cuda
    "nvcc -V"
    # cuDNN
    "cat /usr/include/cudnn.h | grep CUDNN_MAJOR -A 2"
    # python
    "python --version"
    # gawk
    "gawk -V"
    # stanza
    # pandas
    # simpletransformers
    # sentence-transformers
    # scipy
    "pip list"
    # sklearn
    "python -c \"import sklearn; print(sklearn.__version__)\""
)

for cmd in "${CMDS[@]}"
do
    cmd_with_log="${cmd} ${log_cmd}"
    echo "${cmd_with_log}"
    eval "${cmd_with_log}"
done
