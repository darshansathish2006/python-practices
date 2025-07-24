l=[]
new_list=[]
for x in range(1,21):
    if x%2==0:
        l.append(x)

for x in range(len(l)):
    if x<len(l)-2:
        new_list.append(l[x]*l[x+2])

print(new_list)
