l=[12,22,33,44,65]
print (l)

# loop to traverse each element in the l
# and, remove elements
# which are EVEN (divisible by 2)
for i  in l:
	if(i%2 == 0):
	    l.remove(i)

# print l after removing EVEN elements
print (l)