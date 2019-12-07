#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: python_multi_thread.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-09 19:26:51
############################

import threading
import time

def say_hi(n):
    time.sleep(1)
    print('hello {}'.format(n))

def main():
    for i in range(5):
        thread = threading.Thread(target=say_hi, args=(i,))
        thread.start()

if __name__ == '__main__':
    main()
