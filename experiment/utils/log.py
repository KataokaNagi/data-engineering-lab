"""
@file      log.py
@author    Kataoka Nagi (calm1836[at]gmail.com)
@brief     Android-like logging helper
@date      2021-11-13 01:42:13
@version   1.0
@copyright (c) 2021 Kataoka Nagi This src is released under the MIT License, see LICENSE.
"""

from sys import stderr


class Log:

    def __init__(self):
        self.__ENABLE_DEBUG = True
        self.__ENABLE_VERBOSE = True

        self.__RESET = "\033[0m"
        self.__RED = "\033[41m"
        self.__YELLOW = "\033[33m"

    @staticmethod
    def d(self, *args):
        if self.__ENABLE_DEBUG:
            print(args)

    # VERBOSE
    @staticmethod
    def v(self, *args):
        if self.__ENABLE_VERBOSE:
            print(args)

    # ERROR
    @staticmethod
    def e(self, *args):
        print(self.__RED, args, self.__RESET, file=stderr)

    # WARNING
    @staticmethod
    def w(self, *args):
        print(self.__YELLOW, args, self.__RESET)
