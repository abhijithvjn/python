#prgrm to find factorial of a number
num=int(input("enter the number: "))
f=1
for i in range(1,num+1,1):
    f=f*i
print("the factorial is: ",f)