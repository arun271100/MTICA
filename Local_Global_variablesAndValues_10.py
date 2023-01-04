x=5;y=7
def changeme(mylist):
    p=45
    global x,y
    x=x+8
    mylist=[1,2,3,4,5]
    print('Values inside the function : ',mylist)
    print('local variables are : ',locals())
    print('global variables are : ',globals())
    return
mylist_new=[10,20,30,40]
changeme(mylist_new)
print('values outside the function : ',mylist_new)
