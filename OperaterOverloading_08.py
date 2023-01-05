class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,ob):
        return self.real+ob.real,self.imag+ob.imag
    def __sub__(self,ob1):
        return self.real-ob1.real,self.imag-ob1.imag
    def __mul__(self,ob2):
        return (self.real*ob2.real-self.imag+ob2.imag,
                self.real*ob2.imag+self.imag*ob2.real)
    def __str__(self):
        return (self.real,self.imag)
n1=Complex(2,6)
n2=Complex(7,8)
n3=n1+n2
n4=n1-n2
n5=n1*n2
print(n3)
print(n4)
print(n5)
