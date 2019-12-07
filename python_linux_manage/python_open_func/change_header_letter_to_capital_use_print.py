#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: change_header_letter_to_capital_use_print.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 10:55:50
############################

with open ('data.txt') as  inf, open('out_use_print.txt','w') as outf:
    for line in inf:
        print(*[word.capitalize() for word in line.split()], file=outf)
