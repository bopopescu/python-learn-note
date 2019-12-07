#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: re_sub_example.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-01 21:48:46
############################

In [4]: text = 'Today is 12/1/2017. PyCon starts 5/25/2017.'

In [5]: re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
Out[5]: 'Today is 2017-12-1. PyCon starts 2017-5-25.'
