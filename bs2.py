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
<p id='p1'>段落一</p>
<p id='p2' class='red'>段落二</p>
</body>
</html>

'''
sp=BeautifulSoup(html,'html.parser')
print(sp.find('p'))
print(sp.find_all('p'))
print(sp.find('p',{'id':'p2','class':'red'}))
print(sp.find('p',id='p2',class_='red'))