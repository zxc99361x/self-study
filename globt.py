import os,glob
files= glob.glob("globt.py")+glob.glob("os*.py")+glob.glob("*.txt")
for file in files:
    print(file)