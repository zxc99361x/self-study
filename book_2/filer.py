f=open("file1.txt",'rt',encoding="UTF-8")
for line in f:
    print(line,end="")
f.close