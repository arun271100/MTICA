ap1=open(r'D:\PythonPractice\day_10\append.txt','r')
temp=[]
for i in ap1.read():
    if i in "AEIOUaeiou":
        temp.append(i)
print(*temp)
print(len(temp))
ap1.close()


