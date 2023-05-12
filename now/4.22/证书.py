import requests
url='https://ssr2.scrape.center/'
resp = requests.get(url=url,verify=False)
print(resp.status_code)