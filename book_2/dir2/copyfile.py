import os
""" file="myF.txt"
if os.path.exists(file):
    os.remove(file)
else:
    print(file+"檔案未建立") """

cur_p=os.getcwd()
os.system("cls")
os.system("mkdir dir2")
os.system("copy oss.py dir2\copyfile.py")
file=cur_p+"\dir2\copyfile.py"
os.system("notepad "+file)