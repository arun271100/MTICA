def Fact(n):
    ##assert(isinstance(n,int)),'Factorial is not defined for non integer values !'
    assert(type(n)==int),'Factorial is not defined for non integer values !'
    assert(n>=0),'Factorial of negative number is not defined !'
    if n==1 or n==0:
        return 1
    return n*Fact(n-1)
try:
    print(Fact(-545))
except Exception as obj:
    print(obj)

