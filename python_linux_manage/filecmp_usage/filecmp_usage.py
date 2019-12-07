#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: filecmp_usage.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-03 14:39:59
############################

In [1]: import filecmp

In [7]: filecmp.cmp('a.txt','b.txt')
Out[7]: False

In [8]: filecmp.cmp('a.txt','c.txt')
Out[8]: True

In [12]: filecmp.cmp('a.txt', 'a_copy.txt')
Out[12]: True

In [2]: filecmp.cmpfiles('dir1','dir2',['a.txt','b.txt','c.txt','a_copy.txt'])
Out[2]: (['a.txt', 'b.txt', 'c.txt'], [], ['a_copy.txt'])

In [5]: d = filecmp.dircmp('dir1','dir2')

In [6]: d.report()
diff dir1 dir2
Only in dir1 : ['a_copy.txt']
Only in dir2 : ['subdir2']
Identical files : ['a.txt', 'b.txt', 'c.txt']
Common subdirectories : ['subdir1']

In [7]: d.left_list
Out[7]: ['a.txt', 'a_copy.txt', 'b.txt', 'c.txt', 'subdir1']

In [8]: d.left_only
Out[8]: ['a_copy.txt']

In [9]: d.right_only
Out[9]: ['subdir2']

