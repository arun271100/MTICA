n1=input("Enter a number : ")
n2=input("Enter a number : ")
try:
    res=int(n1)/int(n2)
except (ZeroDivisionError,ValueError):
    print('\nZeroDivisionError : Exception handled by Arun')
##except ValueError:
##    print('\nValueError : Exception handled by Arun')
except Exception as a:
    print(a)
else:
    print(n1,'/',n2,'=',res)
finally:
    print('\nThank u , Visit Again')
            
