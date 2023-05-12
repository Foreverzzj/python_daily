import requests
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzslist'
parm = {
    'on': 'true',
    'page': '1',
    'pageSize': '15',
    'xkType': '2',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
}
pag_id = requests.post(url=url, data=parm, headers=headers).json()
id_list = []
alldata = []
for dic in pag_id['list']:
    id_list.append(dic['id'])
    print(id_list)
post_url=''
for id in id_list:
    data={
        id:'id'
    }
    pag = requests.post(url=post_url,data=data,headers=headers).json()
    alldata.append(pag)
fp=open('alldata.json','w',encoding='utf-8')
json.dump(a)
