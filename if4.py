#evenodd in while
n=int(input("Enter a number till which you want to print even and odd numbers: "))
i=0
even=[]
odd=[]
while i<=n:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
    i+=1

i=0
print("Even numbers are:",end=" ")
while i<len(even):
    print(even[i],end=" ")
    i+=1
    
i=0
print("\nOdd numbers are:",end=" ")
while i<len(odd):
    print(odd[i],end=" ")
    i+=1