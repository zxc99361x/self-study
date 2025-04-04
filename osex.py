import os
filen=os.path.abspath("osex.py")
if os.path.exists(filen):
    print("完整路徑名稱: "+filen)
    print("檔案大小: ",os.path.getsize(filen))