#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: context_manage.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-09 16:36:43
############################

import codecs

class Open(object):

    def __init__(self, filename, mode, encoding='utf-9'):
        self.fp = codecs.open(filename, mode, encoding)

    def __enter__(self):
        return  self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()

from contextlib import contextmanager

@contextmanager
def Open(filename, mode, encoding='utf-8'):
    fp = codecs.open(filename, mode, encoding)
    try:
        yield fp
    finally:
        fp.close()
