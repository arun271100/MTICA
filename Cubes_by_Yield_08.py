def cubes():
    i=1
    while 1:
        yield i**3
        i+=1
for i in cubes():
    if i>1000:
        break
    print(i)
    
