import calculator as c
print(" 1.addition\n 2.subtract \n 3.multiply \n 4.division\n")
choice=int(input("Enter your choice:"))
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
if choice==1:
    print(num1,"+",num2,"=",c.add(num1,num2))
elif choice==2:
    print(num1,"-",num2,"=",c.subtract(num1,num2))
elif choice==3:
    print(num1,"*",num2,"=",c.multiply(num1,num2))
elif choice==4:
    print(num1,"/",num2,"=",c.divide(num1,num2))
else:
    print("wrong choice")