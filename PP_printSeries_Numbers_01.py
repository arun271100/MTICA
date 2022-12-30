def printSeries_Numbers(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()
    print('__'*10)
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=' ')
        print()
    print('__'*10)
    num=1
    for i in range(1,n+1):
        for j in range(i):
            print(num,end=' ')  
            num+=1
        print()
    print('__'*10)
    for i in range(0,n):
        print(' '*(n-i-1)+'*'*(i*2+1)+' '*(n-i-1))
n=int(input())  
printSeries_Numbers(n)
