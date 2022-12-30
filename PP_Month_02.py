##def nameofMoth(n,dic):
##    if n<=12 and n>0:
##        return dic[n]
##    else:
##        return 'INVALID INPUT'
##
##n=int(input())
##dic={1:'January',2:'February',3:'March',4:'April',5:'May',6:'june',
##     7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
##print(nameofMoth(n,dic))



def nameOfMonth(n):
    if n==1:
        mn='Jan'
    elif n==2:
        mn='Feb'
    elif n==3:
        mn='Mar'
    elif n==4:
        mn='Apr'
    elif n==5:
        mn='May'
    elif n==6:
        mn='Jun'
    elif n==7:
        mn='Jul'
    elif n==8:
        mn='Aug'
    elif n==9:
        mn='Sep'
    elif n==10:
        mn='Oct'
    elif n==11:
        mn='Nov'
    elif n==12:
        mn='Dec'
    else:
        mn='INVALID'
    return mn
n=int(input())
print(nameOfMonth(n))
