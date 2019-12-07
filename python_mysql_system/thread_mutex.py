#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: thread_mutex.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-09 19:56:21
############################

import threading

lock = threading.Lock()
num = 0

def incre(count):
    global num
    while count > 0:
        with lock:
            num += 1
        count -= 1

def main():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=incre, args=(10000,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print('expected value is ', 10 * 10000, "real value is", num)

if __name__ == '__main__':
    main()
