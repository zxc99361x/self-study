def click1():
    textvar.set("你已經按過了")

import tkinter as tk 
win=tk.Tk()
textvar=tk.StringVar()
but1=tk.Button(win,textvariable=textvar,command=click1)
textvar.set("按鈕")
but1.pack()
win.mainloop()
