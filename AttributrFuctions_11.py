class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1

    def displayCount(self):
        print('Total employee : ',Employee.empCount)
    def displayEmployee(self):
        print('Name  : ',self.name,', salary : ',self.salary)
emp1=Employee('Arun',55000)
emp1.displayEmployee()
setattr(emp1,'name','Nandhu')
print(getattr(emp1,'name'))
print(hasattr(emp1,'des'))
##delattr(emp1,'name')
emp1.displayEmployee()
 
