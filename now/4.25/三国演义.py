import  requests
from bs4 import BeautifulSoup
import lxml
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
url='https://www.gushicimingju.com/novel/sanguoyanyi/'
fp = open('三国演义.text',mode='w',encoding='utf-8')
resp = requests.get(url=url,headers=headers)
pag_text =resp.text
soup = BeautifulSoup(pag_text,'lxml')
list_url= soup.select('.main-content > ul > li ')
for one in list_url:
    t = one.text
    a='https://www.gushicimingju.com'+one.a['href']
    resp1 = requests.get(url=a, headers=headers).text
    soup1 = BeautifulSoup(resp1, 'lxml')
    # cont = soup1.select('.shici-content check-more')
    cont=soup1.find('div', class_='main-content gushi-info')
    tw = cont.text
    fp.write(tw)
print('over')
fp.close()

    # print(a,t)
