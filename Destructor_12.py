class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")
        
