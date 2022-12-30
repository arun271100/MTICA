def printSeries(ch,n):
    assert ((type(ch)==str)),'First number should be String'
    assert ((type(n)==int)),'Second number should be integer'
    for i in range(1,n+1):
        print(ch*i)
    for i in range(30):
        print('_',end=' ')
    print('\n')
    for i in range(n+1):
        print(ch*(n-i))
n1=input("Enter character : ")
n2=int(input('Enter the range : '))
try:
    printSeries(n1,n2)
except AssertionError as a:
    print(a)
