# Implement a Simple Guessing Game
import random
r = random.randint(0,9)
user = 0
while r != user:
    #r = random.randint(0,9)
    user = int(input("Enter the number between 0-9: "))
    if user == r:
        print(f"{r} is equal to { user}")
        break
    elif user < r:
        print(f"{r} is greater than {user} ")
    else:
        print(f"{r} is smaller than {user}")

