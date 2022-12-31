ap=open(r'D:\PythonPractice\day_10\append.txt','a')
inp=input('Entre your data : ')
ap.write(inp+'\n')
ap.close()
print('File written')

bp=open(r'D:\PythonPractice\day_10\append.txt','r')
bp.read()
bp.close
