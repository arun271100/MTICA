##matrix=[[1,2],[3,4],[5,6],[7,8]]
##m1=[]
##m2=[]
##res=[]
##for i in matrix:
##    temp=i
##    m1.append(temp[0])
##    m2.append(temp[1])
##res.append(m1)
##res.append(m2)
##print(res)

m=[[1,2],[3,4],[5,6],[7,8]]
##n=[]
##for i in range(len(m[0])):
##    temp=[]
##    for j in range(len(m)):
##        temp.append(m[j][i])
##    n.append(temp)
##print(n)

print([[m[j][i] for j in range(len(m))] for i in range(len(m[0]))])
    
