import requests
url='https://irs.thsrc.com.tw/IMINT'
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/ 89.0.4389.114 Safari/537.36'
}
r=requests.get(url,headers=headers,timeout=3)
print(r)