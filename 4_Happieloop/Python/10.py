#  Create a Python Program to Convert Temperature
print("Enter the Temperature: \n 1.Celsius to Farenheit. \n 2.Farenheit to Celsius.")
user = int(input("Enter the number: "))
temp = int(input("Enter the temperature: "))
if user == 1:
    print(((9/5)*temp)+32,"C")
elif user == 2:
    print(((temp - 32) * 5/9),"F")
