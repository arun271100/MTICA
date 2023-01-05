class Tiger:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def __str__(self):
        t='Name is : '+self.name+'\nColour is : '+self.colour
        return t
    def bark(self):
        print('roar...')
class Cat(Tiger):
    def bark(self):
        print('Meow...')

ob1=Tiger('Sher','Yellow')
ob2=Cat('Shepa','Black')
ob1.bark()
ob2.bark()
print(ob1)
