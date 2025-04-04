f=open('file.bin','rb')
print("目前檔案位置: ",f.tell())
f.seek(6)
str1=f.read(7)
print(str1)
print("目前文件索引位置: ",f.tell())

f.seek(0)
print("目前文件索引位置: ",f.tell())
str2=f.read(5)
print(str2)

f.seek(-8,2)
str3=f.read()
print(str3)

f.close()
