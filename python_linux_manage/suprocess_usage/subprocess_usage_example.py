#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: subprocess_usage_example.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-04 13:35:07
############################
# 使用subprocess 封装Popen

import subprocess

def execute_cmd(cmd):
    p = subprocess.Popen(cmd,
                         shell = True,
                         stdin = subprocess.PIPE,
                         stdout = subprocess.PIPE,
                         stderr = subprocess.PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout

if __name__ == '__main__':
    command_result = execute_cmd('ls')
    print(command_result)
