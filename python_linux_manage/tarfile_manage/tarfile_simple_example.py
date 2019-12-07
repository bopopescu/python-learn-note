#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: tarfile_create_example.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-03 21:14:59
############################

import tarfile
with tarfile.open('taffile_simple_example.py.tar', mode='w') as out:
    out.add('taffile_simple_example.py')
with tarfile.open('taffile_simple_example.py.tar') as t:
    for member_info in t.getmembers():
        print(member_info.name)
