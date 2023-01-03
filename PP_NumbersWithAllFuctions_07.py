import math
class Number:
    def __init__(self,n):
        self.n=n
    def factorial(self):
        assert self.n>0,'The number should be >=0 to calculate Factorial'
        if self.n==0:
            return 1
        else:
            res=1
            for i in range(1,self.n+1):
                res*=i
            return res
    def checkEvenOdd(self):
        if self.n%2==0:
            return 'Even'
        else:
            return 'Odd'
    def sumOfDigits(self):
        num=0
        if self.n<0:
            num=abs(self.n)
        else:
            num=self.n
        temp=str(num)
        t=0
        for i in temp:
            t+=int(i)
        return t
    def checkArmstrong(self):
        assert self.n>=0,'The number should be positive'
        temp=str(self.n)
        t=0
        for i in temp:
            t+=int(i)**len(temp)
        if self.n==t:
            return 'Armstrong Number'
        else:
            return 'Not Armstrong Number'
    def checkPrime(self):
        assert self.n>0,'The number should be greater than 0'
        if self.n==1 or self.n==2 or self.n==3:
            return 'Prime'
        else:
            for i in range(2,int(math.sqrt(self.n))):
                if self.n%i==0:
                    return 'Not Prime'
            return 'Prime'
        

                           
inp=int(input())
ob=Number(inp)
try:
    print('Factorial of',inp,'is',ob.factorial())
except AssertionError as a:
    print(a)
print('\n'+str(inp),'is',ob.checkEvenOdd())    
print('\nSum of Digits of',inp,'is',ob.sumOfDigits())
try:
    print('\n'+str(inp),'is',ob.checkArmstrong())
except AssertionError as a:
    print('\n'+str(a))
try:
    print('\n'+str(inp),'is',ob.checkPrime())
except AssertionError as a:
    print('\n'+str(a))
    
                
    
