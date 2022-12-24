def binarToDecimal(num):
    num=str(num)
    num=num[::-1]
    total=0
    temp=0
    for i in num:
        total+=int(i)*2**temp
        temp+=1
    return total

inp=int(input())
print(binarToDecimal(inp))
        
