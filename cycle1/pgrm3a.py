#list comprehensions
#generate positive list of numbers from a given list of integers
l=[1,2,-3,-2,4,-6,-1,7,8,9]
print(l)
b=[x for x in l if x>=0]
print(b)