import requests
import re

f = open('dy.csv', mode='w', encoding='utf-8')
fp = open('dl.csv', mode='w', encoding='utf-8')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
url = 'https://www.dy2018.com/'
resp = requests.get(url=url, headers=headers)
resp.encoding = 'gbk'
r = resp.text
obj = re.compile(r'2023必看热片.*?<li><a href=\'/(?P<url1>.*?)\' title', re.S)
obj1 = re.compile(r'<title>.*?(?P<name>\《.*?\》).*?</title>.*?<!--xunleiDownList Start-->.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<address>.*?)</a>',re.S)
result = obj.finditer(r)
for one in result:
    url1 = one.group('url1')
    f.write(f'{url1}\n')
    url2 = 'https://www.dy2018.com/' + url1
    print(url2)
    # resp2 = requests.get(url=url2, headers=headers)
    # resp2.encoding = 'gbk'
    # r1 = resp2.text
    # result2 = obj1.finditer(r1)
    # for two in result2:
    #     name = two.group('name')
    #     address = two.group('address')
    #     fp.write(f'{name}{address}\n')
# f.close()
# fp.close()
resp2 = requests.get(url=url2,headers=headers)
r2 = resp2.text
result2 = obj1.finditer(r2)
for two in result2:
    name =two.group('name')
    address = two.group('address')
    print(name,address)
# print(resp.text)
