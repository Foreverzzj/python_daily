import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
url = "https://www.gushicimingju.com/novel/jinpingmeichuanqi/"
resp = requests.get(url=url, headers=headers)
page_text = resp.text
soup = BeautifulSoup(page_text, "html.parser")
ul = soup.find_all(name='ul', attrs={'class': 'content-left left-2-col'})
fp=open('金梅瓶.text',mode='w',encoding='utf-8')
for li in ul:
    print(li)
    for a in li:
        print(a)
        # t =a.text
        t=a.get_text()
        url1 = 'https://www.gushicimingju.com'+a.a['href']
        resp2 = requests.get(url=url1,headers=headers)
        cont = resp2.text
        soup1 =BeautifulSoup(cont,'html.parser')
        jmp = soup1.find(name='div',attrs='main-content gushi-info')
        r = jmp.text
        fp.write(r)
print('over')
fp.close()
