fn=open("fil.txt",'w')
fn.write("Python is a great language.\n Yeah its great!!\n");
fn.close()
fn=open("fil.txt",'r')
str=fn.read();
print(str)