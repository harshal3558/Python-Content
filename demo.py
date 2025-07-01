class Student():
    print("The class of 7th A")
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

s1 = Student('harsh','maths')
print(s1.name,s1.subject)