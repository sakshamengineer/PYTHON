import tkinter as tk
from tkinter import ttk
from math import *

a = tk.Tk()
a.minsize(300,520)
a.title('Calculator')
var = tk.StringVar(a,"0")
ac=""
f0 = tk.Frame(a)
f0.place(relx=0.5,rely=0.5,anchor='center')
lb = tk.Listbox(f0,height=5,width=32,activestyle= 'none')
lb.grid(row=0,columnspan=6)
sc = ttk.Scrollbar(f0)
sc.grid(row=0,column=4,ipady=15)
lb.config(yscrollcommand = sc.set) 
sc.config(command = lb.yview) 

def press(num):
    global ac
    ac = ac + str(num)
    var.set(ac)

def clear():
    global ac
    ac = ""
    var.set(ac)
    sc.config(command=lb.delete(0,tk.END))

def equal_press():
    try:
        global ac
        total = str(eval(ac))
        var.set(total)
        ac = ""
        lb.insert(tk.END,total)
    except:
        var.set("error")
        ac = ""

def clear1():
    global ac 
    ac = ac[0:len(ac)-1]
    var.set(ac)

def btn(b,t,r,c):
    bn= ttk.Button(f0,text=b,command=lambda: press(t),padding=8,width=6).grid(column=c,row=r,padx=2,pady=0)

en = tk.Entry(f0,textvariable=var,width=20,justify="right",font=('arial',13),borderwidth=2).grid(row=1,columnspan=6,ipadx=30,pady=7)
cl = ttk.Button(f0,text='CA',command= clear,padding=8,width=6).grid(column=1,row=5,padx=2,pady=0)
equal= ttk.Button(f0,text="=",command=equal_press,padding=8,width=6).grid(row=6,columnspan=2,column=2,ipadx=20)
clear2 = ttk.Button(f0,text="⌫",command=clear1,padding=8,width=6).grid(row=8,column=2)

btn('π',pi,8,3)
btn('.','.',5,3)
btn(')',')',7,3)
btn('(','(',7,2)

btn(1,1,2,1)
btn(4,4,3,1)
btn(7,7,4,1)

btn(2,2,2,2)   
btn(5,5,3,2)
btn(8,8,4,2)
btn(0,0,5,2)

btn(3,3,2,3)   
btn(6,6,3,3)
btn(9,9,4,3)

btn('+','+',2,4)
btn('-','-',3,4)
btn('*','*',4,4)
btn('/','/',5,4)

btn('Sin','sin(',6,1)
btn('Cos','cos(',7,1)
btn('Tan','tan(',8,1)
btn('Cosec','1/sin(',6,4)
btn('Sec','1/cos(',7,4)
btn('Cot','1/tan(',8,4)

a.mainloop()