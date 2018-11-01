from PIL import Image
im = Image.open('py.gif')
try :
    im.save('picframe{:02d}.ong'.format(im.tell()))
    while 1:
        im.seek(im.tell()+1)
        im.save('picframe{:02d}.png'.format(im.tell()))
except:
    print("处理结束")

