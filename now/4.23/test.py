import requests
import re

url = 'https://www.dy2018.com/i/107232.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
resp = requests.get(url=url, headers=headers)
resp.encoding = 'gbk'
res = resp.text
list_url1 = []
# print(res)
obj1 = re.compile(
    r'<title>.*?(?P<name>\《.*?\》).*?</title>.*?<!--xunleiDownList Start-->.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<address>.*?)</a>',
    re.S)
result = obj1.finditer(res)
for one in result:
    name = one.group('name')
    address = one.group('address')
    print(name)
    print(address)


