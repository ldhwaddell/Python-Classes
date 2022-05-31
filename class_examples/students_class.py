class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass_fail(self):
        """"""
        if self.marks >= 40:
            return True
        else: 
            return False 


    

student1 = Student("Lucas", 90)
print(student1.name)
print(student1.marks)

