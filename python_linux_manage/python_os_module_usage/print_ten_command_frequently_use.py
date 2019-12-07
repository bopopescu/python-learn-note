#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: print_ten_command_frequently_use.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 15:15:31
############################

# 打印10条最常用命令
import os
from collections import Counter

c = Counter()

with open(os.path.expanduser('~/.bash_history')) as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]] += 1
print(c.most_common(10))
