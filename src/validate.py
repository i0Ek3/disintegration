#!/usr/bin/env python
# coding=utf-8

import re

def validate(str, mode):

    """
    regex example

    mail address: 
        ^[a-z][a-z0-9_\.]+@[a-z]+(\.[a-z]+)+$

    phone number: 
        ^1[3-9]\d{9}$

    fixed line: 
        ^0[1,2,4-9][0-9]\d{0,1}$

    Chinese: 
        ^[\u4E00-\u9FA5]
    
    ref: 
        https://github.com/cdoco/learn-regex-zh
        https://github.com/cdoco/common-regex
    """

    # username = input('please input your username: ')
    # number = input('please input your number: ')

    if str:
        if mode == 'username':
            m1 = re.match(r'^[a-zA-Z][a-zA-Z0-9_]{3,11}$', str)
            if not m1:
                print('invalid username.')
            else:
                print('%s is correct' % str)
        elif mode == 'number':
            m1 = re.match(r'^1[3-9]\d{9}$', str)
            if not m1:
                print('invalid number.')
            else:
                print('%s is correct' % str)
        else:
            print('invalid input.')

    else:
        print('invalid string.')

# cases
# username
validate('a123', 'username')
validate('a123456789', 'username')
validate('0abc3r', 'username')
validate('abc3r09ksdfje3', 'username')
validate('abc', 'username')
validate('0abc_', 'username')
validate('abc_abc', 'username')
validate('abcdef', 'username')
validate('Abcdef', 'username')
validate('abc123', 'username')

# number
validate('13323333333', 'number')
validate('133233333', 'number')
validate('03323333333', 'number')
validate('1332333333333', 'number')
validate('23323333333', 'number')
validate('12323333333', 'number')

# mix
validate('13323333333', 'username')
validate('0abc123', 'number')
