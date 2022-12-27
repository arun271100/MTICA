import time
start=time.time()
inp=int(input('Enter number : '))
for i in range(1,11):
    print(inp,"*",i,"=",i*inp)
print("time taken : ",(time.time()-start)*100000)
