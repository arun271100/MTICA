class Student:
    college='MTICA'
    course='MCA'
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def displayStudent(self):
        print()
        print('college : '+self.college+'\ncourse : '+self.course+\
              '\nName : '+self.name+'\nRoll : '+str(self.roll))
if __name__=='__main__':
    l1=[]
##    for i in range(1,3):
##        print('STUDENT',i)
##        name=input('Name : ')
##        roll=int(input('Roll.no : '))
##        l1.append(name)
##        l1.append(roll)
##    for i in range(0,len(l1),2):
##        s1=Student(l1[i].title(),l1[i+1])
##        s1.displayStudent()
    for i in range(2):
        n=input()
        r=int(input())
        temp=Student(n,r)
        l1.append(temp)
    for i in l1:
        i.displayStudent()
