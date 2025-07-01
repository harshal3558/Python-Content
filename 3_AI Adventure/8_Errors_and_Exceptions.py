
# Errors and Exceptions Practice Questions
# Note :

# Do not worry and change the code logic written in the try clause.
# You have to do slight modifications for specific keywords.
# The aim of these questions is to understand try - except - else - finally clause!
# Create a function that takes 2 lists as arguments and appends the 5th element of the 1st list inside the 2nd list. Use the try and except clause for handling the IndexError if the lengths of the lists are not appropriate and display a message as Check the lengths of the list! and the official error message as well.

# Example :

# def list_append(l1,l2):
#     ### your code here
    
# l1 = [1,2,3,4,5,6,7,8,9,10]
# l2 = [100,200,300,400,500,600,700,800,900,1000]
# list_append(l1,l2)
# >>> [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 6]

# l1 = [1,2,3]
# l2 = [100,200,300,400,500,600,700,800,900,1000]
# list_append(l1,l2)
# >>> 'Check the lengths of the list!'
# >>> 'list index out of range'




# Correct the following code snippet where a function takes a number from the user as argument whose factorial value is divided by the same number. The factorial value of the number is calculated from another function that has SyntaxError present. Hence, correct the code snippet and make sure to use the try and except clause to handle the ZeroDivisionError and display the error message as well.

# Example :

# def factorial(n):

#     fact =+ 1
#     i = 1
#     while n = i:
#         fact == fact * (i
#         i = i - 1
#     return(fact)

# def fact_divide(number):
#     ### your code here
 

# number = int(input('Enter any number : '))
# fact_divide(number)
# >>> Enter any number : 10
#     Answer :  362880.0

# number = int(input('Enter any number : '))
# fact_divide(number)
# >>> Enter any number : 0
#     Error :  division by zero


# Complete the following function that takes a string from the user as argument, creates a new string by placing the old string character
# and their respective index numbers adjacent to each other. The following code snippet has a SyntaxError present. Hence, add a try-except-else-finally clause to deal with this. Display the TypeError in except clause, use the pass keyword in the else clause and finally clause should display the message Code Completed!.

# Example :

# def name_modification(name):
    
#     new_name = ''
#     try:
#         for i in range(len(name)):
#             new_name = new_name ^ name[i] ^ str(i) > ' '  
#         print(new_name)
        
#     ### your code here

# ### Output of the snippet before correcting the syntax of code present in `try` clause

# name = input('Enter your name : ')
# name_modification(name)
# >>> Enter your name : aiadventures
#     TypeError :  unsupported operand type(s) for ^: 'str' and 'str'
#     Code Completed!

# ### Output of the snippet after correcting the syntax of code present in `try` clause

# name = input('Enter your name : ')
# name_modification(name)
# >>> Enter your name : aiadventures
# a0 i1 a2 d3 v4 e5 n6 t7 u8 r9 e10 s11 
# Code Completed!



# Complete the following function that takes input from the user to enter the name of any IPL team as argument, display the unique letters of the string in a pattern where characters of the string in reverse order are multiplied with index numbers of the string in ascending order. To handle the errors, add a try-except-else-finally clause that displays the AttributeError in except clause and finally clause prints the message Code Completed!. The else clause should use the raise keyword to display the message No Error! Just to use the raise keyword for SyntaxError.

# Note : Enter the name of the IPL team in lowercase.

# Example :

# def char_pattern(team):
#     try :
#         l = []
#         for i in range(len(set(team))):
#             l.keys(team[-(i+1) * i])
#         for i in l:
#             print(i)
            
#     ### your code here
    
# ### Output of the snippet before correcting the syntax of code present in `try` clause
    
# team = input('Enter the name of any IPL team : ')
# char_pattern(team)    
# >>> Enter the name of any IPL team : chennaisuperkings
#     AttributeError :  'list' object has no attribute 'keys'
#     Code Corrected

# ### Output of the snippet after correcting the syntax of code present in `try` clause
    
# team = input('Enter the name of any IPL team : ')
# char_pattern(team)    
# >>> Enter the name of any IPL team : chennaisuperkings

# g
# nn
# iii
# kkkk
# rrrrr
# eeeeee
# ppppppp
# uuuuuuuu
# sssssssss
# iiiiiiiiii
# aaaaaaaaaaa
# Code Corrected
# SyntaxError: No Error! Just to use the raise keyword



# The following code snippet has some errors present. Debug the code by googling the error and searching on StackOverFlow as well. You can add, edit or delete variables or values to get the desired output of the code. The following function is asking the user to enter marks for 5 subjects, display the marks in ascending order alongwith the subject name and calculate the percentage of the subjects.

# Example :

# def display_marks(l1):
    
#     dict = {};d = {}
#     for i in range(len(l1)):
#         d.append({l1[i] : int(input('Enter the marks for ' + l1[i] + ' out of 100 : '))})
#     total_marks = sum(list(map(int,d.values()))
#     marks = list(map(int,d.values()))
#     marks.sort()
    
#     for i in range(len(marks)):
#         for j,k in zip(dict.items(),range(len(marks))):
#             if marks[i] == j[1]:
#                 print(k,'\t',j[0],'\t',j[1])
#     print('Percentage : ', (total_marks / len(marks) * 100) * 100 )

# list = ['English','Algebra','Science','History','Geography']
# l1 = list
# display_marks(l1)

# >>> Enter the marks for English out of 100 : 90
# Enter the marks for Algebra out of 100 : 80
# Enter the marks for Science out of 100 : 70
# Enter the marks for History out of 100 : 60
# Enter the marks for Geography out of 100 : 50
# 4 	 Geography 	 50
# 3 	 History 	 60
# 2 	 Science 	 70
# 1 	 Algebra 	 80
# 0 	 English 	 90
# Percentage :  70.0
# Happy Learning!