def remove_vowel(s):
    s1=''
    for i in s:
        if i not in 'AEIOUaeiou':
            s1+=i
    return s1
inp=input("Enter String : ")
print("String without vowel : ",remove_vowel(inp))
