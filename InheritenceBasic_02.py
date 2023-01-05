class parent:
    age=55
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def ch1details(self):
        print('name  : '+self.name,'\nage :',self.age)
class child(parent):
    def ch2details(self):
        print('name  : '+self.name,'\nage :',self.age)
class Dog(parent):
    def bark(self):
        print('Boww')

if __name__=='__main__':
    ob1=child('arun',22)
    ob2=parent('vishnu',18)
    ob3=Dog('szfdswdef',456)
    ob1.ch2details()
    ob2.ch2details()
    ob3.bark()
    ob3.ch1details()
    print(ob1.name+ob2.name)
