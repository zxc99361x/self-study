import requests
url='https://api.ipify.org'
r=requests.get(url)
print('ip is :',r.text)