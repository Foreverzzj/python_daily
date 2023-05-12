import  requests
from bs4 import BeautifulSoup
import lxml
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44'
}
url='https://www.gushicimingju.com/novel/sanguoyanyi/361.html'
resp = requests.get(url=url,headers=headers)
pag_text =resp.text
soup1 = BeautifulSoup(pag_text,'lxml')
cont = soup1.find('div',class_='main-content gushi-info')
r = cont.text
print(r)