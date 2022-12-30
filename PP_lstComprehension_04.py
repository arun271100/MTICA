x,y,z,n=1,1,1,2
##lst2=[]
##
##for i in range(x+1):
##    for j in range(y+1):
##        for k in range(z+1):
##            lst1=[]
##            if i+j+k!=n:
##                lst1.append(i)
##                lst1.append(j)
##                lst1.append(k)
##                lst2.append(lst1)
##            
##print(lst2)

print([[i,j,k] for i in range(x+1) for j in range(y+1)
        for k in range(z+1) if i+j+k!=n])
