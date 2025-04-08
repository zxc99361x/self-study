import requests
payload={'key1':'valeu1','key2':'valeu2'}
r=requests.get("http://httpbin.org/get",params=payload)
print(r.text)