# coding=utf-8
import urllib2
import json
from bs4 import BeautifulSoup

url_format = "http://www.autohome.com.cn/grade/carhtml/%s.html"
# 'accept-encoding': "gzip, deflate, sdch",  这里gzip可能会导致乱码
request_header = {
    'host': "www.autohome.com.cn",
    'connection': "keep-alive",
    'cache-control': "no-cache",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'accept-language': "zh-CN,zh;q=0.8",
    'cookie': "cookieCityId=110100; fvlid=1487217470601lg4EOUyi; sessionip=113.140.17.196; sessionid=9C9218BA-D2ED-4EAF-A2B5-E0A14340493B%7C%7C2017-02-16+11%3A57%3A52.684%7C%7Cwww.baidu.com; sessionuid=9C9218BA-D2ED-4EAF-A2B5-E0A14340493B||2017-02-16+11%3A57%3A52.684||www.baidu.com; ASP.NET_SessionId=ignag0wsafcqmdbmpcko0n1l; ahpvno=9; __utma=1.1557711971.1487217471.1487217471.1487228102.2; __utmb=1.0.10.1487228102; __utmc=1; __utmz=1.1487228102.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ref=www.baidu.com%7C0%7C0%7C0%7C2017-02-16+14%3A56%3A58.106%7C2017-02-16+11%3A57%3A52.684; sessionvid=B997F5EE-3F83-4C93-B3F7-A052F6761E15; area=610199; ahrlid=1487228213059NPxi1oKI-1487228218682",
    'if-modified-since': "Thu, 16 Feb 2017 06:30:22 GMT",
    'postman-token': "bccb3ca8-101b-38da-13e9-403910b57a4d"
}

html_doc = ''
start_char = 'A'

for i in range(ord('A'), ord('Z')):
    req = urllib2.Request(url_format % (chr(i)), headers=request_header)
    response = urllib2.urlopen(req)
    page = response.read()
    html_doc += page;
fo = open('test.html', 'wb+')
fo.write('<!DOCTYPE html>\
        <html>\
        <head>\
        <meta http-equiv=Content-Type content="text/html;charset=gb2312">\
        <meta http-equiv=X-UA-Compatible content="IE=edge,chrome=1">\
        <meta content=always name=referrer>\
        <script type="text/javascript" src="jquery-3.1.1.min.js"></script>\
        <script type="text/javascript" src="autohome.js"></script>\
        <title>Autohome</title>\
        </head>\
        <body>\
        ')
fo.write(html_doc);
fo.write('</body>')
fo.close()
#这里要重新换成只读模式打开
fo = open('test.html', 'r')
soup = BeautifulSoup(fo, "html.parser")

models_file = open("models.txt", "wb")
aaaaaa  = soup.find_all("h4")
for model in soup.find_all("h4"):
    try:
        if model.string is not None:
            models_file.write("%s\r\n" % (model.string.encode('utf-8')))
    except ValueError:
        continue

fo.close()
models_file.close()
