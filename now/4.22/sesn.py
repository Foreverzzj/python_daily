import requests
header={'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
url='https://www.httpbin.org/cookies/set/number/123456789'

s=requests.session()
s.get(url=url,headers=header)
r=s.get('https://www.httpbin.org/cookies',headers=header)
print(r.text)