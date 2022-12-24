student=[[44,"Prasad",75,87],[13,"Gangully",82,79],
         [53,"Sasikala",72,80],[5,"Arun",86,85]]
student.sort()
print(student)
student.sort(key=lambda student:student[2])
print(student)
student.sort(key=lambda student:student[1])
print(student)
