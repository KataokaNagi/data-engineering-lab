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

# function install_if_not_exist() {
#     # $1=installer, $2=command
#     if !(type "$2" > /dev/null 2>&1); then
#         "$1" install "$2";
#     else
#         echo "$2" "is already installed.";
#     fi
# }

##################################################
# apt preparation
##################################################
sudo apt update
sudo apt upgrade


##################################################
# change python version
# @see [Ubuntuでpythonのバージョンを切り換える](https://qiita.com/piyo_parfait/items/5abbe4bee2495a62acdc)
##################################################
whitch python
ls /usr/bin/ | grep python
which update-alternatives
sudo update-alternatives --config python
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 2
sudo update-alternatives --config python


##################################################
# setup venv
##################################################

apt-get install python3-venv;

# make venv if not exist
if [ ! -d $VENV_DIR ]; then
    python3 -m venv venv --system-site-packages;
fi

# activate venv
source $ACTIVATE_DIR;

##################################################
# install by pip in venv
##################################################

# preprocess_03_split_sentences.py
python3 -m pip install cython
pip install -U pip setuptools wheel
pip install -U spacy
python3 -m pip install stanza

# debug for tensorflow
python3 -m pip uninstall torch
python3 -m pip install torch==1.8.2+cu111 torchvision==0.9.2+cu111 torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html

# process_01_train_classifier_as_claim_or_evidence.py
python3 -m pip uninstall importlib-metadata
python3 -m pip install importlib-metadata==4.2.0
python3 -m pip install pandas
python3 -m pip install transformers
python3 -m pip install simpletransformers
python3 -m pip install sklearn
# python3 -m pip uninstall importlib-metadata
# python3 -m pip3 install importlib-metadata==4.8.2
python3 -m pip install wandb
wandb login <API keysを記述> # https://wandb.ai/settings

# for deepl
python3 -m pip install requests

# util
sudo apt install rename

# process_03_articles_features_calculator
python3 -m pip install sentence-transformers


##################################################
# LaTeX
# @see [Ubuntu 18.04 LTS に LaTeX をインストール](https://qiita.com/willow-micro/items/6b13e2038d628c33be8e)
# @see [VSCode で最高の LaTeX 環境を作る](https://qiita.com/rainbartown/items/d7718f12d71e688f3573)
##################################################
sudo apt install \
evince texlive-fonts-extra \
texlive-fonts-recommended texlive-lang-cjk xdvik-ja
sudo apt install texlive-full
# platex hoge.tex
# dvipdfmx hoge.dvi
# evince hoge.pdf &

##################################################
# set path (add venv/bin/activate)
##################################################
# export PYTHONPATH="$PYTHONPATH:/home/nagi/.local/lib/python3.6/site-packages" # tmp (only in current shell)
# echo 'export PYTHONPATH="$PYTHONPATH:/home/nagi/.local/lib/python3.6/site-packages"' >> ~/.bashrc # semipermanent

##################################################
# deactivate venv
##################################################
# deactivate
