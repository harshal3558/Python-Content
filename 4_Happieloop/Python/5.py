# Create a Python Program to Check for Prime Numbers
number = int(input("Enter the number: "))
for i in range(2,number):
    if number%i ==0:
        print(number,"is not prime.")
else:
    print(number,'is prime')