import tkinter as tk 
win=tk.Tk()


but1=tk.Button(win,text="按鈕一",width=20)
but1.grid(row=0,column=0,padx=20,pady=5)
but2=tk.Button(win,text="按鈕二",width=20)
but2.grid(row=0,column=1,padx=20,pady=5,columnspan=22,sticky="E")#與書上圖片所呈現不同 
but3=tk.Button(win,text="按鈕三",width=20)
but3.grid(row=0,column=23,padx=20,pady=5)
but4=tk.Button(win,text="按鈕四",width=20)
but4.grid(row=1,column=0,padx=20,pady=5)
but5=tk.Button(win,text="按鈕五",width=20)
but5.grid(row=1,column=1,padx=20,pady=5)
but6=tk.Button(win,text="按鈕六",width=20)
but6.grid(row=1,column=2,padx=20,pady=5)
win.mainloop()