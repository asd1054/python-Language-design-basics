
import requests
keyword = "Python"
baidu = "http://www.baidu.com/s"
so_360 = "http://www.so.com/s"
try:
    wd = {"wd":keyword}#百度的关键字
    q = {"q":keyword}#360的关键字
    r = requests.get(baidu,params=wd)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")