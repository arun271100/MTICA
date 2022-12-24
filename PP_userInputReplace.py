def replaceDigits(n,i,j):
    n=n.replace(i,'_')
    n=n.replace(j,i)
    n=n.replace('_',j)
    return n
inp=input()
i=input()
j=input()
print(replaceDigits(inp,i,j))
