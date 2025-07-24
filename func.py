#basic function to add to two numbers

def add(num1,num2):
    return num1+num2

n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print(f"Sum of {n1} and {n2} is {add(n1,n2)}.")