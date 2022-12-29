def printSeries(ch,n):
    for i in range(1,n+1):
        print(' '*(n-i),(ch+" ")*i)
ch=input("Enetr a symbol or character : ")
n=int(input('enter range : '))
printSeries(ch,n)
