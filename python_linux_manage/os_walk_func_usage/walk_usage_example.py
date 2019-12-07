#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: walk_usage_example.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-02 20:39:44
############################

import os
import fnmatch

images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
matches = []

for root, dirnames, filenames in os.walk(os.path.expanduser("~")):
    for extensions in images:
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
    # if 'exclude_dir' in dirnames:
        # dirnames.remove('exclude_dir')
print(matches)
