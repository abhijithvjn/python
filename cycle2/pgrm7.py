a=str(input("Enter a string:"))

s="ing"
for i in range(0,len(a)):
    if a[-1]=='g' and a[-2]=='n' and a[-3]=='i':
        print(a+"ly")
        break
    else:
        print(a+"ing")
        break