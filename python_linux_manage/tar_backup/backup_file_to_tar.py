#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: backup_file_to_tar.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-03 21:24:57
############################

from __future__ import print_function
import os
import tarfile
import datetime
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

def main():
    patterns = ['.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "all_image_{0}.tar.gz".format(now)
    with tarfile.open(filename, 'w:gz') as f:
        for item in find_specific_files('.', patterns):
            f.add(item)

if __name__ == '__main__':
    main()
