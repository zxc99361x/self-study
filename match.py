import re
""" pat=re.compile(r'[a-z]+')
m=pat.match('tem12po')
print(m)
 """
pat=re.compile(r'[a-z]+')
m=pat.search('3tem12po')
print(m)
if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())
