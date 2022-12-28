##lst=[]
##dic={}
##for i in range(100,111):
##    for j in range(1,10):
##        if i%j==0:
##            lst.append(j)
##    dic[i]=max(lst)
##    lst.clear()
##print(dic)

dic={}
for i in range(100,111):
    dic[i]=max([j for j in range(1,10) if i%j==0]) 
print(dic)

##print({i:max([j for j in range(1,10) if i%j==0])} for i in range(100,111))


