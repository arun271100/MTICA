def Even(n):
    if n%2==0:
        print(n,'is Even')
def Odd(n):
    if n%2!=0:
       print(n,'is odd')
       
for i in range(3):
    try:
        n=int(input('Enter a number  : '))
        Even(n)
        Odd(n)
    except Exception as a:
        print(a)
