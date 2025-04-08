import tkinter as tk 
win=tk.Tk()

but1=tk.Button(win,text="按鈕一",width=20)
but1.pack(padx=20,pady=5,side="right")
but2=tk.Button(win,text="按鈕二",width=20)
but2.pack(padx=20,pady=5,side="left")
but3=tk.Button(win,text="按鈕三",width=20)
but3.pack(padx=20,pady=5,side="bottom")
but4=tk.Button(win,text="按鈕四",width=20)
but4.pack(padx=20,pady=5)
win.mainloop()