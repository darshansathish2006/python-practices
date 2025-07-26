import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk


conn = mysql.connector.connect(
    host="localhost",
    user='root',
    password="Darshan@06",
    database="studentdb"
)

if conn.is_connected():
    print("Connection done")

mycursor = conn.cursor()

#table creation
mycursor.execute("""
CREATE TABLE IF NOT EXISTS students (
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


#background image
original_bg = Image.open("bg.png")
resized_bg = original_bg.resize((700, 700))  # Match window size
bg_img = ImageTk.PhotoImage(resized_bg)
bg_label = Label(window, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


#variables to hold student details
name = ""
rollno = ""
grade = ""
phone1 = ""
phone2 = ""

# Login page 
welc_lab = Label(text="STUDENT DATABASE MANAGEMENT SYSTEM\nWELCOME! ENTER ADMIN PASSWORD", font=("Bodoni MT Condensed",25),bg="white",fg="black")
login_box = Text(window, height=2, width=20)
login_btn = Button(window, height=1, width=8, text="Login",font=("Bookman Old Style",13),bg="#FFF8D1")


# Main page buttons
add_btn = Button(window, height=2, width=20, text="Add student record",bg="#FF6C0A",font=("Arial Black",10))
del_btn = Button(window, height=2, width=20, text="Delete student record",bg="#EBFF0D",font=("Arial Black",10))
view_all_btn = Button(window, height=2, width=20, text="View students",bg="#9E9EFF",font=("Arial Black",10))
view_btn = Button(window, height=2, width=20, text="Update & view",bg="#52FF74",font=("Arial Black",10))
back_btn = Button(window, height=2, width=10, text="Back",font=("Times New Roman",10),bg="#FE52CD")

# Student form fields
combo_var = StringVar()
classes = ['LKG','UKG','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII']
name_lab = Label(text="Enter student name:", font=("Times New Roman", 20),bg="#46EBB7")
name_box = Text(window, height=2, width=20)
rollno_lab = Label(text="Enter student Roll-number:", font=("Times New Roman", 20),bg="#46EBB7")
rollno_box = Text(window, height=2, width=20)
class_lab = Label(text="Select Class:", font=("Times New Roman", 20),bg="#46EBB7")
class_box = ttk.Combobox(window, values=classes, textvariable=combo_var, width=5)
phone1_lab = Label(text="Enter Father's mobile number:", font=("Times New Roman", 20),bg="#46EBB7")
phone_box1 = Text(window, height=2, width=20)
phone2_lab = Label(text="Enter Mother's mobile number:", font=("Times New Roman", 20),bg="#46EBB7")
phone_box2 = Text(window, height=2, width=20)
submit_btn = Button(window, height=2, width=10, text="SUBMIT",font=("Cooper Black",15),bg="grey",fg="white")

#contents in delete page,update and view page
details_lab = Label(text="")
enter_btn = Button(window, height=2, width=7, text="Enter",font=("Cooper Black",12),bg="grey",fg="white")
delete__btn = Button(window, height=2, width=15, text="Delete record",bg="red",font=("Cooper Black",12))
fetch_btn = Button(window, height=2, width=10, text="Fetch details",bg="grey",fg="white",font=("Cooper Black",12))
rollno_fetch=Label(text="Enter student roll-number to fetch details",font=("Times New Roman",20),bg="#FFF8D1")
rollno_fetch_box=Text(window,height=2,width=20)


updt_class=Button(window,height=2,width=20,text="Update Class",bg="#E695FF")
updt_phone1=Button(window,height=2,width=20,text="Update Father's phone",bg="#E695FF")
updt_phone2=Button(window,height=2,width=20,text="Update Mother's phone",bg="#E695FF")

num_lab=Label(text="Enter new number",font=("Times New Roman",20),bg="#FFF8D1")
confirm_updt_btn=Button(window,height=2,width=15,text="Confirm update",font=("Cooper Black",12),bg="grey",fg="white")

view_all_stud_btn=Button(window,height=2,width=20,text="View all students",bg="#FFFA29",font=("Arial Black",10))
view_spec_std=Button(window,height=2,width=20,text="View class",bg="#FFFA29",font=("Arial Black",10))

info_lab = Label(text=f"{'Name':<20}{'Roll No.':<12}{'Class':<8}{'Father Phone':<15}{'Mother Phone':<15}",
                         font= ("Courier", 12, "bold"))
student_row=Label(text="")



def main():
    login_box.delete("1.0","end")
    welc_lab.place(x=170, y=220)
    login_box.place(x=280, y=320)
    login_btn.place(x=312, y=370)
    add_btn.place_forget()
    del_btn.place_forget()
    view_all_btn.place_forget()
    view_btn.place_forget()
    back_btn.place_forget()

main()

def login():
    back_btn.config(text="Log-out")

    for label in student_labels:
        label.place_forget()
    student_labels.clear()

    if login_box.get("1.0", "end-1c") == "admin@123":
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
        fetch_btn.place_forget()
        updt_class.place_forget()
        updt_phone1.place_forget()
        updt_phone2.place_forget()
        confirm_updt_btn.place_forget()
        rollno_fetch_box.place_forget()
        rollno_fetch.place_forget()
        info_lab.place_forget()
        student_row.place_forget()
        view_all_btn.place_forget()
        view_all_stud_btn.place_forget()
        view_spec_std.place_forget()
        num_lab.place_forget()

        add_btn.place(x=200, y=250)
        del_btn.place(x=400, y=250)
        view_all_btn.place(x=200, y=350)
        view_btn.place(x=400, y=350)
        back_btn.place(x=10, y=20)
        back_btn.config(command=main)
    else:
        messagebox.showerror("Try again!", "Incorrect password. Try again!")

login_btn.config(command=login)


def add():
    back_btn.config(text="Back")

    add_btn.place_forget()
    del_btn.place_forget()
    view_all_btn.place_forget()
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
    submit_btn.place(x=270, y=600)
    submit_btn.config(command=submit_add)


def submit_add():
    name = name_box.get("1.0", "end-1c")
    rollno = rollno_box.get("1.0", "end-1c")
    grade = class_box.get()
    phone1 = phone_box1.get("1.0", "end-1c")
    phone2 = phone_box2.get("1.0", "end-1c")

    if name=="":
        messagebox.showerror("Invalid credentials","Enter valid name")
    elif rollno=="" or not rollno.isnumeric():
        messagebox.showerror("Invalid credentials","Enter valid Roll-number")
    elif grade=="":
        messagebox.showerror("Invalid credentials","Enter valid class")
    elif phone1=="" or len(phone1)!=10:
        messagebox.showerror("Invalid credentials","Father's phone number invalid")
    elif phone2=="" or len(phone2)!=10:
        messagebox.showerror("Invalid credentials","Mother's phone number invalid")
    elif phone1==phone2:
        messagebox.showerror("Father and mother phone number cannot be same")
    else:
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
    back_btn.config(text="Back")

    rollno_fetch.place_configure(x=150, y=240)
    rollno_fetch_box.place_configure(x=300, y=300)
    enter_btn.place(x=340, y=350)
    global sdata
    sdata = rollno_fetch_box.get("1.0", "end-1c")

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
    view_all_btn.place_forget()
    view_btn.place_forget()
    back_btn.config(command=login)

def delete_fetch():
    global roll
    roll = rollno_fetch_box.get("1.0", "end-1c").strip()
    try:
        mycursor.execute("SELECT Name FROM students WHERE `Roll-number` = %s", (roll,))
        result = mycursor.fetchone()
        if result:
            details_lab.place(x=100, y=300)
            details_lab.config(text=f"DO YOU WANT TO DELETE THE RECORD OF STUDENT:\nName: {result[0]}",font=("Times New Roman",15),bg="#FFFBE8")
            delete__btn.place(x=500, y=600)
            rollno_box.place_forget()
            enter_btn.place_forget()
            rollno_lab.place_forget()
            rollno_fetch.place_forget()
            rollno_fetch_box.place_forget()

        else:
            messagebox.showerror("Error", "Roll number not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def delete_confirm():

    
    try:
        query = "DELETE FROM students WHERE `Roll-number` = %s"
        values = (roll,)
        mycursor.execute(query, values)
        conn.commit()
        messagebox.showinfo("Deleted", "Deletion successful!")
        rollno_fetch_box.delete("1.0","end")
       
        login()
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Roll number does not exist!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")
    
    back_btn.config(command=login)

def view():
    back_btn.config(text="Back")
  
    add_btn.place_forget()
    del_btn.place_forget()
    view_all_btn.place_forget()
    view_btn.place_forget()

    rollno_fetch.place_configure(x=150,y=240)

    rollno_fetch_box.place_configure(x=300, y=300)
    fetch_btn.place(x=320, y=350)
    back_btn.config(command=login)
    fetch_btn.config(command=fetch)


def fetch():
    
    global roll
    roll = rollno_fetch_box.get("1.0", "end-1c").strip()

    try:
        mycursor.execute("SELECT * FROM students WHERE `Roll-number` = %s", (roll,))
        result = mycursor.fetchone()
        if result:
            rollno_fetch_box.place_forget()
            fetch_btn.place_forget()
            rollno_fetch.place_forget()
            name = result[0]
            rollno = result[1]
            grade = result[2]
            phone1 = result[3]
            phone2 = result[4]

            details_lab.config(text=f"STUDENT RECORD\n--------------\nNAME: {name}\n\nROLL-NUMBER: {rollno}\n\nCLASS: {grade}\n\nFATHER'S PHONE: {phone1}\n\nMOTHER'S PHONE: {phone2}", font=("Bahnschrift SemiBold", 20),bg="white")
            details_lab.place_configure(x=200, y=180)
            back_btn.config(command=login)
            updt_class.place(x=50,y=600)
            updt_phone1.place(x=250,y=600)
            updt_phone2.place(x=450,y=600)
            rollno_fetch_box.delete("1.0","end")
            updt_class.config(command=update_class)
        else:
            messagebox.showinfo("Not Found", "No student found with this roll number.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_class():
    details_lab.place_forget()
    updt_class.place_forget()
    updt_phone1.place_forget()
    updt_phone2.place_forget()

    num_lab.config(text="Select class to update")
    num_lab.place(x=200,y=240)
    class_box.place(x=250,y=300)
    confirm_updt_btn.place_configure(x=250,y=350)
    confirm_updt_btn.config(command=updt_class_confirm)

def updt_class_confirm():
    global cl 
    cl=class_box.get()
    try:
        if class_box.get()!="":
            mycursor.execute("UPDATE students SET `Class`=%s WHERE `Roll-number`=%s",(cl,roll))
            conn.commit()
            messagebox.showinfo("Update info","Class updated successfully")    
            class_box.set("")
            class_box.place_forget()
            login()
        else:
            messagebox.showerror("Invalid input","Select a class")
    except Exception as e:
        messagebox.showerror("Error", f"Update failed:\n{e}")


def update_father():
    details_lab.place_forget()
    updt_class.place_forget()
    updt_phone1.place_forget()
    updt_phone2.place_forget()

    phone_box1.place_configure(x=270,y=300)
    num_lab.config(text="Enter new number")
    num_lab.place(x=250,y=240)
    confirm_updt_btn.place_configure(x=270,y=350)
    confirm_updt_btn.config(command=update_father_confirm)


def update_father_confirm():
    global ph1 
    ph1=phone_box1.get("1.0","end-1c")
    try:
        if ph1!="" and len(ph1)==10:
            mycursor.execute("UPDATE students SET `Father's-phone`=%s WHERE `Roll-number`=%s",(ph1,roll))
            conn.commit()
            messagebox.showinfo("Update info","Father's phone number updated successfully")
            phone_box1.place_forget()
            phone_box1.delete("1.0","end")
            login()
        else:
            messagebox.showerror("Invalid input","Enter valid phone number")
    except Exception as e:
        messagebox.showerror("Error", f"Update failed:\n{e}")


def update_mother():
    details_lab.place_forget()
    updt_class.place_forget()
    updt_phone1.place_forget()
    updt_phone2.place_forget()

    phone_box2.place_configure(x=270,y=300)
    num_lab.config(text="Enter new number")
    num_lab.place(x=250,y=240)
    confirm_updt_btn.place_configure(x=270,y=350)
    confirm_updt_btn.config(command=update_mother_confirm)


def update_mother_confirm():
    global ph2 
    ph2=phone_box2.get("1.0","end-1c")
    try:
        if ph2!="" and len(ph2)==10:
            mycursor.execute("UPDATE students SET `Mother's-phone`=%s WHERE `Roll-number`=%s",(ph2,roll))
            conn.commit()
            messagebox.showinfo("Update info","Mother's phone number updated successfully")
            phone_box2.place_forget()
            phone_box2.delete("1.0","end")
            login()
        else:
            messagebox.showerror("Invalid input","Enter valid phone number")
    except Exception as e:
        messagebox.showerror("Error", f"Update failed:\n{e}")




def viewpage1():
    back_btn.config(text="Back")

    add_btn.place_forget()
    del_btn.place_forget()
    view_all_btn.place_forget()
    view_btn.place_forget()

    view_all_stud_btn.place(x=100,y=250)
    view_spec_std.place(x=400,y=250)
    back_btn.config(command=login)

student_labels = []  # global list at the top

def viewall():
    global student_labels
    for label in student_labels:
        label.destroy()
    student_labels.clear()

    view_all_stud_btn.place_forget()
    view_spec_std.place_forget()

    try:
        mycursor.execute("SELECT * FROM students")
        result = mycursor.fetchall()

        y = 100
        info_lab.place(x=10, y=y)
        y += 30

        for x in result:
            student_row = Label(
                window,
                text=f"{x[0]:<20}{x[1]:<12}{x[2]:<8}{x[3]:<15}{x[4]:<15}",
                font=("Courier", 12),
                anchor='w',bg="white"
            )
            student_row.place(x=10, y=y)
            student_labels.append(student_row) 
            y += 25

    except Exception as e:
        messagebox.showerror("Error", str(e))

def view_part():
    view_all_stud_btn.place_forget()
    view_spec_std.place_forget()
    
    num_lab.config(text="Select class")
    num_lab.place(x=250,y=300)
    class_box.place(x=250,y=350)
    fetch_btn.place(x=250,y=400)

    fetch_btn.config(command=view_spec)

def view_spec():
    global student_labels
    for label in student_labels:
        label.destroy()
    student_labels.clear()
    cl=class_box.get()
    view_all_stud_btn.place_forget()
    view_spec_std.place_forget()
    try:
        if cl!="":
            num_lab.place_forget()
            class_box.place_forget()
            fetch_btn.place_forget()
            mycursor.execute("SELECT * FROM students WHERE `Class`=%s ORDER BY `Name`",(cl,))
            result = mycursor.fetchall()

            y = 100
            info_lab.place(x=10, y=y)
            y += 30

            for x in result:
                student_row = Label(
                    window,
                    text=f"{x[0]:<20}{x[1]:<12}{x[2]:<8}{x[3]:<15}{x[4]:<15}",
                    font=("Courier", 12),
                    anchor='w',
                    bg="white"
                )
                student_row.place(x=10, y=y)
                student_labels.append(student_row) 
                y += 25
            class_box.set("")
        else:
            messagebox.showerror("Invalid","Enter valid class")

    except Exception as e:
        messagebox.showerror("Error", str(e))



enter_btn.config(command=delete_fetch)
del_btn.config(command=delete_initial)
add_btn.config(command=add)
view_btn.config(command=view)
delete__btn.config(command=delete_confirm)
view_all_btn.config(command=viewpage1)
updt_phone1.config(command=update_father)
updt_phone2.config(command=update_mother)
view_all_stud_btn.config(command=viewall)
view_spec_std.config(command=view_part)


window.mainloop()

