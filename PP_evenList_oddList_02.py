l_even=[]
l_odd=[]
                                                                                                                                                                                                                                                                while i!=-1:
    i=int(input("Enter a value(-1 to end) : "))
    if i%2==0:
        l_even.append(i)
    else:
        l_odd.append(i)
print("\nEven_list : ",*l_even)
print("Min : ",min(l_even))
print("max : ",max(l_even))
print("Avg : ",round(sum(l_even)/len(l_even),1))
print("\nOdd_list : ",*l_odd)
print("Min : ",min(l_odd))
print("max : ",max(l_odd))
print("Avg : ",round(sum(l_odd)/len(l_odd),1))

 
