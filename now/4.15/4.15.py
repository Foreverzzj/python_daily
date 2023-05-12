import requests
heads={'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'}
# url1="https://www.sogou.com"
url1="https://www.dy2018.com//"
resp=requests.get(url=url1,headers=heads)
resp.encoding='gbk'
ptext=resp.text
with open("sg.html", 'w', encoding='utf=8') as fp:
    fp.write(ptext)
    print('over')