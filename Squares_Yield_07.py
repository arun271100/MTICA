def squares(x=0):
    while x<10:
        x+=1
        yield x**2

##ylist=list(squares())
##print(list(ylist))

l=[i for i in squares()]
print(l)
