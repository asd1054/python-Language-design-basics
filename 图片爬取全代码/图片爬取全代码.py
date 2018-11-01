import requests
import os
url = "http://5b0988e595225.cdn.sohucs.com/images/20180702/3e86a148fa684b4ca8ba94e0c9271d77.png"#图片网站地址
root = "D://pics//"
path = root + url.split('/')[-1]#"123.jpg"#
try:
    if not os.path.exists(root):
        os.makedirs(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")