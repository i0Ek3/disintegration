#!/usr/bin/env python
# coding=utf-8

import re

def filter(str):
    filtered = re.sub('[草操艹]|cao|fuck|bitch|cunt|slut|motherfucker|pussy|jb|tm|[你尼][妈玛]|nmsl|mmp|rnqj|\
                      |傻[比逼屄吊屌]|沙雕|煞笔|sb', '^_^', str, flags=re.IGNORECASE)
    print(filtered)

filter('草, 你TM是煞笔吗？fuck you')
filter('cao你个jb玩意儿')
filter('艹，臭傻逼')
filter('cao尼玛傻屌')
filter('hey pussy, you motherfucker')
filter('you just like a bitch')
filter('you\'re cunt')
filter('slut pussy')
