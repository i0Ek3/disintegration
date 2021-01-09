#!/usr/bin/env python
# coding=utf-8

from socket import socket

def client(ip, port, size):
    cli = socket()
    cli.connect((ip, port))
    print(cli.recv(size).decode('utf-8'))
    cli.close()

client('localhost', 6666, 1024)
