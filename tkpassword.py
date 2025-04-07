def checkPW():
    if(pw.get()=="1234"):
        msg.set("密碼正確")
    else:
        msg.set("密碼錯誤")

import tkinter as tk 
win=tk.Tk()
pw=tk.StringVar()
msg=tk.StringVar()
label=tk.Label(win,text="請輸入密碼:")
label.pack()
entry=tk.Entry(win,textvariable=pw)
entry.pack()
but=tk.Button(win,text="登入",command=checkPW)
but.pack()
lbmsg=tk.Label(win,fg="red",textvariable=msg)
lbmsg.pack()
win.mainloop()