class Number:
    '''
this Number class accepts two integers as input and generates outputs
according to the operation selected by the user.
'''
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def add(self):
        return self.n1+self.n2
    def sub(self):
        return self.n1-self.n2
    def mul(self):
        return self.n1*self.n2
    def div(self):
        return self.n1/self.n2
n1=int(input('n1 : '))
n2=int(input('n2 : '))
print('''Which operation do You want to perform :
      1.Addition
      2.Subtraction
      3.Multiplication
      4.Division''')
n3=int(input())
obj=Number(n1,n2)
if n3==1:
    print(n1,'+',n2,'=',obj.add(),sep='')
elif n3==2:
    print(n1,'-',n2,'=',obj.sub(),sep='')
elif n3==3:
    print(n1,'*',n2,'=',obj.mul(),sep='')
elif n3==4:
    try:
        print(n1,'/',n2,'=',obj.div(),sep='')
    except ZeroDivisionError as a:
        print(a)
else:
    print('INVALID SELECTION ')
