#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: tarfile_create_example.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-03 21:14:59
############################

import tarfile
with tarfile.open('send_monitor_info_to_mail.tar', mode='w') as out:
    out.add('README.md')
    out.add('python2_monitor_sys.py')
    out.add('monitor.html')
    out.add('requirment.txt')
with tarfile.open('send_monitor_info_to_mail.tar') as t:
    for member_info in t.getmembers():
        print(member_info.name)
