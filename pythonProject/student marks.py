"""
author anilkumar
problem statement:
displaying marks of student and name

"""


class Student:
    def __init__(self,marks,name):
        self.name=name
        self.marks=marks
student=Student(550,'anil')
print(student.marks)
print(student.name)
