import requests
url="http://www.ehappy.tw/demo.htm"#url="https://www.youtube.com/"
r=requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.text)