# Static Method -
# Method that donot use the self parameter 
# It works at class level
# It is a decoratore in python

class Student:
    
    @staticmethod
    def college():
        print('ABC College')

# It allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.