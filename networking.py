import socket
host="localhost"
port=1001
server=socket.socket()
server.bind((host,port))
server.listen()
con,add=server.accept()
print("Connection established from: "+str(add))
while True:
    data=con.recv(1024).decode()
    if not data:
        break
    data=str(data).upper()
    print(" from client: "+str(data))
    data=input("Type yoour message: ")
    con.send(data.encode())
con.close()