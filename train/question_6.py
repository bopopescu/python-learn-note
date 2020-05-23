'''
Python socket编程，创建tcp客户端，获取baidu.com首页内容并保存在本地文件里

'''

import socket


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('www.baidu.com', 80))
    client.send("GET / HTTP/1.1\r\nHost:"
                "www.baidu.com\r\nConnection:close\r\n\r\n".encode('utf-8'))
    buff = client.recv(1024)
    data = b''
    while len(buff):
        data += buff
        buff = client.recv(1024)
    with open('baidu.html', "a+") as f:
        f.write(data.decode())
