# Flow Control Practice Questions

## Difficulty Level : Easy

# 1.Fill in the blanks with the boolean operators in the following code snippet to get the desired output :

# Code Snippet	Output
# True __ True	True
# ( 1 > 2 ) __ ( 55 < 54)	False
# ( 55 / 2 ) __ True	True
# __ ( 10 > 5 )	False

# True and True == True
# ( 1 > 2 ) or ( 55 < 54) ==	False
# ( 55 / 2 ) and True == True
# ( 10 > 5 ) == False


# 2. Create a program that asks the user to enter the net worth of Mark Zuckerberg and display the specific message as mentioned in the table below according to the input from the user.

# Note : Make sure you enter the appropriate message in input function that assists user in entering the values.

# Note : Do not enter commas when entering the number.

# Net Worth	Display
# = 54500000000	That's 54.5 billion!
# < 54500000000	That's not much!
# > 54500000000	I'll make more when I graduate

# def net_worth(user):
#     try:
#         if user == 54500000000:
#             print("That's 54.5 billion!")
#         elif user < 54500000000:
#             print("That's not much!")
#         elif user > 54500000000:
#             print("I'll make more when I graduate")
#     except:
#         'IndentationError'
#         print('You are having indentation error')

# user = int(input('enter the net worth of Mark Zuckerberg: '))
# net_worth(user)


# 3. Create a program to accept the cost price of a bike and display the total price of the bike including the tax to be paid according to the following criteria :

# Note : Make sure you enter the appropriate message in input function that assists user in entering the values.

# Cost price (in Rs)	Tax
# > 100000	15 %
# > 50000 and <= 100000	10%
# <= 50000	5%

# def total_price(number):
#     if number > 100000:
#         print(number + (number*15/100))
#     elif number > 50000 and number <= 100000:
#         print(number + (number *10/100))
#     elif number <= 50000:
#         print(number + (number*5/100))
    
# cost_price = int(input('Enter the Cost Price: '))
# total_price(cost_price)


# 4. A student needs to have an attendance of atleast 75% to be allowed to sit for the exams.
# Create a program to check if the student satisfies this attendance criteria to sit for the exams by taking 2 inputs from the user
# and display the necessary output message along with the attendance in percentage using the print function.

# Note : Make sure you enter the appropriate message in input function that assists user in entering the values.

# Hint : Take the user inputs for the following :

# Number of classes held
# Number of classes attended.

# def allowance(number1,number2):
#     if number1 and number2 < 0:
#         print('Enter the correct value')
#     elif ((number2/number1)*100) < 75:
#         print("You are fail!")
#     elif ((number2/number1)*100) >= 75:
#         print("You are passed!")

# classes_held = int(input('Enter the number of classes held: '))
# classes_attended = int(input('Enter the number of classes held: '))

# allowance(classes_held,classes_attended)


## Difficulty Level : Medium

# 1. Create a program that displays the wages of worker depending on their age, gender (‘M’, ‘F’) and 
# number of days they work accodring to the criteria mentioned in the table below:

# Note : Make sure you enter the appropriate message in input function that assists user in entering the values.

# Age Group	Gender	Daily Wages
# >= 18 and < 30	M	700
                  # F	750
# >= 30 and <= 40	M	800
                  # F	850

# def wages(age, gender):
#     if age >= 18 and age < 30:
#         if gender == "M":
#             print(700)
#         elif gender == 'F':
#             print(750)
#     elif age >= 30 and age <= 40:
#         if gender == "M":
#             print(800)
#         elif gender == 'F':
#             print(850)

# gender = input('Enter your gender (M or F): ')
# age = int(input("Enter your age: "))
# wages(age,gender)




# 2. Create a program to check if a given year is leap year or not.

# Note : Make sure you enter the appropriate message in input function that assists user in entering the values.

# Note : Google to check all the conditions for a year to be a leap year.

# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         leap = True
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False
#     return leap

# years = int(input("Enter the year: "))
# print(is_leap(years))



## Difficulty Level : Hard

# 1. Create a program that accepts the number of days from the user and calculates the charge for library according to the following table :

# Note : Make sure you enter the appropriate message in input function that assists user in entering the values.

# Number of Days	Cost / day
# Till 5 days	Rs 2 / day
# 6 to 10 days	Rs 3 / day
# 11 to 15 days	Rs 4 / day
# After 15 days	Rs 5 / day

# def library_charges(user):
#     if user < 0:
#         print("Enter valid number..")
#     elif user <=5 and user > 0:
#         print(user*2)
#     elif user == range(6,11):
#         print((5*2)+(user*3))
#     elif user == range(11,16):
#         print((5*2)+(5*3)+(user*4))
#     elif user > 15:
#         print((5*2)+(5*3)+(5*4)+(user*5))

# user = int(input("Enter the number of days: "))
# library_charges(user)



# 2. Create a program that accepts the electric units from user and calculates the bill according to the following rates:

# Note : Make sure you enter the appropriate message in input function that assists user in entering the values.

# Example :

# Number of Unit :550 = 100+200+250

# Total Bill : 0 +400+1250 = 1650

# Range of Units	Cost / unit
# First 100	           Free
# Next 200	        Rs 2 / unit
# Above 300	          Rs 5 / unit


# def electric_unit_calculator(units):
#     if units < 0:
#         print("Enter valid units.")
#     elif units in range(0,101):
#         print('Your donot have to pay bills, its Free!!')
#     elif units in range(101,301):
#         print((units-100)*2)
#     elif units > 300:
#         print((200*2)+((units-300)*5))

# units = int(input("Enter the units :"))
# electric_unit_calculator(units)