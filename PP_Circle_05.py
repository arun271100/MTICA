import math as m
class Circle:
    pi=m.pi
    def __init__(self,r):
        self.r=r
    def perimeter(self):
        return 2*self.pi*self.r
    def area(self):
        return self.pi*(self.r)**2
r=int(input('Enter the radius of circle : '))
ob=Circle(r)
print('Perimeter : ',ob.perimeter())
print('area : ',ob.area())
        
    
