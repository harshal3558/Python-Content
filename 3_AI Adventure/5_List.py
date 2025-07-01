## Lists Practice Questions

## Difficulty Level : Easy

# 1. Create a function that will reverse a given list.

# Example :

# def reverse_list(numbers):
#     ### your code here
    
# list1 = [8, 6, 4, 2, 0]
# reverse_list(list1)

# >>> [0, 2, 4, 6, 8]

# def reverse_list(numbers):
#     return numbers[::-1]

# list1 = [8,6,4,2,0]
# print(reverse_list(list1))


# 2. Create a function that will display the square of every element of the list provided as an argument.

# Example :

# def square_list(list_numbers):
#     ### your code here

# list2 = [1, 2, 3, 4, 5]
# square_list(list2)
# >>> 1
#     4
#     9
#     16
#     25


# def square_list(list_numbers):
#     for i in list_numbers:
#         print(i**2)

# list2 = [1,2,3,4,5]
# square_list(list2)



# 3. Create a function that will take list of fruits and a new_fruit as 2 arguments.
# Add the new_fruit into the list of fruits and display the updated list. Also, try adding the new_fruit at the index position 2.

# Example :

# def to_append(fruits, new_fruit):
#     ### your code here

# fruits = ['banana', 'orange', 'mango', 'lemon']
# new_fruit = 'blueberry'

# to_append(fruits, new_fruit)

# >>> ['banana', 'orange', 'mango', 'lemon', 'blueberry']

# to_append(fruits, new_fruit)

# >>> ['banana', 'orange','blueberry' ,'mango', 'lemon',]

# def to_append(fruits, new_fruit):
#     ### your code here
#     fruits.append(new_fruit)
#     return fruits

# fruits = ['banana', 'orange', 'mango', 'lemon']
# new_fruit = 'blueberry'

# print(to_append(fruits, new_fruit))


# def to_append(fruits, new_fruit):
#     ### your code here
#     fruits.insert(2,new_fruit)
#     return fruits


# fruits = ['banana', 'orange', 'mango', 'lemon']
# new_fruit = 'blueberry'

# print(to_append(fruits, new_fruit))


# 4. Create a function that will take a list as an argument and return an updated list after removing empty strings from the list.
# list3 = ["Vivek", "", "Ankur", "aiadventures", "", "Pranav"].

# Example :

# def remove_spaces(list_names):
#     ### your code here

# list3 = ["Vivek", "", "Ankur", "aiadventures", "", "Pranav"]
# remove_spaces(list3)

# >>> ['Vivek', 'Ankur', 'aiadventures', 'Pranav']


# def remove_spaces(list_names):
#     ### your code here
#     for i in list_names:
#         if i == "":
#             list_names.remove("")
#     return list_names


# list3 = ["Vivek", "", "Ankur", "aiadventures", "", "Pranav"]
# print(remove_spaces(list3))



## Difficulty Level : Medium

# 1. Create a function that takes 2 lists as arguments and it iterates over both lists simultaneously such that output 
# should display items in original order from 1st list and elements from 2nd list in reverse order.

# Note : Please give attention to the output as it doesn't include [] brackets.

# Example :

# def reverse_list(first, second):
#     ### your code here

# list4 = [10, 20, 30, 40]
# list5 = [100, 200, 300, 400]

# reverse_list(list4, list5)
# >>> 10 20 30 40 400 300 200 100


# def reverse_list(first, second):
#     ## your code here
#     new_list = []
#     for l1 in first:
#         new_list.append(l1)
#     for l2 in second:
#         new_list.append(l2)
#     print(new_list)

# list4 = [10, 20, 30, 40]
# list5 = [100, 200, 300, 400][::-1]
# reverse_list(list4,list5)


# 2. Create a function that takes 2 lists as arguments and returns a new single list by performing the string replication 
# between the elements of the lists. The elements should be selected in original order from the 1st list and in reverse order from the 2nd list.

# Example :

# def multiply_elements(first, second):
#     ### your code here

# list4 = ['Ai', 'Adventures', 'Python', 'ML']
# list5 = [1, 2, 3, 4]

# reverse_list(list4, list5)
# >>> ['AiAiAiAi', 'AdventuresAdventuresAdventures', 'PythonPython','ML']



# def multiply_elements(first, second):
#     result = []
#     for i in range(len(first)):
#         # Multiply the string by the corresponding integer
#         result.append(first[i] * second[i])
#     return result

# list4 = ['Ai', 'Adventures', 'Python', 'ML']
# list5 = [1, 2, 3, 4][::-1]

# # Call the function with the two lists
# print(multiply_elements(list4, list5))




# def multiply_elements(first, second):
#     ### your code here
#     for l1,l2 in zip(first,second):
#         print(l1*l2)

# list4 = ['Ai', 'Adventures', 'Python', 'ML']
# list5 = [1, 2, 3, 4][::-1]
# multiply_elements(list4,list5)



 

## Difficulty Level : Hard

# 1. We're using lists to record people that attended our party and in the order they arrive in. For example, the following list represents a party 
# with 7 guests, in which Adela showed up first and Ford was the last to arrive:

# party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

# A guest is considered fashionably late if they arrived after at least half of the party's guests. However, they must not be the very last guest (that's taking it too far).
# In the above example, Mona and Gilbert are the only guests who were fashionably late.

# Create a function which takes a list of party attendees as well as a person as arguments and displays whether that person is fashionably late or not.

# Example :

# def fashionably_late(arrivals, name):
#     ### your code here

# party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
# fashionably_late(party_attendees, 'Mona')
# >>> True
# fashionably_late(party_attendees, 'Ford')
# >>> False

def fashionably_late(arrivals, name):
    ### your code here
    fashion = False
    for i in range(len(arrivals)):
        if i >= len(arrivals)/2:
            fashion = True
        elif i == len(arrivals):
            fashion = False
        else:
            fashion = False
        print(fashion)

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
fashionably_late(party_attendees, 'Mona')




# 2. Create a function that takes 2 lists as arguments. The function should create a new list that contains alternate elements of both the lists and replaces the string elements of the new list with its own length.

# Note : Use loops to update the empty lists.

# Example :

# def list_operations(first, second):
#     ### your code here

# first = ['Ai', 'Adventures', 'Python']
# second = [10, 20, 30]
# list_operations(first, second):
# >>> 
# Elements of the 1st List :  ['Ai', 'Adventures', 'Python']
# Elements of the 2nd List :  [10, 20, 30]
# List with alternate elements from the above 2 lists :  ['Ai', 10, 'Adventures', 20, 'Python', 30]
# Final output list :  [2, 10, 10, 20, 6, 30]
    
# first = ['Jan', 'February', 'March', 72]
# second = [10, 20, 30, 'April']
# list_operations(first, second):
# >>> 
# Elements of the 1st List :  ['Jan', 'February', 'March', 72]
# Elements of the 2nd List :  [10, 20, 30, 'April']
# List with alternate elements from the above 2 lists :  ['Jan', 10, 'February', 20, 'March', 30, 72, 'April']
# Final output list :  [3, 10, 8, 20, 5, 30, 72, 5]
