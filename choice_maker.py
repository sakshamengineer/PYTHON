import random as r
import tkinter as tk
from tkinter import ttk
sc = tk.Tk()
sc.geometry('500x400')
lab = tk.Label(sc,text="")
lab.pack()
e1 = tk.Entry(sc)
e1.pack()
e2 = tk.Entry(sc)
e2.pack()
def fun1():
    
    if e1.get() == '' or e2.get() == '':
        lab.config(text="CANNOT BE BLANK")
    else:
        k = 0
        j = 0 
        for i in range(0,19):

            a = [r.randint(1,2),r.randint(1,2),r.randint(1,2),r.randint(1,2),r.randint(1,2),r.randint(1,2),r.randint(1,2),r.randint(1,2)]
            r.shuffle(a)
            b = r.choice(a)
            if b == 1:
                k+=1
            else:
                j+=1
        if k>j:
            lab.config(text=e1.get())
        else:
            lab.config(text=e2.get())
b1 = ttk.Button(sc,text="generate",command=fun1)
b1.pack()
sc.mainloop()