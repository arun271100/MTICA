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
emp1.name='Anand'
emp1.salary=45000
emp1.displayEmployee()
emp1.experience=3
print(emp1.experience)
emp1.name='Naveen'
##del emp1.salary
emp1.displayEmployee()
