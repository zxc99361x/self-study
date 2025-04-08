def clickme():
    global count
    count+=1
    labeltext.set("你按了"+str(count)+"次")
    if(btntext.get()=="請按下"):
        btntext.set("復原文字")
    else:
        btntext.set("請按下")

import tkinter as tk 
win=tk.Tk()
labeltext=tk.StringVar()
btntext=tk.StringVar()
count=0
label1=tk.Label(win,fg="red",textvariable=labeltext)
labeltext.set("歡迎光臨裡面請")
label1.pack()
button1=tk.Button(win,textvariable=btntext,command=clickme)
btntext.set("請按下")
button1.pack()
win.mainloop()