def addNumber(n1,n2):
    assert(type(n1)==int),'string objects are not addable'
    assert(type(n2)==int),'string objects are not addable'
    return n1+n2
for i in range(4):
    try:
        n1=int(input("Enter a number : "))
        n2=int(input("Enter a number : "))
    except AssertionError as ae:
        print(ae)
    else:
        print(n1,"+",n2,"=",addNumber(n1,n2),sep="")
