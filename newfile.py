import os,shutil
cur_p=os.path.dirname(__file__)
destfile=cur_p+"\\"+"newfile.py"
shutil.copy("shutila.py",destfile)
shutil.copyfile("shutila.py","C:\\30\\new.py")
