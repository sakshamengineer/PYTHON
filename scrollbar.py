import tkinter as tk
from tkinter import ttk
a = tk.Tk()
a.geometry('500x700')
b = tk.Label(a,text="")
b.pack()
is_on = False
def button1():
    global is_on
    if is_on:
        b.config(text="is on")
        c.config(image=on)
        is_on = False
    else :
        b.config(text="is off")
        c.config(image=off)
        is_on = True
on = tk.PhotoImage(file="on.png")
off = tk.PhotoImage(file="off.png")
sty = ttk.Style()
sty.configure('Tbutton')
c = ttk.Button(a,image=on,command= button1)
c.pack(pady=1)
a.mainloop()