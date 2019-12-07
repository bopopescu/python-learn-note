#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: change_header_letter_to_capitals.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 10:43:14
############################

with open ('data.txt') as  inf, open('out.txt','w') as outf:
    for line in inf:
        outf.write(" ".join([word.capitalize() for word in line.split()]))
        outf.write("\n")
