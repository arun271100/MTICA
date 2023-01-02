#Deleting items in Dictionary
Dic={'name':'kelly','age':23,'salary':5000,'City':'Newyork','Planet':'Earth'}
print(Dic)
keys=['name','salary']

#1st Approach
for i in keys:
    Dic.pop(i)
print(Dic)

#2nd Approach
d={i:Dic[i] for i in Dic.keys()-keys}
print(d)
