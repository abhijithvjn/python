#Write a Python program to read each row from a given csv file and print a list of strings. 
import csv
personz=[('Lata',22,45),('Anil',21,56),('John',20,60)]
csvfile=open('personz.csv','w',newline="")
obj=csv.writer(csvfile)
obj.writerows(personz)
csvfile.close()