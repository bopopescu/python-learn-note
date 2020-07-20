#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: re_split_example.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-01 21:48:46
############################

In [6]: text = "MySQL subordinate binlog position: main host '10.173.33.25',
filename 'mysql-bin.000002', postion '524493
   ...: 3660'"

In [8]: re.split(r"[':,\s]+", text.strip("'")
Out[8]: 
    ['MySQL',
     'subordinate',
     'binlog',
     'position',
     'main',
     'host',
     '10.173.33.25',
     'filename',
     'mysql-bin.000002',
     'postion',
     '5244933660']
