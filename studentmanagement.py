import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

conn = mysql.connector.connect(
    host="localhost",
    user='root',
    password="Darshan@06",
    database="studentdb"
)

if conn.is_connected():
    print("Connection done")

mycursor = conn.cursor()

# Create table with auto-increment SNo
mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    SNo INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    `Roll-number` INT UNIQUE,
    Class VARCHAR(10),
    `Father's-phone` BIGINT,
    `Mother's-phone` BIGINT
)
""")

window = Tk()
window.title("Student Database")
window.geometry("700x700")

name = ""
rollno = ""
grade = ""
phone1 = ""
phone2 = ""

# Login page
welc_lab = Label(text="Welcome! Enter password to login.", font="ArielBlack")
login_box = Text(window, height=2, width=20)
login_btn = Button(window, height=2, width=10, text="Login")

# Main page buttons
add_btn = Button(window, height=2, width=20, text="Add student")
del_btn = Button(window, height=2, width=20, text="Delete student record")
updt_btn = Button(window, height=2, width=20, text="Update student record")
view_btn = Button(window, height=2, width=20, text="View student")
back_btn = Button(window, height=2, width=10, text="Back")

# Student form fields
combo_var = StringVar()
classes = ['LKG','UKG','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
name_lab = Label(text="Enter student name:", font=("Times New Roman", 20))
name_box = Text(window, height=2, width=20)
rollno_lab = Label(text="Enter student Roll-number:", font=("Times New Roman", 20))
rollno_box = Text(window, height=2, width=20)
class_lab = Label(text="Select Class:", font=("Times New Roman", 20))
class_box = ttk.Combobox(window, values=classes, textvariable=combo_var, width=5)
phone1_lab = Label(text="Enter Father's mobile number:", font=("Times New Roman", 20))
phone_box1 = Text(window, height=2, width=20)
phone2_lab = Label(text="Enter Mother's mobile number:", font=("Times New Roman", 20))
phone_box2 = Text(window, height=2, width=20)

details_lab = Label(text="")
submit_btn = Button(window, height=2, width=20, text="Submit")
enter_btn = Button(window, height=2, width=20, text="Enter")
delete__btn = Button(window, height=2, width=20, text="Delete record")
fetch_btn = Button(window, height=2, width=20, text="Fetch details")


def main():
    welc_lab.place(x=200, y=270)
    login_box.place(x=260, y=320)
    login_btn.place(x=300, y=370)
    add_btn.place_forget()
    del_btn.place_forget()
    updt_btn.place_forget()
    view_btn.place_forget()
    back_btn.place_forget()

main()

def login():
    if login_box.get("1.0", "end-1c") == "":
        welc_lab.place_forget()
        login_box.place_forget()
        login_btn.place_forget()
        name_box.place_forget()
        rollno_box.place_forget()
        class_box.place_forget()
        phone_box1.place_forget()
        phone_box2.place_forget()
        name_lab.place_forget()
        class_lab.place_forget()
        phone1_lab.place_forget()
        phone2_lab.place_forget()
        rollno_lab.place_forget()
        enter_btn.place_forget()
        delete__btn.place_forget()
        details_lab.place_forget()
        submit_btn.place_forget()

        add_btn.place(x=200, y=250)
        del_btn.place(x=400, y=250)
        updt_btn.place(x=200, y=350)
        view_btn.place(x=400, y=350)
        back_btn.place(x=100, y=600)
        back_btn.config(command=main)
    else:
        messagebox.showerror("Try again!", "Incorrect password. Try again!")

login_btn.config(command=login)

def add():
    add_btn.place_forget()
    del_btn.place_forget()
    updt_btn.place_forget()
    view_btn.place_forget()

    name_lab.place(x=50, y=120)
    name_box.place(x=300, y=120)
    rollno_lab.place(x=50, y=220)
    rollno_box.place(x=370, y=220)
    class_lab.place(x=50, y=320)
    class_box.place(x=200, y=330)
    phone1_lab.place(x=50, y=420)
    phone_box1.place(x=400, y=420)
    phone2_lab.place(x=50, y=520)
    phone_box2.place(x=400, y=520)

    back_btn.config(command=login)
    submit_btn.place(x=250, y=600)
    submit_btn.config(command=submit_add)

def submit_add():
    name = name_box.get("1.0", "end-1c")
    rollno = rollno_box.get("1.0", "end-1c")
    grade = class_box.get()
    phone1 = phone_box1.get("1.0", "end-1c")
    phone2 = phone_box2.get("1.0", "end-1c")

    try:
        query = "INSERT INTO students (Name, `Roll-number`, Class, `Father's-phone`, `Mother's-phone`) VALUES (%s, %s, %s, %s, %s)"
        values = (name, int(rollno), grade, int(phone1), int(phone2))
        mycursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Success", "Student added successfully.")
        name_box.delete("1.0","end")
        rollno_box.delete("1.0","end")
        class_box.set("")
        phone_box1.delete("1.0","end")
        phone_box2.delete("1.0","end")

        login()
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Roll number already exists!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def delete_initial():
    rollno_box.delete("1.0", "end")
    rollno_lab.config(text="Enter student roll-number to fetch details")
    rollno_lab.place(x=200, y=220)
    rollno_box.place(x=300, y=300)
    enter_btn.place(x=300, y=350)
    global sdata
    sdata = rollno_box.get("1.0", "end-1c")

    name_box.place_forget()
    class_box.place_forget()
    phone_box1.place_forget()
    phone_box2.place_forget()
    name_lab.place_forget()
    class_lab.place_forget()
    phone1_lab.place_forget()
    phone2_lab.place_forget()

    add_btn.place_forget()
    del_btn.place_forget()
    updt_btn.place_forget()
    view_btn.place_forget()
    back_btn.config(command=login)

def delete_fetch():
    rollno_box.place_forget()
    enter_btn.place_forget()
    rollno_lab.place_forget()
    roll = rollno_box.get("1.0", "end-1c").strip()
    try:
        mycursor.execute("SELECT Name FROM students WHERE `Roll-number` = %s", (roll,))
        result = mycursor.fetchone()
        if result:
            details_lab.place(x=50, y=300)
            details_lab.config(text=f"DO YOU WANT TO DELETE THE RECORD OF STUDENT:\nName: {result[0]}",font=("Times New Roman",15))
            delete__btn.place(x=500, y=600)
        else:
            messagebox.showerror("Error", "Roll number not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def delete_confirm():
    rollno_box.place_forget()
    enter_btn.place_forget()
    rollno_lab.place_forget()
    rollno = rollno_box.get("1.0", "end-1c").strip()
    try:
        query = "DELETE FROM students WHERE `Roll-number` = %s"
        values = (rollno,)
        mycursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Deleted", "Deletion successful!")
        rollno_box.delete("1.0","end")
        login()
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Roll number does not exist!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")
    
    back_btn.config(command=login)

def view():
    add_btn.place_forget()
    del_btn.place_forget()
    updt_btn.place_forget()
    view_btn.place_forget()
    
    rollno_box.place(x=250, y=250)
    fetch_btn.place(x=250, y=300)

def fetch():
    rollno_box.place_forget()
    fetch_btn.place_forget()
    roll = rollno_box.get("1.0", "end-1c").strip()
    try:
        mycursor.execute("SELECT * FROM students WHERE `Roll-number` = %s", (roll,))
        result = mycursor.fetchone()
        if result:
            name = result[0]
            rollno = result[1]
            grade = result[2]
            phone1 = result[3]
            phone2 = result[4]

            details_lab.config(text=f"STUDENT RECORD\n NAME: {name}\nROLL-NUMBER: {rollno}\nCLASS: {grade}\nFATHER'S PHONE: {phone1}\nMOTHER'S PHONE: {phone2}", font=("Times New Roman", 20))
            details_lab.place(x=30, y=200)
            back_btn.config(command=login)
        else:
            messagebox.showinfo("Not Found", "No student found with this roll number.")
            login()
    except Exception as e:
        messagebox.showerror("Error", str(e))

enter_btn.config(command=delete_fetch)
del_btn.config(command=delete_initial)
add_btn.config(command=add)
view_btn.config(command=view)
fetch_btn.config(command=fetch)
delete__btn.config(command=delete_confirm)




window.mainloop()
