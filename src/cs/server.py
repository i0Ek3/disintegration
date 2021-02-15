#!/usr/bin/env python
# coding=utf-8

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime

def server(ip, port, size):
    ser = socket(family=AF_INET, type=SOCK_STREAM)
    ser.bind((ip, port))
    ser.listen(size)
    print('listening...')

    while True:
        cli, addr = ser.accept()
        print(str(addr) + 'connected to server.')
        cli.send(str(datetime.now()).encode('utf-8'))
        cli.close()

def main():
    server('localhost', 6666, 512)

# usage
# run cmd: python server.py in one terminal
# run cmd: telnet localhost 6666 in anthor terminal
main()
