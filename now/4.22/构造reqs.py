from requests import Request, Session
url='https://httpbin.org/post'
data={
    'name' : 'germey'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
s = Session()
reqs = Request('POST',url,data=data,headers=headers)#构造Request对象
prepped = s.prepare_request(reqs)#调用Session类的prepare_request方法将 reqs 转化为一个 Prepared Request对象
r = s.send(prepped)#调用send 方法发送
print(r.text)
print(type(reqs))#<class 'requests.models.Request'>
print(type(prepped))#<class 'requests.models.PreparedRequest'>
print(type(r))#<class 'requests.models.Response'>