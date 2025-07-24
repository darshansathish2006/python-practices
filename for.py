#nested if and for

n=int(input("Enter the number of employees you want to register:"))

for i in range(n+1):
    print(f"\nEnter details for employee {i+1}")

    name=str(input(f"\nEnter employee {i+1} name: "))
    dob=str(input("Enter date of birth(dd/mm/yyyy): "))
    Fathername=str(input("Enter Father's name: "))
    Mothername=str(input("Enter Mother's name: "))
    bloodgroup=str(input("Enter Bloodgroup: "))
    email=str(input("Enter email: "))
    phone=int(input("Enter phone number: "))
    tenth_marks=int(input("Enter marks obtained in SSLC out of 500: "))
    twelfth_marks=int(input("Enter marks obtained in HSC out of 600: "))
    tenth_percentage=(tenth_marks/500)*100
    twelfth_percentage=(twelfth_marks/600)*100
    monthly_salary=int(input("Enter monthly salary: "))
    q_salary=monthly_salary*3
    h_salary=monthly_salary*6
    a_salary=monthly_salary*12


    print("\n\n-----------------BIO DATA------------------")


    print(f"Employee {i+1} Name: {name}")
    print(f"Date of  birth: {dob}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Father's name: {Fathername}")
    print(f"Mother's name: {Mothername}")
    print(f"Blood group: {bloodgroup}")
    print(f"SSLC marks: {tenth_marks}")
    print(f"Percentage of marks obtained in SSLC: {tenth_percentage:.2f}%")
    print(f"HSC marks: {twelfth_marks}")
    print(f"Percentage of marks obtained in HSC: {twelfth_percentage:.2f}%")
    print(f"Monthly salary: {monthly_salary}")
    print(f"Quarter salary: {q_salary}")
    print(f"Half yearly salary: {h_salary}")
    print(f"Annual salary: {a_salary}")


    print(f"\nEmployee {i+1} has been registered.")

print("\nAll employees have been registered. Exiting...")