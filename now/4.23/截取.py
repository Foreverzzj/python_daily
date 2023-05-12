import requests
import re
heads={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
# url1="https://www.sogou.com"
url1="https://www.dy2018.com//"
resp=requests.get(url=url1,headers=heads)
resp.encoding='gbk'
ptext=resp.text
obj = re.compile(r'2023必看热片.*?<ul>.*?</ul>',re.S)
r = obj.findall(ptext)
print(type(r[0]))
print(r[0])
obj1 = re.compile(r'(?P<url1>i\/\d+.html)', re.S)
result1 = obj1.finditer(r[0])
for two in result1:
    url2 = two.group('url1')
    print(type(url2))
# result =obj1.findall(r[0])
# for one in result:
#     print(type(one))