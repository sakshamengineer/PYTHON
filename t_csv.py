import csv 
import tkinter as t 
from tkinter import ttk
s = t.Tk()
f = open('new.csv','a+',newline='\n')
a = csv.writer(f)
s.geometry('600x700')
d = t.Entry(s)
d.pack()
b = t.Entry(s)
b.pack()
c = t.Entry(s)
c.pack()
def func():
    df= d.get()
    bf= b.get()
    cf= c.get()
    e=[df,bf,cf]
    la = t.Label(s,text=e)
    la.pack()
    a.writerow(e)
bu = ttk.Button(s,text= 'run', command=func) 
bu.pack()
f1 = open('new.csv','r+')
re = csv.reader(f1)
for i in re:
    la = t.Label(s,text=i)
    la.pack()
s.mainloop()
f1.close()
f.close()