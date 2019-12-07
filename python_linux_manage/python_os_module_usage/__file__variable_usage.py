#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: __file__variable_usage.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 11:37:52
############################

# __file__ 变量的用法
import 
import os
print("current directory : ", os.getcwd())
path = os.path.abspath(__file__)
print("full path of current file : ", path)
print("parent directory of current file :",
      os.path.abspath(os.path.join(os.path.dirname(path), os.path.pardir)))
os.path.abspath

