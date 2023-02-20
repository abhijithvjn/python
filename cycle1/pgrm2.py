#Display future leap years from current year to a final year entered by user
x=int(input("Enter the year:"))
for i in range(2022,x,1):
    if i%4==0 and i%100 != 0 or i%100==0 and i%4==0 and i%400==0:
        print("the leap years are",i)
if x<2022:
        print("error")    
    