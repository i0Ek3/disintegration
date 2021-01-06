#!/usr/bin/env python
# coding=utf-8

import sys

list = [1, 2, 3, 4, 5]
print(list)
list.append(10)
print(list)
list2 = list.insert(1, 20)
print(list2)

if 3 in list:
    list.remove(3)
else:
    list.add(3)

print(list)


f = [x+y for x in 'abcdefg' for y in '1234567']
print(sys.getsizeof(f))
for v in f:
	print(v)
print(sys.getsizeof(v))


t = ('a', 1, False)
print(t)
for v in t:
    print(v)

set1 = {1, 2, 2, 3, 3, 5}
print(set1)
set2 = set((1, 2, 2, 3))
print(set2)
set3 = {n for n in range(1, 3) if n % 2 == 1 or n % 3 == 0}
print(set3)

def oopen():
    f = open('test.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()

import json
json.dump()

import requests
requests.
