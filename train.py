from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Train Status")
window.geometry("600x600")

Index=0

trains = ["Chennai", "Mumbai", "Delhi", "Kolkata", "Hyderabad"]
train_no = [1001, 1002, 1003, 1004, 1005]
train_stat = ["Arrived", "Waiting", "Arrived", "Delayed", "Departed"]

check_btn = Button(window, height=2, width=20, text="Check all trains")

check2 = Button(window, height=2, width=20, text="Check for particular train")

train_box=Text(window,height=2,width=20)

enter_btn=Button(window,height=2,width=20,text="Fetch details")
back=Button(window,height=2,width=10,text="Back")


check_btn.place(x=130, y=250)
check2.place(x=320, y=250)

back_btn=Button(window,height=2,width=20,text="Back")



def trainlist():
    heading = Label(text="Train-ID----------Train To---------Train Status\n")
    heading.place(x=100, y=100)
    y = 130 
    for i in range(5):  
        status = Label(text=f"{train_no[i]}        \t{trains[i]}        \t{train_stat[i]}")
        status.place(x=100, y=y)
        y += 30  
    check_btn.place_forget()
    check2.place_forget()

def disp():
    global Index
    global lab1

   

    train = train_box.get("1.0", "end-1c")
    found = False


    for i in range(5):
        if train == str(train_no[i]) or train.lower() == trains[i].lower():
            Index = i
            found = True
            break

    if found:
        lab1.place_forget() 
        enter_btn.place_forget()
        train_box.place_forget()
        part_train = Label(text=f"Train-ID----Train To----Train Status\n{train_no[Index]}     {trains[Index]}       {train_stat[Index]}")
        part_train.place(x=200, y=250)

    else:
        messagebox.showinfo("Error", "Enter correct Train details")



def particular_train():
    check_btn.place_forget()
    check2.place_forget()
    
    global lab1
    lab1=Label(text="Enter Train-ID/Train Name")
    lab1.place(x=250,y=200)

    train_box.place(x=250,y=250)
    enter_btn.place(x=250,y=300)
    enter_btn.config(command=disp)


   
check_btn.config(command=trainlist)
check2.config(command=particular_train)
window.mainloop()
