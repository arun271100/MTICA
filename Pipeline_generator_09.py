def gen1(n):
    for i in range(n):
        yield i
def gen2(temp):
    for n in temp:
        if n%2:
            yield n
for i in gen2(gen1(10)):
    print(i)
    
