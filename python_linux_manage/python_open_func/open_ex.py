#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: open_ex.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 10:26:23
############################


In [12]: ls
data.txt

In [13]: f = open('data.txt')

In [14]: print(f.read())
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.conjugate
Comlex is better than comlicated.


In [15]: f.close()

In [15]: f.close()

In [16]: f = open('data1.txt', 'w')

In [20]: f = open('data1.txt', 'x')
---------------------------------------------------------------------------
FileExistsError                           Traceback (most recent call last)
<ipython-input-20-513e792d1659> in <module>
----> 1 f = open('data1.txt', 'x')

FileExistsError: [Errno 17] File exists: 'data1.txt'

In [21]: f = open('data2.txt', 'x')

In [22]: f.write('hello, world')
Out[22]: 12

In [23]: f.close()

