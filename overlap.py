#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PIL import Image, ImageDraw, ImageFilter

count = sys.argv[1]
name = ''

# 事前にoverlap1.png、overlap2.png（任意の背景色で塗りつぶされた画像に、任意の画像サイズ）を用意する
if count == '1':
    name = '/path/to/overlap1.png'
    img1 = Image.open(name)
elif count == '2':
    name = '/path/to/overlap2.png'
    img1 = Image.open(name)
img2 = Image.open('image' + count + '.png').resize(img1.size)
mask = Image.new("L", img1.size, 128)
img = Image.composite(img1, img2, mask)
img.save(name)
