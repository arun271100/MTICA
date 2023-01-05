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
print('Total employee : ',Employee.empCount)
emp2=Employee('Naveen',45000)
emp1.displayEmployee()
emp2.displayEmployee()
print('Total employee : ',Employee.empCount)
emp3=Employee('Prathap',44000)
emp3.displayEmployee()
emp1.displayCount()
emp2.displayCount()
emp3.displayCount()
print('Total employee : {0}'.format(Employee.empCount))


