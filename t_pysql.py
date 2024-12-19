import tkinter as tk 
import mysql.connector as msc
from tkinter import ttk
con = msc.connect(host = 'localhost',user='root',password='4536',database='saksham')
cur = con.cursor()
s = tk.Tk()
#sc = ttk.Scrollbar(s,orient='vertical')
#sc.pack(side='right',fill='y')
dim = s.geometry('700x600')
ent = tk.Entry(s)
ent.pack()
listbox = tk.Listbox(s,activestyle='none')
def execute():
    a = ent.get()
    cur.execute(a)
    for i in cur:
        listbox.insert(tk.END,i)
    listbox.insert(tk.END,'\n')
    listbox.pack(fill='both')
but = ttk.Button(s,text='execute',command=execute)
but.pack()
s.mainloop()
con.commit()