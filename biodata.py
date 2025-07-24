name=str(input("Enter your name: "))
dob=str(input("\nEnter your date of birth(dd/mm/yyyy): "))
Fathername=str(input("\nEnter Father's name: "))
Mothername=str(input("\nEnter Mother's name: "))
bloodgroup=str(input("\nEnter your Bloodgroup: "))
email=str(input("\nEnter your email: "))
phone=int(input("\nEnter your phone number: "))
tenth_marks=int(input("\nEnter marks obtained in SSLC out of 500: "))
twelfth_marks=int(input("\nEnter marks obtained in HSC out of 600: "))
tenth_percentage=(tenth_marks/500)*100
twelfth_percentage=(twelfth_marks/600)*100


print("\n\n-----------------BIO DATA------------------")


print(f"\nYour Name: {name}")
print(f"\nDate of  birth: {dob}")
print(f"\nEmail: {email}")
print(f"\nPhone: {phone}")
print(f"\nFather's name: {Fathername}")
print(f"\nMother's name: {Mothername}")
print(f"\nBlood group: {bloodgroup}")
print(f"\nSSLC marks: {tenth_marks}")
print(f"\nPercentage of marks obtained in SSLC: {tenth_percentage:.2f}%")
print(f"\nHSC marks: {twelfth_marks}")
print(f"\nPercentage of marks obtained in HSC: {twelfth_percentage:.2f}%")