# class Student:

#     college_name = "ABC College"

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print('Welcome student,',self.name)

#     def get_marks(self):
#         return self.marks
    
# s1 = Student('Karan',97)
# s1.welcome()
# print(s1.get_marks())

class Student:

    def __init__(self,name:str,marks:int):
        self.name=name
        self.marks=marks
    
    def welcome(self):
        print('Welcome student',self.name)

    def get_marks(self):
        return self.marks
    
s1=Student('karan',99)
s1.welcome()
print(s1.get_marks())
s2=Student('harsh',97)
s2.welcome()
print(s2.get_marks())