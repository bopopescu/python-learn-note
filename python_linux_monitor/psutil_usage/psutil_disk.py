#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: psutil_disk.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-04 22:06:36
############################
import psutil

def get_disk_via_mountpoint(mountpoint):
    disk = [item for item in psutil.disk_partitions() if item.mountpoint ==
            mountpoint ]
    return disk[0].device

disk_info = get_disk_via_mountpoint('/')
print(disk_info)
