#!/bin/bash
#
# @file      venv.sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     (WIP) make venv if not making & pip3 install
# @date      2021-11-11 13:17:34
# @version   1.0
# @see       [venv: Python 仮想環境管理](https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e#%E6%96%B0%E3%81%97%E3%81%84%E7%92%B0%E5%A2%83%E3%81%AE%E4%BD%9C%E6%88%90)
# @see       [[bash]ディレクトリが存在しない場合は作成。存在かつ空でない場合は警告を出力して終了する構文](https://qiita.com/s-katsumata/items/f23fb3fb8c2fc75003a1)
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 
VENV_DIR=./venv
ACTIVATE_DIR_FROM_VENV_DIR=bin/activate
ACTIVATE_DIR="$VENV_DIR/$ACTIVATE_DIR_FROM_VENV_DIR"

function install_if_not_exist() {
    # $1=installer, $2=command
    if !(type "$2" > /dev/null 2>&1); then
        "$1" install "$2";
    else
        echo "$2" "is already installed.";
    fi
}

install_if_not_exist "apt-get" "python3-venv";

# make venv if not exist
if [ ! -d $VENV_DIR ]; then
    python3 -m venv venv;
fi

# activate venv
source $ACTIVATE_DIR;

# install by pip3 in venv
install_if_not_exist "pip3" "cython";
install_if_not_exist "pip3" "spacy";
install_if_not_exist "pip3" "stanza";
python3 -m pip uninstall torch
python3 -m pip3 install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html

# set path (add venv/bin/activate)
# export PYTHONPATH="$PYTHONPATH:/home/nagi/.local/lib/python3.6/site-packages" # tmp (only in current shell)
# echo 'export PYTHONPATH="$PYTHONPATH:/home/nagi/.local/lib/python3.6/site-packages"' >> ~/.bashrc # semipermanent

# deactivate venv
# deactivate
