from bs4 import BeautifulSoup
html='''
<htnl>
<head>
<meta charset='utf-8'>
<title>
網頁標題
</title>
</head>
<body>
<img src="http://www.ehappy.tw/python.png">
<a href="http://www.e-happy.com.tw">超連結</a>
</body>
</html>

'''
sp=BeautifulSoup(html,'html.parser')
print(sp.select('img')[0].get('src'))
print(sp.select('a')[0].get('href'))
print(sp.select('img')[0]['src'])
print(sp.select('a')[0]['href'])