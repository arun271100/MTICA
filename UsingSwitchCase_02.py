def add(a,b):
    return 'a'+'+'+'b'+'='+str(a+b)
def sub(a,b):
    return 'a'+'-'+'b'+'='+str(a-b)
def mul(a,b):
    return 'a'+'*'+'b'+'='+str(a*b)
def div(a,b):
    return 'a'+'/'+'b'+'='+str(a/b)
def choice():
    print('''+ : Addition
- : Subtraction
* : Multiplication
/ : Division
Q or q : Quit
select your choice : ''')
select={'+':add,'-':sub,'*':mul,'/':div}
opt=0
while True:
    if opt=='q' or opt=='Q':
        break
    choice()
    opt=input()
    if opt in '+-*/':
        a=int(input('a : '))
        b=int(input('b : '))
        print('_'*20)
        print(select[opt](a,b))
        print('_'*20+'\n')
    elif opt not in 'Qq':
        print('INVALID INPUT\n')

