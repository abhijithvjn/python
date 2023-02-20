#Write a Python program to read a file line by line and store it into a list.
fn=open("pgrm file.txt",'r')
print(fn)
lines=fn.readlines()
l1=[line.strip() for line in lines]
print(l1)
