import socket
host='localhost'
port=1001
obj=socket.socket()
obj.connect((host,port))
message=input("Type your message: ")
while message!='q':
    obj.send(message.encode())
    data=obj.recv(1024).decode()
    print("Receieved from server: "+data)
    message=input("Type your message: ")
obj.close()