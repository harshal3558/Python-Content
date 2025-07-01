## Functions Practice Questions

## Difficulty Level : Easy

# 1. Create a function to calculate the cube of a number that is passed as the argument to the function.

# Example :

# def cube(number):
#     ### your code here

# number = 4

# cube(number)

# >>> 64

# def cube(number):
#     print(number**3)
# number = 4
# cube(number)



# 2. Create a function to calculate the sum of square of 2 numbers that are defined as the default arguments and its square output is 5.

# Example :

# def square(n1 = value,n2 = value):
#     ### your code here

# square()

# >>> 5

# def square(n1=1,n2=2):
#     print((n1**2)+(n2**2)) 
# square()



# 3. Create a function to calculate the factorial of a number which is passed as an argument and assign the output of the function to a variable named out.

# Example :

# def factorial(number):
#     ### your code here

# out = factorial(5)
# out

# >>> 120

# def facto(number):
#     factorial = 1
#     for i in range(1,number+1):
#         factorial *=i
#     print(factorial)
# number = int(input("Enter the number: "))
# facto(number)



# 3. Correct the syntax of the following function to get the required output.

# Note : Make use of all the concepts covered until now.

# Example :

# defn 123string_concatenation{s1 = 'ai',s2 ,s3 = 3);
    
#     elif s3 == 3;
#     s = s1 + s2 * s3
#         printf[s,end = '-')
#     else;;
#     s = s1 + s2 * 1
#     printf(s,end = '->'\
    
#     123string_concat{'adventures']

#         >>> 'aiadventuresaiadventuresaiadventures'

# def string_concatenation(s1 = 'ai',s2='',s3 = 3):
#     if s3 == 3:
#         s = (s1 + s2) * s3
#         print(s,end = '')
#     else:
#         s = s1 + s2 * 1
#         print(s,end = '')
    
# string_concatenation(s2='adventures')




## Difficulty Level : Medium

# 1. Create a function to calculate the area of triangle or rectangle using 3 arguments : base, height and shape.

# Example :

# def calculate_area(base, height,shape):
#     ### your code here

# b = 2
# h = 6

# calculate_area(b,h, 'Rectangle')

# >>> 12


# calculate_area(b,h, 'Triangle')

# >>> 6.0


# def calculate_area(base,height,shape):
#     if shape == 'rectangle':
#         print(base*height)
#     if shape =='triangle':
#         print(1/2*base*height)

# base = 2
# height = 6
# shape = 'rectangle'
# calculate_area(base,height,shape)




# 2. Create a function that returns None value and display the result of the string concatenation.
# You have to take the 2 strings required for the function as argument as shown in the example given below.
# Example :

# def none_value_assignment(s1 = input(),s2 = input()):
#     ### your code here

# var1 = none_value_assignment()
# type(var1)

# >>> result of string concatenation of s1 and s2
# >>> NoneType

# var2 = none_value_assignment('ai', 'adventures')
# type(var2)

# >>> aiadventures
# >>> NoneType

# def none_value_assignment(s1=None, s2=None):
#     # If no arguments are provided, prompt for input
#     if s1 is None:
#         s1 = input("Enter first string: ")
#     if s2 is None:
#         s2 = input("Enter second string: ")
    
#     # Concatenate the strings
#     result = s1 + s2
    
#     # Return the concatenated result
#     return result

# # Example usage
# var1 = none_value_assignment()  # Will prompt for input
# print(var1)  # Outputs the concatenated string

# var2 = none_value_assignment('ai', 'adventures')  # Directly provides inputs
# print(var2)  # Outputs 'aiadventures'




## Difficulty Level : Hard

# 1. Create a function to calculate and display the sum of the following sequence by taking input from user for n.

# Sequence : 1 + 1/1! + 1/2! + 1/3! + + 1/n!

# Hint : Give a thought above factorial() you have just created a few problems back.

# def sequence(n):
#     ### your code here

# sequence(5)
# >>> 2.7166666666666663


# def facto(number):
#     factorial = 1
#     for i in range(1,number+1):
#         factorial *= i
#     return factorial

# def sequence(num):
#     seq = 1
#     for i in range(1,num+1):
#         seq = seq + 1/facto(i)
#     return seq

# print(sequence(5))



# 2. Create a function to check whether a string is pangram or not.

# Pangram Definition : It is a sentence containing all 26 letters of the English alphabets.

# Example :

# def ispangram(sentence):
#     ### your code here

# sentence1 = "a quick brown fox jumps over the lazy dog"
# sentence2 = "hello my name is ramesh"

# ispangram(sentence1)

# >>> True

# ispangram(sentence2)

# >>> False


# def ispangram(sentence):
#     ### your code here
#     alphabet= 'abcdefghijklmnopqrustuvwxyz'
#     for letter in alphabet:
#         if letter not in sentence:
#             return False
#     else:
#         return True


# sentence1 = "a quick brown fox jumps over the lazy dog"
# sentence2 = "hello my name is ramesh"

# print(ispangram(sentence1))
# print(ispangram(sentence2))