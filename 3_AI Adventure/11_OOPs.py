
# OOP Practice Questions
# Difficulty Level : Easy

# class Student():
#     print("Object Created Successfully!")

#     def __init__(self,fullname):
#         self.name = fullname
#         print("adding student in database.")

# s1 = Student('Karan')
# print(s1.name)
# s2 = Student('Arjun')
# print(s2.name)



## Create a class named Display_Info that has 4 instance variables : name, age, hobby and favourite_colour and
## a method display that displays the instance variables in the same order. Also, make sure to display a message :
## Object Created Successfully! whenever an object is created.

# Example :

# class Display_Info():
#     ### your code here
        
# di1 = Display_Info('Ai Adventures',35,'Drawing','Red')
# di1.display()
# >>> Object Created Successfully!
# Name of the Person :  Ai Adventures
# Age of the Person :  35
# Hobby of the Person :  Drawing
# Favourite Colour of the Person :  Red

# class Display_Info():
#     print("Object Created Successfully!")

#     def __init__(self,name, age, hobby, favourite_colour):
#         self.name = name
#         self.age = age
#         self.hobby = hobby
#         self.favourite_colour = favourite_colour


#     def display(self):
#         print("name of the Person :", self.name)
#         print("Age of the Person : ", self.age)
#         print("Hobby of the Person : ", self.hobby)
#         print("Favourite Colour of the Person : ", self.favourite_colour)

# d1 = Display_Info('Harshal',23,'football','white')
# detail1 = d1.display()


    # def content(self ,name:str ,age:int ,hobby:str ,favourite_colour:str) :
    #     self.name = name#input("Enter the name: ")
    #     self.age = age#int(input("Enter the age: "))
    #     self.hobby = hobby#input("Enter the hobby: ")
    #     self.favourite_colour = favourite_colour#input("Enter the fovourite colour: ")

# di = Display_Info(Hassrahl)
# s1 = di.content('Harshal',23,'football','white')
# print(s1)





# Create a class named Circle that has a constructor variable radius and 2 methods that calculate the area and the perimeter of the circle.

# Example :

# class Circle():
#     ### your code here
        
# c1 = Circle(8)
# c1.area()
# >>> 'Area of the Circle :  200.96'

# c2 = Circle(17)
# c2.perimeter()
# >>> 'Perimeter of the Circle :  106.76'

# class Circle(): 
#     ### your code here
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         area = 3.14*(self.radius**2)
#         print("Area of Circle is :", area)

#     def perimeter(self):
#         perimeter = 2 * 3.14 * (self.radius)
#         print("Perimeter of the Circle is :",perimeter)
        
# c1 = Circle(8)
# c1.area()
# c1.perimeter()



# Create a class named marks_calculation that has no constructor and no instance variables but has a method named percentage that takes input from the user for marks out of 100 for 5 subjects : ['English','Geometry','History','Science','Geography'] and stores them inside a dictionary with subject names as keys and marks as values. It is then stored as an instance variable marks, display this variable alongwith the percentage of the marks.
# class marks_calculation():
#     ### your code here
        
# m1 = marks_calculation()

# m1.percentage()
# >>> Enter the marks for English out of 100 : 90
# Enter the marks for Geometry out of 100 : 80
# Enter the marks for History out of 100 : 70
# Enter the marks for Science out of 100 : 60
# Enter the marks for Geography out of 100 : 50
# Percentage :  70.0
    
# m1.marks
# >>> {'English': 90, 'Geometry': 80, 'History': 70, 'Science': 60, 'Geography': 50}






# Create a class named BankAccount that contains 2 initialization variables balance and min_balance = 1000. Value for balance variable is passed during object creation whereas min_balance is already defined inside the constructor. It should also contain 2 methods withdraw() and deposit() that takes an argument to add or reduce the balance. Account should maintain min_balance and should not drop the balance below it. Display the balance and appropriate messages after evey withdrawal and deposit.

# Example :

# class BankAccount():
#     ### your code here
        
# b1 = BankAccount(3000)
# b1.withdraw(2000)
# >>> Withdrawal successful!
# New Account Balance : ₹ 1000

