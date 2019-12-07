#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: psutil_memory.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-04 21:46:22
############################

import psutil

def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    print(enumerate(symbols))
    for i, s in enumerate(symbols):
        print(i, s)
        prefix[s] = 1 << (i + 1) * 10
        print(prefix[s])
    for s in reversed(symbols):
        # print(reversed(symbols))
        print("s: ",s)
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' %(value, s)
    return  "%sB" % n

# mem = bytes2human(psutil.virtual_memory().total)
mem = bytes2human(psutil.virtual_memory().free + psutil.virtual_memory().buffers
                 + psutil.virtual_memory().cached)
print(mem)
