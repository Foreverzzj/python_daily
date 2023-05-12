import requests
heads={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
url1="https://www.sogou.com/web"
print('输入你的搜索词')
key=input()
parm={
    'query':key
}
resp=requests.get(url=url1,params=parm,headers=heads)
pag=resp.text
name=key+'.html'
with open(name,'w',encoding='utf-8') as fp:
    fp.write(pag)
    print('over')