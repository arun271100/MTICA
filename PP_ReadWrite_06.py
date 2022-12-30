gh=open('D:\Arun.txt')
temp=gh.read()
gh.close
print('Name of the file :: ',gh.name)
print('closed or not ::',gh.closed)
print(temp)
