import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
url = "https://ssr1.scrape.center/static/img/logo.png"
r = requests.get(url=url, headers=headers,verify=False,timeout=1)
# pag=r.text
print(r.content)
# title = re.findall(pattern,pag)
# print(title)
# for one in pattern1.findall(pag):
with open('lgo2.ico','wb')as fp:
    fp.write(r.content)