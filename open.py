#!/usr/bin/env python3
# coding=utf-8

def oopen(filename, mode, encoding='utf-8'):
    f = None
    try:
        f = open(filename, mode)
        print(f.read())
    except FileNotFoundError:
        print('No files here!')
    except LookupError:
        print('Unkonwn encoding!')
    except UnicodeDecodeError:
        print('Wrong decoding!')
    finally:
        if f:
            f.close()

def wopen(filename, mode, encoding='utf-8'):
    try:
        with open(filename, mode) as f:
            print(f.read())
    except FileNotFoundError:
        print('No files here!')
    except LookupError:
        print('Unkonwn encoding!')
    except UnicodeDecodeError:
        print('Wrong decoding!')


#wopen('./pytest/test.txt', 'r')
