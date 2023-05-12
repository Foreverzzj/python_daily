import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
url='https://www.baidu.com'
r=requests.get(url=url,headers=headers)
pag=r.cookies
print(pag)
for key, value in pag.items():
    print(key + '='+ value)