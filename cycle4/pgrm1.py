#co4pgrm1
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b  
    def perimeter(self):
        return 2*(self.l+self.b)
    def area(self):
        return self.l*self.b
    def compare(self,o):
        try:
            if obj1.area()==obj2.area():
                print("Both areas are equal")
            elif obj1.area()> obj2.area():
                print("Area of rectangle obj1 is greater:")
            else:
                print("Area of rectangle obj1 is lower:")
            if obj1.perimeter()==obj2.perimeter():
                print("Both areas are equal")
            elif obj1.perimeter()> obj2.perimeter():
                print("Perimeter of rectangle obj1 is greater:")
            else:
                print("Perimeter of rectangle obj1 is lower:")   
        except:
            print("Objects cannot be comparable")
        
   
l1=int(input("Enter the 1st length Rect1:"))
b1=int(input("Enter the 1st breadth Rect1:"))
l2=int(input("Enter the 2nd length Rect2:"))
b2=int(input("Enter the 2nd breadth Rect2:"))
obj1=rectangle(l1,b1)
obj2=rectangle(l2,b2)
print("Area of Rect1:%s"%(obj1.area()))
print("Perimeter of Rect1:%s"%(obj1.perimeter()))
print("Area of Rect2:%s"%(obj2.area()))
print("Perimeter of Rect2:%s"%(obj2.perimeter()))
obj1.compare(obj2)
    
