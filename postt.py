import requests
payload={'key1':'valeu1','key2':'valeu2'}
r=requests.post("http://httpbin.org/post",data=payload)
print(r.text)