from PIL import Image
from PIL import ImageEnhance
im = Image.open("test.jpg")
om = ImageEnhance.Contrast(im)
om.enhance(20).save("new.jpg")
print("图像的对比度增强成功")