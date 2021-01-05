#!/usr/bin/env python
# coding=utf-8

import os
import time

def main():
    content = 'Hello there, welcome here to learn Python.\t'
    while True:
        os.system('clear')
        print(content)
        time.sleep(0.3)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
