# /usr/bin/python3
# -*- coding: utf-8 -*-
"""
1、安装库  pip install pymupdf
2、直接运行
"""
import fitz
from os import path

workdir = r'd:\pdf2png'

pdf = '1.pdf'
pdf1 = '2.pdf'

fname = path.join(workdir, pdf)
doc = fitz.open(fname)                      # open document

for page in doc:                            # iterate through the pages
    rotate = int(0)
    # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
    zoom_x = 1.0
    zoom_y = 1.0
    trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    pix = page.getPixmap(matrix = trans, alpha = False)     # render page to an image
    pix.writePNG(path.join(workdir, "p-%i.png" % (page.number + 1)))    # store image as a PNG