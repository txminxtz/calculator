import tkinter
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")

label_results= Label(root,width=25,height=2,text="",font=("arial",30))
label_results.pack()

Button(root,text="C", width=5, height=1, font=("arial",40,"bold"), bd=1,fg="#fff",bg="#3697f5").place(x=10,y=100)

https://www.youtube.com/watch?v=tdqUPsDbLLc

root.mainloop()