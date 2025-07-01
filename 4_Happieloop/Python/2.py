# Build a Simple Calculator

def addition(a,b):
    return 'addition: ',a+b
    
def subtraction(a,b):
    return "subtraction: ",a-b

def multiply(a,b):
    return "multiplication: ",a*b
    
def division(a,b):
    return "division: ",a/b

while True:
    print("Welcome to calculator!!")
    print("Enter '1' for addition.")
    print("Enter '2' for subtraction.")
    print("Enter '3' for multiplication.")
    print("Enter '4' for division.")
    print("Enter '5' for exit.")
    

    user = int(input("Enter the command number: "))
    if user in [1,2,3,4,0]:
        a = int(input("Enter the number: "))
        b = int(input("Enter the number: "))

        if user == 1:
            addition(a,b)
        elif user == 2:
            subtraction(a,b)
        elif user == 3:
            multiply(a,b)
        elif user == 4:
            division(a,b)
    elif user == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Input")

