import tkinter as tk 
win=tk.Tk()

win.geometry("300x100")
label1=tk.Label(win,text="輸入成績: ")
label1.place(x=20,y=20)
score=tk.StringVar()
entryUrl=tk.Entry(win,textvariable=score)
entryUrl.place(x=90,y=20)
btnD=tk.Button(win,text="成績計算")
btnD.place(x=80,y=50)
win.mainloop()