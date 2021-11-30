"""
@file      log.py
@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     Android-like logging helper
@date      2021-11-13 01:42:13
@version   1.0
@copyright (c) 2021 Kataoka Nagi This src is released under the MIT License.
"""

from sys import stderr


class Log:

    # @see [Pythonでのstatic変数／static関数について考える]
    # (https://qiita.com/daiyada/items/5865cef7aa068363ac14)
    __ENABLE_DEBUG = True
    __ENABLE_VERBOSE = True

    __RESET = "\033[0m"
    __RED = "\033[41m"
    __YELLOW = "\033[33m"

    @staticmethod
    def d(*args):
        if Log.__ENABLE_DEBUG:
            print(*args)

    # VERBOSE
    @staticmethod
    def v(*args):
        if Log.__ENABLE_VERBOSE:
            print(*args)

    # ERROR
    @staticmethod
    def e(*args):
        print(Log.__RED, *args, Log.__RESET, file=stderr)

    # WARNING
    @staticmethod
    def w(*args):
        print(Log.__YELLOW, *args, Log.__RESET)
