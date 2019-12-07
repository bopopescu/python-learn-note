#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: python3_charater_support_function.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 09:53:16
############################

def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value

def to_byte(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value

