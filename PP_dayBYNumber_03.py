import time
start=time.time()
def dayBYNumber(n):
    if n>=0 and n<=6:
        if n==0:
            res='SUN'
        if n==1:
            res='MON'
        if n==2:
            res='TUE'
        if n==3:
            res='wed'
        if n==4:
            res='THU'
        if n==5:
            res='FRI'
        if n==6:
            res='SAT'
        return res
    else:
        return 'INVALID'
for i in range(5):
    n=int(input())
    print(dayBYNumber(n))
    stop=time.time()
    print('Time Taken : ',stop-start)
        
    
