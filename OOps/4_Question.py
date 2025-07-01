# Create student class that takes names & marks of 3 subjects as arguments in constructor. Then create a method  to print the average.

# class Students:

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def marks_avg(self):
#         sum = 0
#         for i in self.marks:
#             sum +=i
#         print(f'Hi, {self.name}, your average marks is: {sum/3}')

# s1 = Students('Tony',[99,97,95])
# s1.marks_avg()



class student:

    def __init__(self,marks,name):
        self.marks=marks
        self.name=name

    def average(self):
        sum=0
        for i in self.marks:
            sum += i
        print(f"Hi, {self.name}, your aerage score is {sum/3}")

s1=student([99,98,97],'harsh')
s1.average()