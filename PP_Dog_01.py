class Dog:
    price=900
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
    def __str__(self):
        return 'Im the d1 object'
        
    def details(self):
        print('Dog name is '+self.name+' and clour is '+
              self.colour+" with price of "+str(self.price))

if __name__=='__main__':
    d1=Dog('Naveen','white')
    d2=Dog('Gangully','Brown')
    print(d1.name)
    print(d1.colour)
    d1.details()
    d2.details()
    print(d1)

