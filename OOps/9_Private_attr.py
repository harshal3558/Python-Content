## Private(like) attributes & methods (__)
# Conceptual Implementations in Python
# Private attributes& methods are ment to be used only within thw class and are not accessible from outside the class.


class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account("12345","abcde")

print(acc1.acc_no)
print(acc1.acc_pass)


## Privating 

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # '__' is used to private the attribute

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcde")

print(acc1.acc_no)
# print(acc1.acc_pass)
print(acc1.reset_pass())

# We can access private keyword inside the class   