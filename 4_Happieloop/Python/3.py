# Create a Python Program to Generate Fibonacci Sequence

a1 = 0
a2 = 1
count = 0
series = []

user = int(input("Enter the number: "))

for i in range(user):
    a1,a2 = a2,a1+a2
    print(a1)
'''    
def Fibonacci(a1,a2):
    for i in range(user):
        a1,a2 = a2,a1+a2
        print(a1)
user = int(input("Enter the number: "))
Fibonacci(0,1)'''