import fitz   

fname = '1_1.pdf'
doc = fitz.open(fname)                      # open document

for page in doc:                            # iterate through the pages
    rotate = int(0)
    # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
    zoom_x = 2.0
    zoom_y = 2.0
    trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    pix = page.getPixmap(matrix = trans, alpha = False)     # render page to an image
    pix.writePNG("page-%i.png" % (page.number + 1))    # store image as a PNG