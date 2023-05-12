import requests
import json

url = "https://movie.douban.com/j/chart/top_list"
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
parm = {
    'type': '11',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '40'
}
resp = requests.post(url=url, data=parm, headers=headers)
pag = resp.json()
print(pag)
name=parm['type']+'.json'
fp=open(name,'w',encoding='utf-8')
json.dump(pag,ensure_ascii=False,fp=fp)
