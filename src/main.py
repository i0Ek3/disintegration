#!/usr/bin/env python
# coding=utf-8

from isnew import isNewer
import logx as lg

y = 'Yes'
n = 'No'

def main():
    yes = input('Are you newer for Python? [Yes or No]: ')
    isNewer(yes)

    beg = int(input("Please input a number as begin: "))
    end = int(input("Please input a number as end: "))
    base = int(input("Please input a number as base: "))
    lg.logx(beg, end, base)

if __name__ == '__main__':
    main()
