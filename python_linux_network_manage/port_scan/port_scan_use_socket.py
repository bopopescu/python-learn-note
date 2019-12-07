#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: port_scan_use_socket.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-06 14:38:24
############################

from __future__ import print_function
from socket import *

def conn_scan(host, port):
    conn = socket(AF_INET, SOCK_STREAM)
    try:
        conn.connect((host, port))
        print(host, port, 'is avaliable')
    except Exception as e:
        print(host, port, 'is not avaliable')
    finally:
        conn.close()

def main():
    host = '47.104.148.179'
    for port in range(20, 5000):
        conn_scan(host, port)

if __name__ == '__main__':
    main()

