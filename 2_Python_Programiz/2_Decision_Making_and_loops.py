# Decision Making and Loops

### Python Program to check if a number is positve, negative, or 0.

# def check(number):
#     if number < 0:
#         print(number," is negative.")
#     elif number == 0:
#         print(number,'is niether  positive nor negative, it is zero.')
#     elif number > 0:
#         print(number,'is positve.')
#     else:
#         print('Error')
# check(5)

### Python program to check if number is odd or Even.

# def odd_even(number):
#     if number % 2 == 0:
#         print(number,'is even')
#     elif number % 2 == 1:
#         print(number,"is odd")
#     else:
#         print('error')
# odd_even(13)

### Python program to check leap year

# def leap_year(year):
#     leap = False
#     if year % 4 == 0:
#         if year % 100 == 0:
#             leap = True
#             print(year,'is Leap year')
#         elif year % 400 == 0:
#             leap = True
#             print(year,'is leap year')
#     else:
#         leap = False
#         print(year,'is not leap year')
# leap_year(2000)

### Python Program to find the largest among three numbers

# def largest_three(a,b,c):
#     if a > b and a > c:
#         print(a,f"is largest among {a},{b},{c}.")
#     elif b > a and b > c:
#         print(b,f"id largest among {a},{b},{c}.")
#     else:
#         print(c,f"is largest among {a},{b},{c}")
# largest_three(4,3,5)

### Python program to check prime number

# def check_prime(number):
#     for i in range(2,number):
#         if number % i == 0:
#             return (number,'is not prime.')
#             break
#     else:
#         return (number,'is prime.')
# # check_prime()

### Python program to print all prime number in an Interval.

# def all_prime(number):
#     for i in range(2,number):
#         print(check_prime(i))
# all_prime(15)

### Python program to find the factorial of a number

# def facto(number):
#     factorial = 1 
#     for i in range(1,number+1):
#         factorial = factorial * i
#     print(f"Factorial of {number} is",factorial)
# facto(5)

### Python Program to Display the Multiplication Table

# def table(number):
#     for i in range(1,11):
#         print(f"{number} X {i} =",number*i)
# table(2)

### Python program to print Fibonacci Sequence

# def fibonacci(number):
#     fibo = []
#     a,b = 0,1
#     for i in range(0,number+1):
#         fibo.append(i)
#         a, b = b, a+b
#     return fibo
# print(fibonacci(10))

### Python program to check Armstrong NUmber

# def arm(number):
#     str_num = str(number)
#     length = len(str_num)
#     sum = 0
#     for i in str_num:
#         sum = sum + (int(i)**length)
#     if sum == int(number):
#         print(number,"is Armstrong number")
#     else:
#         print(number,"is not armstrong number") 
# # number = input('Enter the number: ')

### Python Program to find armstrong number in an Interval

# def interval_arm(number):
#     for i in range(number+1):
#         print(arm(i))
# interval_arm(160)

### Python Program to find sum of natural numbers

# def sum(number):
#     total = 0
#     for i in range(0,number+1):
#         total += i
#     print(total)
# sum(10)

### Python Program to create pyramid pattern

# def pyramid(n):
#     for i in range(n,0):
#         print(i*'*')
#         n-=1
#     for j in range(0,n):
#         print(j*'*')
# pyramid(5)

### Python Program to iterate over Dictionaries using for loop


### Python Program to Reverse a number

# def rev_1(number):
#     print(int(str(number)[::-1]))
# rev_1(123)

### Python Program to Compute the power of a number

# def power_number(number):
#     return num**number
# num = int(input('Enter the number to be powered: '))
# number = int(input('Enter the power: '))
# print(f"The number {number} with power of {num} is",power_number(number))