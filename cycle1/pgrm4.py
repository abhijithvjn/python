#count the occurences of each word in a line of text
linetext=str(input("enter the line"))
w={}
for i in linetext.split(" "):
    if i in w.keys():
        w[i]+=1
    else:
        w[i]=1
print(w)
