try:
    n=int(input())
    #if n<=0:
     #   print("enter greater than zero")
        
    l=[]
    for i in range(n):
        l.append(int(input("Enter value: ")))
    avg=sum(l)/len(l)
    print(f"The average is: {avg:.2f}")
except:
    if n<=0:
        print("Enter greater than zero")
    elif ValueError:
        print("Enter a numerical value")
