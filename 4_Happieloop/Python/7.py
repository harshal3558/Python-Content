# Implement a Simple Word Count Program
user = input("Enter the word: ")
count = 0
for word in user:
    count+=1
print(f"Word count of {user} is {count}.")