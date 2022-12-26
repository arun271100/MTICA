def isAnagram(s1,s2):
    if sorted(s1)==sorted(s2):
        return 'Yes'
    return 'No'
s1=input("Enter two string1 : ")
s2=input("Enter two string2 : ")
print(isAnagram(s1,s2))
