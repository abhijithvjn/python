#Create a class #Rectangle with private attributes length and width. Overload ‘<’  operator to compare the area of 2 rectangles.
class rectangle:
    def __init__(self):
        self.__length=int(input("Enter the length of the rectangle:"))
        self.__breadth=int(input("Enter the breadth of the rectangle:"))
 
    def __lt__(self,ob2):
        area1=self.__length*self.__breadth
        area2=ob2.__length*ob2.__breadth
        print("Area of rectangle is ",area1)
        print("Area of rectangle is ",area2)
        return area1<area2
print("Enter the length and breadth of first object:")
obj1 = rectangle()
print("Enter the length and breadth of second object:")
obj2 = rectangle()
if obj1<obj2:
    print("obj1 is less than obj2")
else:
    print("obj1 is greater than obj2")

