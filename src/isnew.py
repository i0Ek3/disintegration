#!/usr/bin/env python
# coding=utf-8

def isNewer(yes, ret=True):
    if ret == True and yes == 'Yes':
        print('Hello, freshbird!')
    elif ret == True and yes == 'No':
        print('Here we go, driver!')
    else:
        print('Your request was dined!')
