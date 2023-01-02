Dic={'name':'kelly','age':23,'salary':5000,'City':'Newyork','Planet':'Earth'}

#Approach 1
if 23 in Dic.values():
    print(23,'Exists')
else:
    print(23,'Not Exists')

#Approach 2 for getting value and item both
for i,j in Dic.items():
    if j==23:
        print('for',"(",i,")",'Value is',j)

#Assigning by pop method
Dic['Loaction']=Dic.pop('City')
print(Dic)
