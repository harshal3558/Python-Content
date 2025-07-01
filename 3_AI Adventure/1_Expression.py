## Expressions Practice Questions

## Difficulty Level : Easy

# 1. Add parentheses to the following expression so that it evaluates to 0. 8 - 3 * 2 - 1 + 1

print((8-(3*2))-(1+1))
    

# 2. Implement Simple Interest Formula : S.I. = P × R × T

# P = 1500
# R = 9.5
# T = 20

# def simple_interest(P,R,T):
#     SI = P*R*T
#     return SI
# P = 1500
# R = 9.5
# T = 20
# print(f'Simple Interest of P = {P}, R = {R},T = {T} is',simple_interest(P,R,T))


# 3. Try to implement Compound Interest Formula : V = P(1+r/n)^nt

# P = 1500
# r = 0.043
# n = 4
# t = 6

# def compound_interest(P,r,n,t):
#     V = (P*(1+r/n)**n)*t
#     return V
# P = 1500
# r = 0.043
# n = 4
# t = 6
# print('The Compound Interest is:',compound_interest(P,r,n,t))



# 4. Implement Fahrenheit to Celsius conversion formula : F = ( C x 9 / 5 ) + 32

# C = 253

# def celsius(farenheit):
#     f = (C * 9/5) + 32
#     return f
# C = 25 
# print(f"The {C} Celsius to Farenheit is :",celsius(C))



## Difficulty Level : Medium

# 1. Create 2 variables and assign values like name and surname from the user. Then concatenate these 2 variables and display using print function.

# def con(name,surname):
#     print(f'MY name is {name}+{surname}')
# name = input("Enter your name: ")
# surname = input("Enter the surname: ")
# con(name,surname)


# 2. Create 2 variables and assign values like birth month and birth year from the user. Display these 2 variables and the length of these variables inside a single print function.

# def dis(birth_month,birth_year):
#     print(f"birth month = {birth_month}\nlength of birth month = {len(birth_month)}\nbirth year = {birth_year}\nlength of birth year = {str(birth_year) }")
# birth_month = input("Entet he birth month :")
# birth_year = input("Enter the birth year :")
# dis(birth_month,birth_year)



## Difficulty Level : Hard

# 1. Create 2 variables and assign values of user's favourite IPL team and any number between 1 - 10. Display the name of this favourite IPL team as many times as the number they pick from 1 - 10.

# Note : Pass the message in the input function for taking information from the user.

# def assign(team,number):
#     if number > 10:
#         print('Error')
#     return team * number
# team = input("Enter the name of your favorite IPL team: ")
# number = int(input("Enter the number between 1-10: "))
# print(assign(team,number))


# 2. Create 4 variables and take input from user for information like height, weight, age and a number from 1 - 10.
# Display the results of true division, floor division and exponentiation of height,
# weight and age with the number selected from 1 - 10 concatenated together inside a print function respectively.

# Note : Pass the message in the input function for taking information from the user. Hint : Concatenate string \n to display output on new line.

# def info(height,weight,age,number):
#     if number > 10:
#         print("Error")
    

# height = int(input("Enter the height: "))
# weight = int(input("Enter the weight:"))
# age = int(input("Enter the your age: "))
# number = int(input("Enter the number between 1-10: "))
# info(height,weight,age,number)