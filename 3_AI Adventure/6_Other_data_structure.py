
# Other Data Structures Questions
# Difficulty Level : Easy


# Create a dictionary named student and it should contain your Name, Gender, Age & Programming language. After creating it add a new key Roll number and set its value as 43.



# Create a function to display how many times substring A has appeared in the string ABRACADABRA.

# Example :

# def match_string(string,substring):
#     ### your code here

# string = 'ABRACADABRA'
# substring = 'A'

# match_string(string,substring)
# >>> 5```



# Create a function that takes 2 dictionaries as arguments and returns the total bill after selling every fruit according to their rate specified.

# Example :

# def total_bill(first, second):
#     ### your code here

# stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
# prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}


# total_bill(stock, prices)
# >>> 117.0```



# Create a dictionary by assigning the keys from a list and its values from the user using input function.

# List :

# keys_list = [ "Name", "Birth Month", "Programming Language", "Salary" ]

# Example :

# def create_dict(keys_list):
#     ### your code here
#     sampleDict = {}

# keys_list = [ "Name", "Birth Month", "Programming Language", "Salary" ]

# create_dict(keys_list)
# >>>
# Difficulty Level : Medium




# Create a function that displays the unique elements present inside the dictionary in descending order in a single line.

# Example :

# def unique_elements(dictionary):
#     ### your code here
    
# marks = {"English": 78, "Maths": 89, "Science": 92, "History": 89, "Geography": 77, "Physics": 92, "Chemistry": 78}

# unique_elements(marks)
# >>> 92 89 78 77```



# Create a function that will take 1 argument as tuple of countries and display the number of vowels in the name of each country.

# Example :

# def count_vowels(countries):
#     ### your code here

# asian_countries = ('afghanistan', 'bangladesh', 'bhutan', 'china', 'india', 'iran', 'iraq', 'israel','japan')
# count_vowels(asian_countries)

# >>> afghanistan has 4 vowels.
#     bangladesh has 3 vowels.
#     bhutan has 2 vowels.
#     china has 2 vowels.
#     india has 3 vowels.
#     iran has 2 vowels.
#     iraq has 2 vowels.
#     israel has 3 vowels.
#     japan has 2 vowels.



# Difficulty Level : Hard
# Write a program that will find all the numbers between 1000 and 3000 (both included) such that each digit of the number is an even number and the numbers obtained should be printed in a comma - separated sequence on a single line.

# Note : Google search for join function of string datatype.

# def even_in_range():
#     ### your code here



# Create a function that will try to mimic the SUPEROVER scenario from Cricket. You have to create 2 dictionaries for 2 teams and each dictionary will contain the outcome of 6 balls bowled in the superover as key (i.e- run scored on that ball) and values of that dictionary will be as follows:

# 'W' : 0 runs

# 'R' : 1-6 runs

# The runs scored will be generated randomly using random module by using random.randint(0,6) and make sure that you are including the number 5 in dictionary deliberately even though there is no 5 runs in cricket. You also have to track the number of wickets fallen in that superover.

# Also make sure that your dictionary has 6 unique keys for every deliveries in a superover. The output of the function should be dictionaries of both the teams and scorecard along with the number of wickets fallen, by compnaring the scores of both the teams show which team has won in superover, as shown in the example below: Example :

# def superover():
#     ### your code here
    
# superover()
# >>> >>> Performance of Team1 : {0: 'W', 1: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'R'}
#     Performance of Team2 : {0: 'W', 1: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'R'}
#     Scorecard of Team1 : 19 / 1
#     Scorecard of Team2 : 19 / 1
#     Its a Draw!  
    
# >>> Performance of Team1 : {0: 'W', 1: 'R', 2: 'R', 4: 'R', 5: 'R', 6: 'R'}
#     Performance of Team2 : {0: 'W', 1: 'R', 2: 'R', 3: 'R', 4: 'R', 6: 'R'}
#     Scorecard of Team1 : 18 / 1
#     Scorecard of Team2 : 16 / 1
#     Team1 wins by 2 runs!
    
# >>> Performance of Team1 : {0: 'W', 1: 'R', 3: 'R', 4: 'R', 5: 'R', 6: 'R'}
#     Performance of Team2 : {0: 'W', 1: 'R', 2: 'R', 3: 'R', 4: 'R', 5: 'R'}
#     Scorecard of Team1 : 19 / 1
#     Scorecard of Team2 : 15 / 1
#     Team1 wins by 4 runs!
# Happy Learning!