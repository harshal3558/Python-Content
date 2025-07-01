## Loops Practice Questions

##  Difficulty Level : Easy

# 1. Create a program to display the first 10 even numbers in reverse order in a single line using end parameter of print function.

# Note : Use both the loops.

# for i in range(10,0,-1):
#     print(i*2,end=" ")

# n = 10
# while n != 0:
#     print(n*2,end=" ")
#     n-=1

# 2. Create a program that displays numbers starting from 20 to 40 with a difference of 5 in a single line using end parameter of print function.

# Note : Use both the loops.

# for i in range(20,40,5):
#     print(i,end=" ")

# n = 20
# while n!=40:
#     print(n)
#     n+=5

# 3. Create a program to display the cube of first 5 numbers in single line using end parameter of print function.

# Note : Use both the loops.

# for i in range(1,6):
#     print(i**3,end= " ")

# n= 0
# while n!=5:
#     print(n**3,end = " ")
#     n+=1

# 4. Create a program to display the factorial of a number.

# Note : Use both the loops with positive and negative step values.

# number = 5
# factorical = 1
# for i in range(1,number+1):
#     factorical *= i
# print(factorical)

# n = 5
# factorial = 1
# while n!=1:
#     factorial *= n
#     n-=1
# print(factorial)



## Difficulty Level : Medium

# 1. Create a program that keeps on accepting input from user until 0 is entered and print the sum of all the numbers entered at the end.

# n = ''
# sum = 0
# while n!=0:
#     n = int(input("Enter the number: "))
#     sum += n
# print(sum) 



# 2. Create a program to print the following series for n terms where n is the number taken from the user.

# Series : 2,22,222,2222,...... n terms

# n = input('Enter the term: ')
# for i in range(1,5):
#     print(n*i, end = ",")

# number = int(input('Enter the term: '))
# n = 0
# count = 0
# while count != 5:
#     n = (n*10)+number
#     print(n,end=",")
#     count+=1



## Difficulty Level : Hard

# 1. Create a program that displays the first number divisible by 5 between 6 to 16 and then break the loop.

# Note : Use both the loops.

# for i in range(6,16):
#     if i%5==0:
#         print(i)
#         break

# s=6
# e=16
# while s!=e:
#     if s%5==0:
#         print(s)
#         break
#     s+=1


# 2. Create a program that replicates the following output :

# Note : Use both the loops.

# The Multiplication Table of 2

# 2 x 1 = 2

# .

# .

# .

# The Multiplication Table of 3

# 3 x 1 = 3

# .

# .

# .

# The Multiplication Table of 4

# 4 x 1 = 4

# .



# n = int(input('Enter the number: '))
# for i in range(1,11):
#     print(i*n)

# n = 1
# number = int(input("Enter the number: "))
# while n!=11:
#     print(number*n)
#     n+=1