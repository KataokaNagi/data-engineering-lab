# -*- coding: utf-8 -*-
"""txt_translator.py

# txt_translator.py

## 基本情報
- author
    - Kataoka Nagi (calm1836[at]gmail.com)
- brief
    - Translate Japanese Fake News Dataset 2 txt
- date
    - 2021-09-12
- version
    - 1.0
- copyright (c) 2021 Kataoka Nagi
    - This src is released under the MIT License, see LICENSE.

## 要件
- 変換前データ
    - txtファイル
        - 指定した任意の言語
        - \nで改行
    - 行
        - 各記事に対応
    - 列
        - 1記事の全文章
- 変換後データ
    - txtファイル
        - 指定した任意の言語
        - \nで改行
    - 行
        - 各記事に対応
    - 列
        - 1記事の全文章

## [DeepL API](https://www.deepl.com/docs-api/)
- 制限
    - utf-8の文書にのみ対応
    - 50万文字/月
    - 最大50テキスト/回
    - GETよりPOSTを推奨
    - 内部で文を分割して翻訳
    - 長すぎる文章には対応できない

## 使い方
- DeepL API Freeの認証キーを代入
    - DEEPL_API_KEY
    - Webに公開しないこと
- txtファイルのパスを代入
    - 翻訳前は PRE_TRANS_TXT_DIR
    - 翻訳後は POST_TRANS_TXT_DIR
- txtファイルの言語情報を代入
    - 翻訳前は PRE_TRANS_LANG
    - 翻訳後は POST_TRANS_LANG
    - 形式は[DeepL APIのsource_kang, target_lang](https://www.deepl.com/docs-api/translating-text/request/)に準拠
- 実行時にGoogle認証
    - 認証後に表示されるコードを入力

## Setup
"""

import requests
import time
import datetime

# SAVING_TXT_NAME = "japanese_fakenews_dataset_2_en.txt"
# PRE_TRANS_TXT_DIR = "G:\\マイドライブ\\lab\\experiment\\japanese_fakenews_dataset_2_txt\\japanese_fakenews_dataset.txt"
# POST_TRANS_TXT_DIR = "G:\\マイドライブ\\lab\\experiment\\txt_translator\\" + SAVING_TXT_NAME

IN_TXT_NAME = "en.txt"
OUT_TXT_NAME = "jp.txt"
PRE_TRANS_TXT_DIR = "./" + IN_TXT_NAME
POST_TRANS_TXT_DIR = "./" + OUT_TXT_NAME

# PRE_TRANS_LANG = "JA"  # Japanese
# POST_TRANS_LANG = "EN-US"  # English(American)
PRE_TRANS_LANG = "EN"  # English(American)
POST_TRANS_LANG = "JA"  # Japanese

SLEEP_SEC_PER_TRANS = 20

############################################################
# Don't publish on the web
DEEPL_API_DIR = "./.deepl_api_key"
deepl_api_key = ""
############################################################

with open(DEEPL_API_DIR, "r", encoding="utf_8") as f:
    deepl_api_key = f.readlines()


"""### Mount google drive"""

# from google.colab import drive
# drive.mount('/content/drive')

"""## Download txt"""

# from google.colab import files

pre_trans_txts = []
with open(PRE_TRANS_TXT_DIR, "r", encoding="utf_8") as f:
    pre_trans_txts = f.readlines()

print(pre_trans_txts[:(len(pre_trans_txts) % 5)])

"""## DeepL translation
- [DeepL APIをPythonから利用して日本語の文章を翻訳する](https://deepblue-ts.co.jp/nlp/deepl-api-python/)

### Estimate translation time
"""


# TIME_DIFF = 9  # between jp & colab server
TIME_DIFF = 0

sum_sleep_sec = SLEEP_SEC_PER_TRANS * len(pre_trans_txts)
trans_hour = sum_sleep_sec / 60 / 60

now_datetime = datetime.datetime.now()
now_datetime += datetime.timedelta(hours=TIME_DIFF)
fin_trans_datetime = now_datetime + datetime.timedelta(seconds=sum_sleep_sec)

print("trans_hour:")
print(trans_hour)
print()
print("fin_trans_datetime:")
print(fin_trans_datetime)
print()

"""### Translation"""

# !pip install requests


NUM_TRANS = len(pre_trans_txts)
NUM_TRANS_PER_PRINT = 100

# debug
# NUM_TRANS = 3
# NUM_TRANS_PER_PRINT = 2

post_trans_txts = []
cnt_backup = 0

for i in range(NUM_TRANS):
    params = {
        "auth_key": deepl_api_key,
        "text": pre_trans_txts[i].rstrip("\n"),
        "source_lang": PRE_TRANS_LANG,
        "target_lang": POST_TRANS_LANG
    }
    request = requests.post(
        "https://api-free.deepl.com/v2/translate",
        data=params)
    result = request.json()
    post_trans_txts.append(result["translations"][0]["text"])
    time.sleep(SLEEP_SEC_PER_TRANS)

    # debug
    # print(result)
    print('.', end='', flush=True)
    if ((i % NUM_TRANS_PER_PRINT) ==
            NUM_TRANS_PER_PRINT - 1) or (i == NUM_TRANS - 1):
        print()
        print("{}/{} translated".format(i + 1, NUM_TRANS))
        if len(post_trans_txts[i]) > 20:
            print("{}th doc: {} ... {}".format(
                i + 1, post_trans_txts[i][:10], post_trans_txts[i][-10:]))

        # backup docs
        backup_txt_dir = POST_TRANS_TXT_DIR[:-
                                            4] + "_{}".format(cnt_backup) + ".txt"
        range_l = NUM_TRANS_PER_PRINT * cnt_backup
        range_r = NUM_TRANS_PER_PRINT * (cnt_backup + 1)
        if range_r > NUM_TRANS:
            range_r = NUM_TRANS
        with open(backup_txt_dir, 'w', encoding="utf-8") as f:
            for txt in post_trans_txts[range_l:range_r]:
                f.write("%s\n" % txt.rstrip("\n"))
        cnt_backup += 1
        print("backuped from {}th to {}th".format(range_l, range_r - 1))


"""## Write"""

with open(POST_TRANS_TXT_DIR, 'w', encoding="utf-8") as f:
    for txt in post_trans_txts:
        f.write("%s\n" % txt.rstrip("\n"))

print("done")
