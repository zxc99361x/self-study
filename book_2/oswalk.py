import os
cur_p=os.path.dirname(__file__)
sample_tree=os.walk(cur_p)
for dirname,subdir,files in sample_tree:
    print("檔案路徑: ",dirname)
    print("目錄串綠: ", subdir)
    print("檔案串列: ",files)
    print()