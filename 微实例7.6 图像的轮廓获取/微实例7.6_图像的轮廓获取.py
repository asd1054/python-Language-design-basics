from PIL import Image
from PIL import ImageFilter
im = Image.open("test.jpg")
om = im.filter(ImageFilter.CONTOUR)
om.save("new.jpg")
print("轮廓获取成功")