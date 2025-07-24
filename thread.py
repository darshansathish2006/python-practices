# import threading

# def print_cube(num):
#     print(f"The cube is {num*num*num}")

# def print_square(num):
#     print(f"Square of number is {num*num}")

# def print_num(num):
#     print(f"The original number is {num}")


# t1=threading.Thread(target=print_cube,args=(10,))
# t2=threading.Thread(target=print_square,args=(10,))
# t3=threading.Thread(target=print_num,args=(10,))

# t1.start()
# t2.start()
# t3.start()

# import threading 
# import time

# def print_numbers():
#     for i in range(5):
#         print(i)
#         time.sleep(1)

# def print_letters():
#     for ch in ['A','B','C','D','E']:
#         print(ch)
#         time.sleep(1)

# t1=threading.Thread(target=print_numbers)
# t2=threading.Thread(target=print_letters)

# t1.start()
# t2.start()

import threading
import time

def task(name,delay):
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} finished")

t1=threading.Thread(target=task,args=("Thread 1",2))
t2=threading.Thread(target=task,args=("Thread 2",3))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads are executed")