#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: port_scan_use_telnetlib.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-06 14:46:05
############################

from __future__ import print_function

import telnetlib

def conn_scan(host, port):
    t = telnetlib.Telnet()
    try:
        t.open(host, port ,timeout = 1)
        print(host, port, 'is avaliable')
    except Exception as e:
        print(host, port, 'is not avaliable')
    finally:
        t.close()

def main():
    host = '47.104.148.179'
    for port in range(80, 5000):
        conn_scan(host, port)

if __name__ == '__main__':
    main()

