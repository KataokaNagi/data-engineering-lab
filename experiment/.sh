#!/bin/bash
#
# @file      .sh
# @author    Kataoka Nagi (calm1836[at]gmail.com)
# @brief     note of all experiments sh
# @date      2021-12-05 04:39:44
# @version   1.0
# @copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
# 

bash venv.sh

# make ./covid-19-news-articles/*-articles_preprocess-01_extract-column-c.csv with LibreOffice

bash preprocess_02_awk.sh
# bash preprocess_02_awk.sh -d

bash preprocess_03_split_sentences.sh -l --stanza
bash preprocess_03_split_sentences.sh -l --spacy
# bash preprocess_03_split_sentences.sh -ld --stanza
# bash preprocess_03_split_sentences.sh -ld --spacy

# make ./IBM_Debater_(R)_CE-EMNLP-2015.v3/claims_preprocess-01_extract-column-c with LibreOffice
# make ./IBM_Debater_(R)_CE-EMNLP-2015.v3/evidence_preprocess-01_extract-column-c with LibreOffice

bash preprocess_04_for-debater-dataset.sh
# bash preprocess_04_for-debater-dataset.sh -d

bash preprocess_04_for-debater-dataset.sh
# bash preprocess_04_for-debater-dataset.sh -d

# bash process_01_train_classifier_as_claim_or_evidence.sh
bash process_01_train_classifier_as_claim_or_evidence.sh -l

# bash process_02_exe_classifier_as_claim_or_evidence.sh
bash process_02_exe_classifier_as_claim_or_evidence.sh -l
# bash process_02_exe_classifier_as_claim_or_evidence.sh -dl
