#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: use_glob_to_find_file.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 20:29:18
############################

In [23]: import glob

In [24]: glob.glob('*.txt')
Out[24]: ['a1.txt', 'b1.txt']

In [25]: glob.glob('[a-c]?.jpg')
Out[25]: ['c2.jpg']

In [26]: glob.glob('[!a-c]?.jpg')
Out[26]: ['d2.jpg']

