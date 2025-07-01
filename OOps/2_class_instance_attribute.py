# Class Attribute
# Object Attribute

# Object Attribute have higher priority than Class Attribute

class Students:     # --> Class Name

    college_name = "ABC"    # Class Attribute

    def __init__(self,name,marks):  # __init__ Constructor  (parameter)
        self.name = name            # name parameter
        self.marks = marks          # marks parameter

    def hello(self):
        print('hello',self.name)

# Creating Object
s1 = Students('Karan',34)
s1.hello()