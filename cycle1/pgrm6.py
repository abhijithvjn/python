n=int(input("Enter the number of names to be entered:"))
name=str(input("Enter the names:"))
count=0
for name in name:
    count=count+name.count('a')
print("Occurence of 'a' in the names is",count)