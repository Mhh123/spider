import pytesseract
from PIL import Image


def sb(image):
    #  打开图片
    img = Image.open(image)

    #  将图片转化为灰度图片
    img = img.convert('L')

    #  二值化处理
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = img.point(table, '1')

    img = img.convert('RGB')
    return pytesseract.image_to_string(img)
