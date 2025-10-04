# gui_calculator.py
import tkinter as tk

def click(btn):
    if btn=="=":
        try: entry_var.set(str(eval(entry_var.get())))
        except: entry_var.set("Error")
    elif btn=="C": entry_var.set("")
    else: entry_var.set(entry_var.get()+btn)

root = tk.Tk()
root.title("Calculator")
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=16, font=("Arial",24))
entry.grid(row=0,column=0,columnspan=4)
buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"],
    ["C"]
]
for r,row in enumerate(buttons):
    for c,btn in enumerate(row):
        tk.Button(root,text=btn,width=5,height=2,font=("Arial",18),command=lambda b=btn: click(b)).grid(row=r+1,column=c)
root.mainloop()
