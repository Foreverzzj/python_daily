import string

import requests
import re
f = open('ddl.csv', 'w', encoding='utf-8')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
url = 'https://www.dy2018.com/'
resp = requests.get(url=url, headers=headers)
resp.encoding = 'gbk'
r = resp.text
list_url = []
list_url1 = []
resp = requests.get(url=url,headers=headers)
obj = re.compile(r'(?P<url1>i\/\d+.html)', re.S)
obj1 = re.compile(r'<title>.*?(?P<name>\《.*?\》).*?</title>.*?<!--xunleiDownList Start-->.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<address>.*?)</a>',re.S)
for one in obj.findall(r):
    list_url.append(url+one)
# list_str=string.join(list_url)
# with open('url.text','w',encoding='utf-8') as fp:
#     fp.write(list_str)
# str2 = ''
print(list_url)
str2 = '\n'.join(list_url)
# print(str2,type(str2))
with open('url.text','w', encoding="utf-8") as fp:
       fp.write(str2)
fp.close()
for url1 in list_url:
    respo = requests.get(url=url1,headers=headers)
    respo.encoding='gbk'
    r1 = respo.text
    result = obj1.finditer(r1)
    for item in result:
        name = item.groups('name')
        address = item.groups('address')
        print(type(item.groups('address')))
        f.write(f'{name}{address}\n')
# f.close()
# url2 = list_url[1]
# print(url2)
# respo = requests.get(url=url2,headers=headers)
# respo.encoding='gbk'
# r1 = respo.text
# print(r1)
# result = obj1.finditer(r1)
# for item in result:
#     name = item.groups('name')
#     address = item.groups('address')
#     print(name)
#     print(address)
#     f.write(f'{name}{address}\n')
