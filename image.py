#!/usr/bin/env python
# coding=utf-8

from PIL import Image

img = Image.open('./test.jpg')
print((img.format, img.size, img.mode)) 
