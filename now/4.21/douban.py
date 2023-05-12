import requests
import re

f = open('top250.csv', mode='w', encoding='utf-8')
toplist = []
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
url = 'https://movie.douban.com/top250'
n =0
for i in range(10):

    parms = {
        'start': n,
        'filter': '',
    }
    n += 25
    dou = requests.get(url=url, headers=headers, params=parms)
    douban = dou.text
    with open('test.html','w',encoding='utf-8') as fp:
        fp.write(douban)
# re.S可以让正则表达式中的点匹配换行符
    obj = re.compile(
        r'<div class="hd">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?导演: (?P<daoyan>.*?)&nbsp.*?主演: (?P<actor>.*?)...<br>.*?(?P<year>\d*?)&nbsp;/&nbsp;(?P<country>.*?)&nbsp;/&nbsp;(?P<type>.*?)\n.*?inq">(?P<ping>.*?)</span>',
        re.S)
    with open('douban.html','w',encoding='utf-8')as fp:
	    fp.write(douban)
    result = obj.finditer(douban)
    for item in result:
    # print(item.group('name','daoyan','actor','year','country','type','ping'))
    # toplist.append(item.group('name','daoyan','actor','year','country','type','ping'))
     name = item.group('name')
     daoyan = item.group('daoyan')
     actor = item.group('actor').strip()  # 去除字符串两端的空白
     f.write(f'{name}{daoyan}{actor}\n')  # 可用python  csv模块写入
f.close()
dou.close()
print('over')
print(type(dou))
print(type(douban))
# 翻页提取
