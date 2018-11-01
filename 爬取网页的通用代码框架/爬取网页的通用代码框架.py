import requests
#小规模 爬取网页 requests
#中规模 爬取网站 scrapy
#大规模 爬取全网 需要定制开发

#通用代码框架
def getHtmlText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()#如果状态码不是200，会引发HTTPerror异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == '__main__':
    url="http://www.baidu.com"
    a = getHtmlText(url)
    print(a)