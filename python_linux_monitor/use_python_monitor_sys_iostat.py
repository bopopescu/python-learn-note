#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################File Name: use_python_monitor_sys_iostat.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-04 21:23:53
############################

from __future__ import print_function
from collections import namedtuple

Disk = namedtuple('Disk', 'major_number minor_number divice_name'
                  ' read_count read_merged_count read_sections'
                  ' time_spent_reading write_count write_merged_count'
                  ' write_sections time_spent_write io_requests'
                  ' time_spent_doing_io weighted_time_spent_doing_io')

def get_disk_info(device):
    """
    从/proc/diskstats中读取磁盘io信息
    [root@ykyk Pydiction]# cat /proc/diskstats 
     253       0 vda  72957 74 2334738 140208 346500 209614 13735640 6844641 0  150951 6984769
     253       1 vda1 72872 74 2330602 140195 344821 209614 13735640 6844037 0 150342 6984152
    """
    with open('/proc/diskstats') as f:
        for line in f:
            if line.split()[2] == device:
                return Disk(*(line.split())) 
    raise RuntimeError("device ({0}) not found !.".format(device))

def main():
    disk_info = get_disk_info('vda')
    print(disk_info)
    print('disk write times: {0}'.format(disk_info.write_count))
    print('disk write byte time: {0}'.format(int(disk_info.write_sections) *
                                             512))
    print('disk write latency: {0}'.format(disk_info.time_spent_write))

if __name__ == '__main__':
    main()
