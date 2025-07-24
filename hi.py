from tkinter import *
from tkinter import messagebox
from tkinter import ttk
window=Tk()
window.title("New window")
window.geometry("600x600")


def clickme():
    data=combo_var.get()
    print(data)


value=[
    "option1",
    "option2",
    "option3",
]

combo_var=StringVar()
combo_var.set("None")
combo=ttk.Combobox(window,values=value,textvariable=combo_var).place(x=50,y=50)
btn=Button(window,text="click me",height=1,width=20,fg="red",bg="blue",command=clickme).place(x=150,y=150)

window.mainloop()