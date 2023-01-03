import math as m
class Rectangle:
    pi=m.pi
    def __init__(self,l,w):
        assert l>0 and w>0,'The length or width should not be negative !'
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(l+w)
l=int(input('Enter length : '))
w=int(input('Enter width : '))
try:
    ob=Rectangle(l,w)
    print('Area of Rectangle : ',ob.area())
    print('Perimeter of Rectangle : ',ob.perimeter())
except AssertionError as a:
    print(a)

    

    
