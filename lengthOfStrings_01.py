def countLength(inp):
    l=inp.split()
##    for i in l:
##        print(len(i),end=' ')
    return [len(i) for i in l]
inp=input()
print(*countLength(inp))
