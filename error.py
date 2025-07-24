arr=[]

while True:
    for i in range(1,6):
        try:
            arr.append(int(input(f"Enter number {i} :")))
        except:
            if ValueError:
                print("Enter an integer!")
        finally:
            print("Element added")

    for i in range(len(arr)+1):
        try:
            print(arr[i])
        except:
            if IndexError:
                print("List index exceeded...")
        finally:
            print("Successfully printed!")

