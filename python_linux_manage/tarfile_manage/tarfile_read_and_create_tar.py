#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: tarfile_read_and_create_tar.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-03 21:19:49
############################

# 读取一个用gzip算法压缩tar包
with tarfile.open('tarfile_add.tar', mode='r:gz') as out:
# 创建一个用bzip2算法压缩的tar包
with tarfile.open('tarfile_add.tar', mode='w:bz2') as out:

