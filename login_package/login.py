from module import credential

while True:
    username=str(input("Enter your username: "))
    password=str(input("Enter your password: "))
    if username==credential.user_name:
        if password==credential.user_password:
            print("Login success")
            break
        else:
            print("Incorrect password")
    else:
        print("Username does not exist")
        
