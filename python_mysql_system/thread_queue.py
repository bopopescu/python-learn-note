#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: thread_queue.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-09 20:03:37
############################

import queue
from threading import Thread
q = queue.Queue()

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()

for i in range(num_work_threads):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

for item in source():
    q.put(item)

q.join()
