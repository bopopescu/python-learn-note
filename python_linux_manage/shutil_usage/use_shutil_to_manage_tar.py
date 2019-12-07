#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: use_shutil_to_manage_tar.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-04 13:12:12
############################
'''
In [1]: import shutil

In [2]: shutil.get_archive_formats()
Out[2]: 
    [('bztar', "bzip2'ed tar-file"),
     ('gztar', "gzip'ed tar-file"),
     ('tar', 'uncompressed tar file'),
     ('xztar', "xz'ed tar-file"),
     ('zip', 'ZIP file')]
'''

In [4]: cd /root/python_linux_manage/shutil_usage/
/root/python_linux_manage/shutil_usage

In [5]: ls
shutil_usage_example.py

In [6]: shutil.make_archive('backup', 'gztar')
Out[6]: 'backup.tar.gz'

In [7]: shutil.make_archive('backup', 'zip')
Out[7]: 'backup.zip'

In [8]: ls
backup.tar.gz  backup.zip  shutil_usage_example.py

In [9]: import tarfile
In [10]: f = tarfile.open('backup.tar.gz','r:gz')

In [12]: f.getnames()
Out[12]: ['.', './.use_shutil_to_manage_tar.py.swp', './shutil_usage_example.py']

n [18]: shutil.unpack_archive('backup.tar.gz',
                              extract_dir='/root/python_linux_manage/shutil_usage/back')

In [19]: ls
back/  backup.tar.gz  backup.zip  shutil_usage_example.py

In [20]: ls back/
shutil_usage_example.py


