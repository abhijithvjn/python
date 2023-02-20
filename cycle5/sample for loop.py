fn=open("pgrm file.txt",'r')
s=fn.readlines()
for x in range(0,len(s)):
    print(s[x])
fn.close()