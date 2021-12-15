# -*- coding: utf-8 -*-
"""
@file      preprocess_06_rm_duplicate_sentences.py
@author    Kataoka Nagi (calm1836[at]gmail.com)
@date      2021-12-15 20:32:19
@version   1.0
@see       [Pythonで重複してる文を削除するプログラム](https://qiita.com/kataware/items/5f1191170a018d6defce)
@copyright This file includes the work that is distributed in the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
@copyright (c) 2021 Kataoka Nagi
"""


def main():
    import sys
    import re
    from utils.log import Log as log

    # input file dir
    txt_dir = ""
    dist_dir = ""

    try:
        txt_dir = sys.argv[1]
        dist_dir = sys.argv[2]
    except IndexError:
        print('Usage: {0} {1} TEXTFILE'.format(txt_dir, dist_dir))
        sys.exit(1)

    log.d("in_file_name:", txt_dir)
    log.d("out_file_name:", dist_dir)

    # input lines into unique set
    with open(txt_dir, 'r+') as f:
        unique_lines = {line.rstrip() for line in f}

    # output lines
    dist_lines = [line + "\n" for line in unique_lines]
    log.v("dist_lines[0]:\n", dist_lines[0])

    with open(dist_dir, 'w+') as f:
        f.writelines(dist_lines)
        log.d("done\n")


if __name__ == "__main__":
    main()
