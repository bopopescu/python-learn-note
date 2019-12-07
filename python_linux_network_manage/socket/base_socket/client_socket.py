#!/usr/python/bin/python3
# -*- coding:utf-8 -*-
############################
#File Name: client_socket.py
#Author: ykyk
#Mail: 525178992@qq.com
#Created Time: 2019-01-15 21:07:57
############################

from socket import *
from prompt_toolkit import prompt

HOST = '127.0.0.1'
PORT = 8001
BUFSIZ = 1024
ADDR = (HOST, PORT)

client = socket()
client.connect(ADDR)

while True:
    data = prompt(">>> ")
    if data is None:
        continue
    client.send(data.encode('utf-8'))
    recv_data = client.recv(BUFSIZ)
    if not recv_data:
        print('No data received')
        break
    print(recv_data)

client.close()