# b1.withdraw(500)
# >>> Withdrawal denied! Cannot let balance cross the min_balance limit!
# Account balance if this withdrawal is allowed : ₹ 500

# b1.deposit(1000)
# >>> Deposit successful!
# New Account Balance : ₹ 2000
# Difficulty Level : Medium





# Create a class named Point that consists of 2 constructor variables x and y, 9 Dunder or Magic methods and a length method to carry out a varied range of operations assuming the constructor variables as x co-ordinate and y co-ordinate of a point respectively. Constructor of the class Point should display a message : Point (x,y) created! as well.

# List of Dunder or Magic methods : [addition, subtraction, multiplication, true division, greater than, greater than equal to, less than, less than equal to, equal to equal to]

# Note : Google about Dunder or Magic methods.

# Example :

# class Point:
#     ### your code here
    
# p1 = Point(10,5)
# p2 = Point(5,10)

# print(p1 + p2)
# print(p1 - p2)
# print(p1 * p2)
# print(p1 / p2)
# print(p1 > p2)
# print(p1 >= p2)
# print(p1 < p2)
# print(p1 <= p2)
# print(p1 == p2)

# >>> 
# Point (10,5) created!
# Point (5,10) created!
# (15, 15)
# (5, -5)
# 100
# (2.0, 0.5)
# False
# True
# False
# True
# False




# Create a class named Course that has 1 default value constructor variable course = 'Machine Learning' and a method average_score that takes marks from the user for 5 tests, assigns it to a new constructor variable scores and calculates the average score of these marks. Create another class named student which has 2 instance variables name and age and inherits the Course class. It also contains a method display_info that displays a message using the attributes of Course class and student class, it also displays the average score using the average_score method of the Course class.

# Note : Try using super keyword and without using super keyword.

# Example :

# class Course:
#     ### your code here
    
# s1 = student('Aiadventures',35)
# s1.display_info()

# >>> Aiadventures, age 35, has enrolled in Machine Learning course!
# Enter the marks scored out of 10 : 8 9 7 10 6
# Average Score of Aiadventures in Machine Learning course :  8.0
# Difficulty Level : Hard




# Create a program that mimics a real-life SUPEROVER in cricket by creating a class named Team_Performance having no constructor but 3 constructor variables : team = {}, runs = [] and wickets = 0 defined in the only method play of the class. play is responsible for generating the scorecard and storing it inside team, runs and wickets are stored inside runs and wickets respectively. Another class named Superover inherits class Team_Performance that contains a constructor with 2 instance variables : team1 and team2 and displays a message "Let's begin the Superover between team1 and team2!" whenever an object is created. It also contains a method begin that calls the play method twice, stores the scorecard, runs and wickets information for both the teams and displays the final ouput.

# Note : Runs are calculated using random.randint(0,6) from random module.

# Note : You will have to create new variables inside begin method. The aim of this question is to learn about the structure of code as well as deciding the number of variables and their usage.

# Note : 0 is considered as wicket and 5 as run is not accepted.

# Example :

# class Team_Performance:
#     ### your code here
    
# match = Superover('A','B')
# match.begin()

# >>> Let's begin the Superover between A and B!
# Performance of A : {'B1': 4, 'B2': 4, 'B3': 4, 'B4': 1, 'B5': 1, 'B6': 2}
# Performance of B : {'B1': 2, 'B2': 3, 'B3': 2, 'B4': 6, 'B5': 0, 'B6': 2}
# Scorecard of A : 16 / 0
# Scorecard of B : 15 / 1
# A wins by 1 runs!

# >>> Let's begin the Superover between A and B!
# Performance of A : {'B1': 6, 'B2': 1, 'B3': 0, 'B4': 1, 'B5': 1, 'B6': 6} 
# Performance of B : {'B1': 4, 'B2': 1, 'B3': 0, 'B4': 6, 'B5': 3, 'B6': 2}
# Scorecard of A : 15 / 1
# Scorecard of B : 16 / 1
# B wins by 1 runs!

