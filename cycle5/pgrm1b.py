#Write a Python program to read a file line by line and store it into a list.
print([line.strip() for line in open('pgrm file.txt','r')])