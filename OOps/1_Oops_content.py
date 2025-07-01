class Student:

    def __init__(self,fullname):
        self.fullname = fullname # name= attributes
        print('Adding new student in database')

s1 = Student('Karan')
print(s1.fullname)
s2 = Student('Arjun')
print(s2.fullname)


# class Student:

#     def __init__(self,name):
#         self.name = name
#         # print('Hello {}'.format(name))
#         print('done')

# s1 = Student('Karan')
# student_list = []
# s = s1.name
# student_list.append(s)
# print(s)