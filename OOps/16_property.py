# Property Decorator

class Student:

    def  __init__(self,phy,che,math):   # constructor
        self.phy = phy                  # phy attribute
        self.che = che
        self.math = math
        # can use this but have drawback
        # self.percentage = str((self.phy + self.che+ self.math) / 3) + '%'

    
    # def calcPercentange(self):     # method
    #     self.percentage = str((self.phy + self.che+ self.math) / 3) + '%'

    @property
    def percentage(self):
        return str((self.phy + self.che+ self.math) / 3) + '%'



stu1 = Student(98,97,99)
print(stu1.percentage)

# change or update
stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentange()  
print(stu1.percentage)

# There is more easier method to use that is Property method
