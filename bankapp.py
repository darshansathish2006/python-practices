from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Bank Application")
window.geometry("600x600")

balance = 10000

withdraw_box = None
deposit_box = None

# Labels
id_label = Label(text="Enter user-id")
pass_label = Label(text="Enter password")

# Text Boxes
id_box = Text(window, height=2, width=20)
pass_box = Text(window, height=2, width=20)

# Buttons (pre-created)
check_btn = Button(window, height=2, width=20, text="Enter")
pass_check = Text(window, height=2, width=20)

# Sign-in Button
signint_btn = Button(window, height=2, width=20, text="Sign-in", command=lambda: take_input())

bal_amt = Label(text=f"Current balance: ₹{balance}\nEnter amount to withdraw")

def main():
    id_label.place(x=250, y=100)
    pass_label.place(x=250, y=200)
    id_box.place(x=250, y=150)
    pass_box.place(x=250, y=250)
    signint_btn.place(x=250, y=300)

main()

def check_pass():
    if pass_box.get("1.0", "end-1c") == "hello@123":
        return True

def check_bal():
    messagebox.showinfo("Balance", f"Your current balance is ₹{balance}")

def incorrect():
    messagebox.showwarning("Error", "Incorrect id/password")

def confirm_withdraw():
    global balance
    amt = withdraw_box.get("1.0", "end-1c")
    if amt.isdigit():
        balance = balance - int(amt)
        messagebox.showinfo("Success", f"₹{amt} withdrawn\nNew balance: ₹{balance}")
        withdraw_box.place_forget()
        confirm_btn.place_forget()
        bal_amt.config(text=f"Current balance: {balance}")
        bal_amt.place_forget()
        main()
    else:
        messagebox.showerror("Invalid", "Enter a valid number")

def verify_password():
    global lab1
    if pass_check.get("1.0", "end-1c") == "hello@123":
        pass_check.place_forget()
        check_btn.place_forget()
        lab1.place_forget()
        bal_amt.place(x=250, y=100)
        bal_amt.config(text=f"Current balance: ₹{balance}\nEnter amount to withdraw")

        global withdraw_box
        global confirm_btn

        withdraw_box = Text(window, height=2, width=20)
        withdraw_box.place(x=250, y=200)

        confirm_btn = Button(window, height=2, width=20, text="Confirm", command=confirm_withdraw)
        confirm_btn.place(x=250, y=270)
        pass_check.delete("1.0","end")
    else:
        incorrect()

def withdraw():
    withdraw_btn.place_forget()
    check_bal_btn.place_forget()
    deposit_btn.place_forget()

    global lab1
    global pass_check

    lab1 = Label(window, text="Enter your password")
    lab1.place(x=250, y=100)

    pass_check.place(x=250, y=150)

    check_btn.config(text="Enter", command=verify_password)
    check_btn.place(x=250, y=200)

def confirm_deposit():
    global balance
    amt2 = deposit_box.get("1.0", "end-1c")
    if amt2.isdigit():
        balance = balance + int(amt2)
        messagebox.showinfo("Success", f"₹{amt2} deposited\nNew balance: ₹{balance}")
        deposit_box.place_forget()
        confirm_btn2.place_forget()
        bal_amt.config(text=f"Current balance: {balance}")
        bal_amt.place_forget()
        main()
    else:
        messagebox.showerror("Invalid", "Enter a valid number")

def verify_password2():
    if pass_check.get("1.0", "end-1c") == "hello@123":
        pass_check.place_forget()
        check_btn.place_forget()
        lab2.place_forget()
        bal_amt.config(text=f"Current balance: ₹{balance}\nEnter amount to deposit")
        bal_amt.place(x=250, y=100)

        global deposit_box
        global confirm_btn2

        deposit_box = Text(window, height=2, width=20)
        deposit_box.place(x=250, y=200)

        confirm_btn2 = Button(window, height=2, width=20, text="Confirm", command=confirm_deposit)
        confirm_btn2.place(x=250, y=270)
        pass_check.delete("1.0","end")
    else:
        incorrect()

def deposit():
    deposit_btn.place_forget()
    withdraw_btn.place_forget()
    check_bal_btn.place_forget()
    global lab2
    lab2 = Label(window, text="Enter your password")
    lab2.place(x=250, y=100)
    pass_check.place(x=250, y=150)
    check_btn.place(x=250, y=200)
    check_btn.config(text="Enter", command=verify_password2)

def take_input():
    if id_box.get("1.0", "end-1c") == "1234" and check_pass():
        id_box.place_forget()
        pass_label.place_forget()
        id_label.place_forget()
        signint_btn.place_forget()
        pass_box.place_forget()
        id_box.delete("1.0", "end")
        pass_box.delete("1.0", "end")

        withdraw_btn.place(x=250, y=250)
        check_bal_btn.place(x=250, y=300)
        deposit_btn.place(x=250, y=350)
    else:
        incorrect()

withdraw_btn2 = Button(window, height=2, width=20, text="Withdraw amount", command=withdraw)
withdraw_btn = Button(window, height=2, width=20, text="Withdraw", command=withdraw)
check_bal_btn = Button(window, height=2, width=20, text="Check balance", command=check_bal)
deposit_btn = Button(window, height=2, width=20, text="Deposit", command=deposit)

window.mainloop()
