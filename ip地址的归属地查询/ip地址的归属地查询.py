'''

http://site.ip138.com/输入你要查询的域名/domain.html #这个目录用于查询IP解析记录
htp://site.ip138.com/输入你要查询的域名/beian.html #这个用于查询子域名
http://site.ip138.com/输入你要查询的域名/whois.html #这个用于进行whois查询

'''
import requests
url = "http://ip138.com/ips138.asp?ip="
try:
    ip = input("请输入要查询的ip地址：")
    r = requests.get(url+ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")