# >>> Let's begin the Superover between A and B!
# Performance of A : {'B1': 1, 'B2': 1, 'B3': 4, 'B4': 0, 'B5': 3, 'B6': 6}
# Performance of B : {'B1': 4, 'B2': 0, 'B3': 2, 'B4': 1, 'B5': 2, 'B6': 6}
# Scorecard of A : 15 / 1
# Scorecard of B : 15 / 1
# Its a Draw!




# Create a program that mimics a race by creating a class named Player that has 2 instance variable name and distance = 0, 1 class variable number_of_steps and 3 methods : walk, run and jump that increment distance by 0.5, 1 and 2 respectively. Create another class named Race with no constructor but with 2 methods : number_generator and start where number_generator uses random.randint to generate numbers. start method initiates the game and uses walk, run and jump methods of Player class when the generated number is an odd number, even number and prime number respectively. Increment the number_of_steps variable whenever any of the methods of Player class is executed. The game is won by the player that achieves the distance of 20 points in the fewest number_of_steps.

# Note : Do not use inheritance. Pass objects as method arguements.

# Example :

# class Player:
#     ### your code here
    
# p1 = Player('P1')
# p2 = Player('P2')
# race = Race()
# race.start(p1,p2)

# >>> P1 won the race with 16 steps!
# Roadmap of P1 :  {2: 'Jump', 4: 'Jump', 5: 'Run', 7: 'Jump', 8: 'Run', 9: 'Run', 10: 'Run', 12: 'Jump', 12.5: 'Walk', 13.5: 'Run', 15.5: 'Jump', 16.0: 'Walk', 17.0: 'Run', 18.0: 'Run', 20.0: 'Jump', 22.0: 'Jump'}
# P2 lost the race and took 17 steps!
# Roadmap of P2 :  {1: 'Run', 2: 'Run', 3: 'Run', 4: 'Run', 5: 'Run', 6: 'Run', 8: 'Jump', 9: 'Run', 11: 'Jump', 12: 'Run', 14: 'Jump', 14.5: 'Walk', 16.5: 'Jump', 17.0: 'Walk', 19.0: 'Jump', 20.0: 'Run', 21.0: 'Run'}

# >>> P2 won the race with 15 steps!
# Roadmap of P2 :  {1: 'Run', 3: 'Jump', 3.5: 'Walk', 5.5: 'Jump', 7.5: 'Jump', 8.5: 'Run', 9.5: 'Run', 11.5: 'Jump', 12.5: 'Run', 14.5: 'Jump', 15.5: 'Run', 17.5: 'Jump', 19.5: 'Jump', 20.0: 'Walk', 22.0: 'Jump'}
# P1 lost the race and took 16 steps!
# Roadmap of P1 :  {2: 'Jump', 2.5: 'Walk', 3.5: 'Run', 5.5: 'Jump', 6.5: 'Run', 7.0: 'Walk', 9.0: 'Jump', 9.5: 'Walk', 11.5: 'Jump', 13.5: 'Jump', 14.5: 'Run', 15.0: 'Walk', 17.0: 'Jump', 18.0: 'Run', 19.0: 'Run', 21.0: 'Jump'}
    
# >>> Its a Draw!
# P1 steps : 15
# Roadmap of P1 :  {2: 'Jump', 3: 'Run', 4: 'Run', 5: 'Run', 7: 'Jump', 9: 'Jump', 9.5: 'Walk', 10.5: 'Run', 11.5: 'Run', 13.5: 'Jump', 14.5: 'Run', 16.5: 'Jump', 18.5: 'Jump', 19.5: 'Run', 21.5: 'Jump'}
# P2 steps : 15
# Roadmap of P2 :  {1: 'Run', 3: 'Jump', 5: 'Jump', 6: 'Run', 6.5: 'Walk', 7.5: 'Run', 8.5: 'Run', 10.5: 'Jump', 12.5: 'Jump', 14.5: 'Jump', 15.0: 'Walk', 16.0: 'Run', 18.0: 'Jump', 19.0: 'Run', 21.0: 'Jump'}
# Happy Learning!



