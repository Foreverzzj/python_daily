import requests
import json
if __name__ == '__main__':
    url = "https://fanyi.baidu.com/sug"
heads={
		'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
	}
key=input('输入字符')
data1= dict(kw=key)
resp=requests.post(url=url,data=data1,headers=heads)
pag=resp.json()
print(pag)
name=key+'.json'
fp=open(name,'w',encoding='utf-8')
json.dump(pag,fp=fp,ensure_ascii=False)