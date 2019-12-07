#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: fnmatch_example.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 20:17:26
############################

In [8]: import os

In [9]: import fnmatch

In [10]: os.listdir('.')
Out[10]: ['c2.jpg', 'd2.jpg', 'a1.txt', '.fnmatch_example.py.swp', 'b1.txt']

In [12]: [name for name in os.listdir('.') if fnmatch.fnmatch(name, '*.jpg')]
Out[12]: ['c2.jpg', 'd2.jpg']

In [13]: [name for name in os.listdir('.') if fnmatch.fnmatch(name, '[a-c]*')]
Out[13]: ['c2.jpg', 'a1.txt', 'b1.txt']

In [14]: [name for name in os.listdir('.') if fnmatch.fnmatch(name, '[a-c]?.txt')]
Out[14]: ['a1.txt', 'b1.txt']

In [16]: [name for name in os.listdir('.') if fnmatch.fnmatch(name, '[!a-c]*')
Out[16]: ['d2.jpg', '.fnmatch_example.py.swp']

In [17]: names = os.listdir('.')

In [18]: names
Out[18]: ['c2.jpg', 'd2.jpg', 'a1.txt', '.fnmatch_example.py.swp', 'b1.txt']

In [20]: fnmatch.filter(names, '[a-c]?.txt')
Out[20]: ['a1.txt', 'b1.txt']

In [21]: fnmatch.filter(names,'[!a-c]*')
Out[21]: ['d2.jpg', '.fnmatch_example.py.swp']

