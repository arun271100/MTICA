ap1=open(r'D:\PythonPractice\day_10\append.txt','r')
ap2=open(r'D:\PythonPractice\day_10\Aover.txt','w')
ap2.write(ap1.read())
ap1.close()
ap2.close()
print('File copied successfully')

