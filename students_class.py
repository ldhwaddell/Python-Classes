from ast import Str


class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else: 
            return False 

    def __init__(self, name:Str, marks:int):
        self.name = name
        self.marks = marks
    

student1 = Student("Lucas", 90)
print(student1.name)
print(student1.marks)

