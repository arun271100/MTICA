def yield_demo(n):
    res=0
    for i in range(1,n+1):
        res+=i
        yield list(('i=',i,'res=',res))
    return res

inp=int(input())
ob=yield_demo(inp)
for i in range(inp):
    print(*next(ob))
