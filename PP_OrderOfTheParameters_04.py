def Function(name ,marks=90,Age=22):
    print('Name : ',name)
    print('Marks : ',marks)
    print('Age : ',Age)
    return

##Function()
##Function('Arun',80)
##Function(Age=23,'Arun',marks=80)  #Error Positional Arguements should not follow keywords
Function('Arun',Age=23,marks=80)
