#traffic signal
print("Enter signal status")
signal=int(input("1 for Green | 2 for Yellow | 3 for Red: "))
if signal==1:
    print("Signal is Green.Vehicle Go")
elif signal==2:
    print("Signal is Yellow.Vehicle slow down")
elif signal==3:
    print("Signal is Red.Vehicle Stop")
else:
    print("\nInvalid input")