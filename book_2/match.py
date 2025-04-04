import re
""" pat=re.compile(r'[a-z]+')
m=pat.match('tem12po')#開頭無法是數字
print(m)
 """
pat=re.compile(r'[a-z]+')
m=pat.search('3tem12po')#僅搜尋第一段出現的英文
print(m)
if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
