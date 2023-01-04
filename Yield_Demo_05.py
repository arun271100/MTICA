def yield_Demo(a,b):
    res=0
    if a>b:
        for i in range(b,a-1,-1):
            res+=i
            yield 'i=',i,'res=',res
        
    else:
        for i in range(a,b+1):
            res+=i
            yield 'i=',i,'res=',res
        
a=int(input())
b=int(input())
ob=yield_Demo(a,b)
if a>b:
    for i in range(a-b):
        print(next(ob))
else:
    for i in range(b-a+1):
        print(next(ob))
