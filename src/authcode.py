#!/usr/bin/env python3
# coding=utf-8

import random

"""
Moudle authcode which can generate random code follows rule.
"""

def generate_code(size=6):
    std_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    spec_chars = '+-_*/%?!@#$^&='
    loc1 = len(std_chars) - 1 # 61
    loc2 = len(spec_chars) - 1 # 13
    code = ''

    anwser = input('standard one or mix with special sign? [(F)ore/(B)ack]: ')
    if anwser == 'F':
        for _ in range(size):
            index = random.randint(0, loc1)
            code += std_chars[index]
        print(code)
    elif anwser == 'B':
        for _ in range(size // 2):
            idx1 = random.randint(0, loc1)
            idx2 = random.randint(0, loc2)
            code += std_chars[idx1] + spec_chars[idx2]
        print(code)
    else:
        pass

size = int(input('input a number: '))

if size > 0:
    generate_code(size)
else:
    generate_code()

