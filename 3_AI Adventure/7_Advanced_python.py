
# Advanced Python Questions
# Difficulty Level : Easy
# Create a list to store the numbers between 111 to 200 that are divisible by 7 using comprehension.
# Create a dictionary with 5 key-value pairs that has key as an integer in string datatype and their respective value as a tuple consisting of 2 elements : key in float datatype & square value of key in integer datatype using comprehension.

# Example :

# >>> {'0': (0.0, 0), '1': (1.0, 1), '2': (2.0, 4), '3': (3.0, 9), '4': (4.0, 16)}
# Create a dictionary with key-value pairs that has key as the number and their respective value as True if the length of the number is greater than 1 else False using comprehensions.
# Create a set that filters the numbers that are divisible by 7 as well as 8 between 0 - 1000 using set comprehension.
# Difficulty Level : Medium
# Create a function that takes numbers as input, displays the sum of those numbers, stores the numbers inside a dictionary with number being the key and values being the square root of those numbers in reverse order in float datatype using map function and dictionary comprehension.

# Note : Use input() inside the function and use .split() to split the number string.

# Example :

# input('Enter the input numbers : ').split()
# >>> ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# def number_operation():
#     ### your code here
    
# number_operation()
    
# >>> Enter the input numbers : 1 2 3 4 5 6 7 8 9 10
    
#     Sum of Input Numbers :  55
        
#     {10.0: 3.1622776601683795, 9.0: 3.0, 8.0: 2.8284271247461903, 7.0: 2.6457513110645907, 6.0: 2.449489742783178, 5.0: 2.23606797749979, 4.0: 2.0, 3.0: 1.7320508075688772, 2.0: 1.4142135623730951, 1.0: 1.0}
# Create a function that uses dictionary comprehension to create a dictionary that stores the character of the string as the keys and its value will be a group of (1,True) if it is a vowel or (0,False) if it is not.

# Note : Try to solve this using zip function and without zip function.

# Example :

# def is_vowel(string1)::
#     ### your code here
    
# string1 = "practice problems to drill list comprehension in your head."
# is_vowel(string1)

# >>> {'p': (0, False),
#  'r': (0, False),
#  'a': (1, True),
#  'c': (0, False),
#  't': (0, False),
#  'i': (1, True),
#  'e': (1, True),
#  ' ': (0, False),
#  'o': (1, True),
#  'b': (0, False),
#  'l': (0, False),
#  'm': (0, False),
#  's': (0, False),
#  'd': (0, False),
#  'h': (0, False),
#  'n': (0, False),
#  'y': (0, False),
#  'u': (1, True),
#  '.': (0, False)}
# Difficulty Level : Hard
# Create a function that mimics a lottery system that is based on the vowels and consonants from the user's name. Vowels are worth 5 points each and consonants are worth 1 point each. Points calculation also includes the index numbers of the vowels and consonants. If the vowel points equates to consonant points, it is a lottery!

# Note : Enter your name in lowercase. Try solving this using enumerate and range function.

# Example :

# point_calculations = ( (5 * Number of vowels) or (1 * Number of consonants) ) + 
#                      ( sum(index values of vowels) or sum(index values of consonants) )

# name : 'abhishek'; index_values : 'a' = 0, 'b' = 1, 'h' = 2, 'i' = 3,
#                                   's' = 4, 'h' = 5, 'e' = 6 ,'k' = 7
# vowels = ['a', 'i', 'e']; consonants = ['b', 'h', 's', 'h', 'k']

# vowel_points = ( 5 * 3 vowels ) + ( 0 + 3 + 6 ) = 15 + 9 = 24
# consonant_points = ( 1 * 5 consonants ) + ( 1 + 2 + 4 + 5 + 7 ) = 5 + 19 = 24

# def lottery():
#     ##Your code here
    
# lottery()
# >>> Enter your name : abhishek
#     Vowel Points :  24
#     Consonant Points :  24
#     Lottery!!!!

# lottery()
# >>> Enter your name : aiadventures
#     Vowel Points :  56
#     Consonant Points :  46
#     Better Luck Next Time!
# Create a function to mimic the fermi pico bagels game by passing two strings as arguments using any type of comprehension.

# Note : Do not pass numbers with repetitive digits.

# Note : Make use of iterators, loops and flow control statements in the comprehension.

# Example :

# def result(guess_number,original_number):
#     ##Your code here
    
# result('143','345')
# >>> 'Fermi Pico'

# result('178','345')
# >>> 'Bagels'
# Happy Learning!