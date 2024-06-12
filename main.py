import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("580x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    label_results.config(text=equation)

def clear():
    global equation
    equation = ""
    label_results.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_results.config(text=result)

label_results = tk.Label(root, width=25, height=2, text="", font=("arial", 30))
label_results.pack()

tk.Button(root, text="C", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5", command=clear).place(x=10, y=100)
tk.Button(root, text="/", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("/")).place(x=150, y=100)
tk.Button(root, text="%", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("%")).place(x=290, y=100)
tk.Button(root, text="*", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("*")).place(x=430, y=100)

tk.Button(root, text="7", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("7")).place(x=10, y=200)
tk.Button(root, text="8", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("8")).place(x=150, y=200)
tk.Button(root, text="9", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("9")).place(x=290, y=200)
tk.Button(root, text="-", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("-")).place(x=430, y=200)

tk.Button(root, text="4", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("4")).place(x=10, y=300)
tk.Button(root, text="5", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("5")).place(x=150, y=300)
tk.Button(root, text="6", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("6")).place(x=290, y=300)
tk.Button(root, text="+", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("+")).place(x=430, y=300)

tk.Button(root, text="1", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("1")).place(x=10, y=400)
tk.Button(root, text="2", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("2")).place(x=150, y=400)
tk.Button(root, text="3", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("3")).place(x=290, y=400)
tk.Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show("0")).place(x=10, y=500)

tk.Button(root, text=",", width=4, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2A2D36", command=lambda: show(",")).place(x=290, y=500)
tk.Button(root, text="=", width=4, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037", command=calculate).place(x=430, y=400)

root.mainloop()
