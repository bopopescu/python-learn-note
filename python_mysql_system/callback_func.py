#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: callback_func.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-09 15:24:10
############################

def greeting(f):
    f()

def say_hi():
    print('Hi~')

def say_hello():
    print('Hello~')

greeting(say_hi)
greeting(say_hello)
