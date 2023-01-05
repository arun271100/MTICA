class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,ob):
        return self.x+ob.x,self.y+ob.y
    def __sub__(self,ob1):
        return self.x-ob1.x,self.y-ob1.y
first=Vector2D(5,7)
second=Vector2D(5,6)
result=first+second
print(result)

result=first-second
print(result)
