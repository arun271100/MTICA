##temp=[]
##lst=[]
##for i in range(100,111):
##    for j in range(1,10):
##        if i%j==0:
##            temp.append(j)
##    lst.append([i,max(temp)])
##print(lst)

##lst=[]
##for i in range(100,111):
##    lst.append([i,max([j for j in range(1,10) if i%j==0])])
##print(lst)
##

print([[i,max([j for j in range(1,10) if i%j==0])]for i in range(100,111)])
