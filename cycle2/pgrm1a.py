#prgrm to find factorial of a number(recursive method)
def calc_factorial(x):
    if x==1:
        return 1
    else:
        return(x*calc_factorial(x-1))
x=int(input("Enter a No:"))
print("The factorial of",x,"is",calc_factorial(x))