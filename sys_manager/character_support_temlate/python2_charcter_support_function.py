#!/usr/bin/python
# -*- coding:utf-8 -*-
############################
#File Name: python2_charcter_support_function.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 09:49:22
############################

def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = uncode_or_str.decode('utf-8')
    else:
        value unicode_or_str
    return value

def to_str(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.encode('utf-8')
    else:
        value = unicode_or_str
    return value

