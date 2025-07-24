user_name="darshan"
user_pass="darshan06"

while True:
    username=str(input("Enter your username: "))
    password=str(input("Enter your password: "))
    if username==user_name:
        if password==user_pass:
            print("Login success")
            break
        else:
            print("Incorrect password")
    else:
        print("Username does not exist")
