def frequency(string):
    dic={}
    for i in string:
        count=0
        for j in range(len(string)):
            if i==string[j]:
                count+=1
        dic[i]=count
    return dic
n=int(input())
for i in range(n):
    string=input()
    dic=frequency(string)   
    for i in sorted(dic.items(), key=lambda x:x[1],reverse=-1):
        if i[0] !=' ':
            print(i[0],'=',i[1])


    
