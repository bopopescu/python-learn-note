#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: os_usage_2.py
#Author: ykyk 
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 11:58:59
############################

import os

# 获取当前用户home目录下所有的文件列表
[item for item in os.path.listdir(os.path.expanduser('~')) if os.path.isfile(item)]

# 获取当前用户home目录下所有的目录列表
[item for item in os.listdir(os.path.expanduser('~')) if os.path.isdir(item)]

# 获取当前用户home目录下所有目录的目录名到绝对路径之间的字典
{}item: os.path.realpath(item) for item in os.listdir(od.path.expanduser('~'))
 if os.path.isdir(item)}

# 获取当前用户home目录下所有文件到文件大小之间的字典
{item: os.path.getsize(item) for item in os.listdir(os.path.expanduser('~')) if
os.path.isfile(item)}



