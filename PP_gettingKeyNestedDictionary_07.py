sampDic={'name':'kelly','age':23,'salary':5000,'City':'Newyork'}
keys=['name','salary']
newDic={}
for i in keys:
    newDic[i]=sampDic[i]
print(newDic)

d={i:sampDic[i] for i in keys}
print(d)

for i in keys:
    newDic.update({i:sampDic[i]})
print(newDic)
