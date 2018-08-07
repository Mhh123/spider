import pytesseract
from PIL import Image


#  打开图片
img = Image.open('MPYU.png')

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

print(pytesseract.image_to_string(img))
