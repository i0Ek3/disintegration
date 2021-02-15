#!/usr/bin/env python
# coding=utf-8

from PIL import Image

img = Image.open('./../pytest/test.jpg')
img.show()
print((img.format, img.size, img.mode)) 
