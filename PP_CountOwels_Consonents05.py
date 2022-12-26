def extract_Owels_Consonents(s):
    temp_owel=''
    temp_consonent=''
    temp_number=''
    temp_spl=''
    for i in s:
        if i in 'AEIOUaeiou':
            temp_owel+=i
        elif i in '0123456789':
            temp_number+=i
        elif i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            temp_consonent+=i
        else:
             temp_spl+=i                           
    lst=[]
    lst.append(temp_owel)
    lst.append(temp_consonent)
    lst.append(temp_number)
    lst.append(temp_spl)
    return lst
inp=input("Enter your string : ")
lst=extract_Owels_Consonents(inp)

print("\nVowels are : ",lst[0],"\nvowels count : ",len(lst[0]),
      "\n\nConsonents are : ",lst[1],"\nConsonent count : ",len(lst[1]),"\n\nNumbers are : ",lst[2],
      "\nNumbers count : ",len(lst[2]),"\n\nSpecial characters are : ",lst[3],
      "\nSpecial characters count : ",len(lst[3]))
s1=sorted(lst[0])


                                             


##print("\nFrequency of Vowels : \n\nFrequency of A : ",s1.count('A'),
##      "\nFrequency of E : ",s1.count('E'),
##      "\nFrequency of I : ",s1.count('I'),
##      "\nFrequency of O : ",s1.count('O'),
##      "\nFrequency of U : ",s1.count('U'),
##      "\nFrequency of a : ",s1.count('a'),
##      "\nFrequency of e : ",s1.count('e'),
##      "\nFrequency of i : ",s1.count('i'),
##      "\nFrequency of o : ",s1.count('o'),
##      "\nFrequency of u : ",s1.count('u'),)
##            
