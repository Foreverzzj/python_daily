import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
key=input('请输入')
parm = {
    'op':'keyword',
    'cname': '',
    'pid': '',
    'keyword':key,
    'pageIndex': '1',
    'pageSize': '10'
}
resp=requests.post(url=url,data=parm,headers=headers)
pag=resp.text
print(pag)
name=parm['keyword']+'.text'
with open(name,'w',encoding='utf-8') as fp:
    fp.write(pag)
