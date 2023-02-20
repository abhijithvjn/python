#Python program to copy odd lines of one file to other
f1=open("pgrm file.txt",'r')
f2=open("pgr.txt",'w')
s=f1.readlines()
for x in range(1,len(s)):
    if(x%2!=0):
        l=f2.write(s[x])
f1.close()
f2=open("pgr.txt","r")
f3=f2.read()
print(f3)
f2.close()