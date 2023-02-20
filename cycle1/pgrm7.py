n=int(input("Enter the number of elements :"))
l1=[]
for i in range (n):
    list=int(input("Enter the numbers :"))
    l1.append(list)
print(l1)
m=int(input("Enter the number of elements :"))
l2=[]
for j in range (m):
    newlist=int(input("Enter the numbers :"))
    l2.append(newlist)
print(l2)
#checking whether the two lists are of same size
if len(l1)==len(l2):
    print("The given lists are of same size")
else:
    print("The length of the two lists is not the same")
#checking whether the lists are of same sum
if sum(l1)==sum(l2):
    print("The lists have same sum value")
else:
    print("The sum of the lists not the same")
#checking whether the lists have common element
x=[i for i in l1 if i in l2]
if i>=0:
    print("The element in both the lists are:",x)
else:
    print("There is no common elements in the two lists")