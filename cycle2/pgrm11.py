#Write lambda functions to find area of square, rectangle and triangle
#square
a=int(input("Enter side,a: "))
asq=lambda a: a*a
print("area= ",asq(a))
#rectangle
l=int(input("Enter the length of the rectangle: "))
b=int(input("Enter the breath of the rectangle: "))
ar=lambda l,b:l*b
print("area= ",ar(l,b))
#triangle
br=int(input("Enter the breath of the triangle: "))
h=int(input("Enter the height of the triangle: "))
atr=lambda br,h:0.5*br*h
print("area= ",atr(br,h))

