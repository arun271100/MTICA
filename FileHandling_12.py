with open(r'D:\PythonPractice\day_10\Aover.txt','r') as fo:
    with open(r'D:\PythonPractice\day_13\NewFile1.txt','w+') as fo2:
        print(fo.read())
        fo2.write('Hey this is the new file :')
    with open(r'D:\PythonPractice\day_13\NewFile1.txt','r+') as fo3:
        print(fo3.read())
    
