import requests
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
url = "http://www.baidu.com"
resp = requests.get(url=url,headers=headers)
print(resp.cookies)
for key ,value in resp.cookies.items():
    print(key+"="+value)