with open('file2.txt','r',encoding='utf-8-sig') as f:
    doc=f.readlines()
    print(doc)
with open('file2.txt','r',encoding='utf-8-sig') as f:
    str1=f.read(5)
    print(str1)