a=input("Enter the string: ")
c=0
for i in a:
    if i==" ":
        continue
    else:
        c+=1
print(c,"Characters in "+a)