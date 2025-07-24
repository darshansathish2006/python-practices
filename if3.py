#evenodd
n=int(input("Enter a number till which you want to print even and odd numbers: "))
even=[]
odd=[]
for i in range(n+1):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Even numbers are:",end=" ")
for i in even:
    print(i,end=" ")

print("\nOdd numbers are:",end=" ")
for i in odd:
    print(i,end=" ")