#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: use_python_create_zip_file_in_command_line.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-03 22:00:32
############################
'''
    -l 显示zip格式压缩包中的文件列表
    -c 创建zip格式压缩包
    -e 提取zip格式压缩包
    -t 验证文件是一个有效的zip格式压缩包
'''


python -m zipfile -c monty.zip spam.txt eggs.txt
python -m zipfile -e monty.zip target-dir/ 
python -m zipfile -l monty.zip

