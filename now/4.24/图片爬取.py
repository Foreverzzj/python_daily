import  requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
url='https://n.sinaimg.cn/tech/transform/330/w144h186/20220428/24d5-c55b0fa6d2b78f5c95a70dd4bc4abf64.gif'
resp = requests.get(url=url,headers=headers)
print(resp.content)
fp=open('o1.gif','wb')
fp.write(resp.content)
# with open('01.gif','wb') as fp:
#     fp.write(resp.content)
#     fp.close()
print('over')