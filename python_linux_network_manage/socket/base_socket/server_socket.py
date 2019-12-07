#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: server_socket.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-15 21:17:54
############################

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 8001
BUFSIZ = 1024
ADDR = (HOST, PORT)

server = socket()
server.bind(ADDR)
server.listen(5)

while True:
    print("wating for connectiion")
    client, addr = server.accept()
    print("...connection from {0}".format(addr))

    while True:
        data = server.recv(BUFSIZ)
        if not data:
            break
        server.send("[{0}] {1}".format(ctime(), data.encode('utf-8')))
    server.close()
server.close()
