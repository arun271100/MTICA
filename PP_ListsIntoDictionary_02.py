l1=['Arun','Arshad','Anusha','Gangully']
l2=[90,88,97,75]
d={}
##for i in range(len(l1)):
##    d[l1[i]]=l2[i]


for i,j in zip(l1,l2):
    d[i]=j
print(d)


    
