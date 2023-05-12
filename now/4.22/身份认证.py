import requests
# from  requests.auth import HTTPBasicAuth
url='https://ssr3.scrape.center'
# r = requests.get(url=url,verify=False,auth=HTTPBasicAuth('admin','admin'))
r=requests.get(url=url,verify=False,auth=('admin','admin'))
print(r.status_code)
print(type(r))
with open('ssr3.html','w',encoding='utf-8')as fp:
    fp.write(r.text)