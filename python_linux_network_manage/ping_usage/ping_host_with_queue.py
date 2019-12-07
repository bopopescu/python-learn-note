#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: ping_host_with_queue.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-06 14:27:11
############################
from __future__ import print_function
import subprocess
import threading
from Queue import Queue
from Queue import Empty

def call_ping(ip):
    if subprocess.call(['ping', '-c', '1', ip]):
        print("{0} is alive".format(ip))
    else:
        print("{0} is unreacheable".format(ip))

def is_reacheable(q):
    try:
        while True:
            ip = q.get_nowait()
            call_ping(ip)
    except:
        pass

def main():
    q = Queue()
    with eopn('ips.txt') as f:
        for line in f:
            q.put(line)

    threads = []
    for i in range(10):
        thr = threading.Thread(target=is_reacheable, args=(q,))
        thr.start()
        thread.append(thr)

    for thr in threads:
        thr.join()

if __name__ == '__main__':
    main()
