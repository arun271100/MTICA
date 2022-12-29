def div(a,b):
    assert( isinstance(a,int) or isinstance(a,float)),\
    'Firat Arguements should be either int or float'
    assert( isinstance(b,int) or isinstance(b,float)),\
    'Second Arguements should be either int or float'
    assert(b!=0),"Division by zero is not defined !"
    return a/b
try:
    print(div(12,4))
except AssertionError as a:
    print(a)
try:
    print(div(12,''))
except AssertionError as a:
    print(a)
 
