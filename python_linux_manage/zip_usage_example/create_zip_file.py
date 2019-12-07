#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: create_zip_file.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-03 21:54:39
############################

import zipfile
new_zip = zipfile.ZipFile('tarfile_simple_example.py.zip', 'w')
new_zip.write('tarfile_simple_example.py')
new_zip.close()

