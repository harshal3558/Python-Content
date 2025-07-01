##  __class__ is a special attribute that refers to the class of an instance. It allows you to access the class to which an object belongs. 

# Supermethod
# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         self.name = name
#         # Person.name = name # It can be used to change class attribute.

# p1 = Person()
# p1.changeName('rahul kumar')
# print(p1.name)



# OR



# class Person:
#     name = "anonymous"

#     def changeName(self, name):
#         self.__class__.name = "Rahul"
#         #self.name = name
#         # Person.name = name # It can be used to change class attribute.

# p1 = Person()
# p1.changeName('rahul kumar')
# print(p1.name)
# print(Person.name)



# OR



class Person:
    name = "anonymous"
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName('rahul kumar')
print(p1.name)