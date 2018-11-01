from PIL import Image
'''

    制作失败！！！！！！！

'''
ascii_char = list('"$%_&WM#*oahkbdqw,ZO0QLCJUYXzcvunxrjft/\|()?-/+@<>i;:,\^`.~')
def ger_char(r,b,g,alpha = 256 ):
    if alpha ==0:
        return ' '
    gray = int (0.2126*r + 0.7152*g+0.0722*b)
    unit = 256/len(ascii_char)
    return ascii_char[int(gray//unit)]
def main():
    im = Image.open('test.jpg')
    WIDTH,HEIGHT = 100,60 
    im = im.resize((WIDTH,HEIGHT))
    txt = ''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += ger_char(*im.getpixel((j,i)))
        txt += '\n'
    fo = open('pic_char.txt','w')
    fo.write(txt)
    fo.close()
    print("绘画成功")
main()