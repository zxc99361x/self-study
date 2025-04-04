import re
pat=re.compile(r'[a-z]+')
m=pat.findall('tem12po')#找出所有英文且將出現的組合整理成陣列
print(m)