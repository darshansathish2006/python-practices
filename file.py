string=str(input())
f=open("file.txt","w")
f.write(string)
f.close()

f=open("file.txt","r")
var=f.read()

l=var.split()
print(len(l))