#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: os_module_usage_example.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 20:58:38
############################

"""
     1）找到某个目录及子目录下最大的十个文件
     2）找到某个目录及子目录下最老的十个文件
     3）找到某个目录及子目录下，所有文件名中包含“mysql-bin”的文件
     4）找到某个目录及字幕里下，排除.git子目录以后所有的Python源文件
"""
import os
import fnmatch

def is_file_match(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename, patterns):
                yield os.path.join(root, filename)

    for d in exclude_dirs:
        if d in dirnames:
            dirnames.remove(d)

# 1)
for item in find_specific_files('.'):
    print(item)

# 2)
print('2')
patterns = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
# exclude_dirs = ['/root']
for item in find_specific_files('/root', patterns):
    print(item)

# 2-1)
print('2-1')
patterns = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
exclude_dirs = ['/root']
for item in find_specific_files('/root', patterns):
    print(item)
# 3)
print('3')
files = {name: os.path.getsize(name) for name in find_specific_files('/root/')}
print(files.items())
result = sorted(files.items(), key=lambda d:d[1], reverse=True)[:10]
for i, t in enumerate(result, 1):
    print(i, t[0], t[1])
