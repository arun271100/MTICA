l=[]
i=1
while i!=0:
    i=int(input("Enter a value(0 to end) : "))
    l.append(i)
print("Min : ",min(l))
print("max : ",max(l))
print("Avg : ",round(sum(l)/len(l),1))
    
