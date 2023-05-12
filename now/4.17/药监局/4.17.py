# list.appedd(x)在列表最后增加一个元素x
import requests
import json
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzslist'
id_list = []
alldat = []
for page in range(1,10):
    page=str(page)
    parm={
    'on': 'true',
    'page': page,
    'pageSize': '15',
    'xkType': '2',
    'productName': '',
    'conditionType': '1',
    'applyname': '',
    'applysn': ''
    }
    pag_list = requests.post(url=url, data=parm, headers=headers).json()
    for dic in pag_list['list']:
      id_list.append(dic['ID'])
      print(id_list)
post_url=''
for id in id_list:
    data={
        'id':id
    }
    pag = requests.post(url=post_url,data=data,headers=headers).json()
    alldat.append(pag)
fp=open('alldat.json','w',encoding='utf-8')
json.dump(alldat,fp=fp,ensure_ascii=False)