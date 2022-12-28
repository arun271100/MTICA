string='''
Practice problems for list com pre hension in python
'''
lst=string.split()
lst=[i.strip('\n') for i in lst ]
dec={i:len(i) for i in lst}
print(dec)
