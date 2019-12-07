#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: ping_host.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-06 14:06:51
############################

# from __future__ import print_function

import subprocess
import threading

def is_reachable(ip):
    if subprocess.call(['ping', '-c','1', ip]):
        print('{0} is alive'.format(ip))
    else:
        print('{0} is unreacheale'.format(ip))

def main():
    with open('ips.txt') as f:
        lines = f.readlines()
        threads = []
        for line in lines:
            thr = threading.Thread(target=is_reachable, args=(line.))
            thr = start()
            threads.append(thr)

        for thr in threads:
            thr.join()

if __name__ == '__main__':
    main()
