def remove_duplicates(s):
    s1=''
    for i in s:
        if i not in s1:
            s1+=i
    return s1
inp=input("Enter a string : ")
print("string without duplicates : ",remove_duplicates(inp))
