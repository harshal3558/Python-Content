## Q. Define a Circle class to create a circle with radius r using the constructor.
#     Define an Area() method of the class which calculates the area fo the circle.
#     Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


# class Circle:

#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return (22/7) * self.radius **2
    
#     def perimeter(self):
#         return 2 * (22/7) * self.radius

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())




## Q. Define a Employee class with attributes role, dapartment & salary. This class also has a showDetails() method.
#     Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

  
# class Employee:

#     def __init__(self,role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role = ",self.role)
#         print("dept = ",self.dept)
#         print("salary = ",self.salary)

# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         # super().__init__("Engineer","IT","75,000")
#         super().__init__(self.role,self.dept,self.salary)

 
# # engg1 = Engineer("Elon Musk", 40)
# # engg1.showDetails()

# e1 = Employee("accountant","finance",'60,000')
# e1.showDetails()



## Q Create a class called Order which stores item & its price.
#    Use Dunder function __gt__() ,(greater than) to convey that: order1 > order2 if price of order1 > price of order2

# class Order:
#     def __init__(self,item, price):
#         self.item = item
#         self.price = price

#     def __gt__(self,odr2):
#         return self.price > odr2.price 


# odr1 = Order('chips',20)
# odr2 = Order("tea",15)

# print(odr1 > odr2) # True




## 1. Class and Object Creation
## Q1: Create a class called Car that has attributes like make, model, and year. Implement a method to display the car details.

# class Car:

#     def __init__(self,model,year,maker):
#         self.model = model
#         self.year = year
#         self.maker = maker

#     def showDetail(self):
#         print("Model of car is:",self.model)
#         print("Year of car is:",self.year)
#         print("Manufacturer of car is:",self.maker)

## if __name__ == "__main__":
##     car1 = Car("Toyota", "Camry", 2020)
##     car2 = Car("Honda", "Civic", 2019)

## car1.showDetails()
## print()
## car2.showDetails()

# c1=Car('tata','2011','tata')
# c1.showDetail()


## Q2: Define a class Book with attributes like title, author, and price. Create an instance of the class and display its attributes.

# class Book:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price

#     def showdetail(self):
#         print("Title of book is: ",self.title)
#         print("Author of Book is: ",self.author)
#         print("Price of the Book is: ",self.price)

# b1=Book("Hellen Killer","Helen Killer","45$")
# b1.showdetail()


### 2. Encapsulation

## Q3: Create a class BankAccount with private attributes for account_number and balance. Implement methods to deposit and withdraw money while ensuring that the balance cannot go negative.

# class BankAccount:

#     def __init__(self,account_number,initial_balance):
#         self.__account_number = account_number
#         self.__balance = initial_balance

#     def deposit(self,amount):
#         if amount > 0 :
#             self.__balance+=amount
#             print(f"Deposited: {amount}, New Balance: {self.__balance}")
    
#     def withdraw(self,amount):
#         if amount > 0:
#             if  self.__balance <= amount:
#                 self.balance -= amount
#                 print(f"Withdraw:{amount}, New balance: {self.__balance}")
#             else:
#                 print("Insufficient fund for this withdraw")
#         else:
#             print("Withdraw amount must be positive")
    
#     def showbalance(self):
#         return self.__balance
    
#     def show_account(self):
#         return self.__account_number

# if __name__ == "__main__":
#     account = BankAccount("12345678",5000)
#     account.deposit(1000)
#     account.withdraw(500)
#     account.withdraw(1200)
#     print(f"The final Banalnce is: {account.showbalance()}")



## Q4: Define a class Student with private attributes for name and grades. Implement getter and setter methods to access and modify these attributes securely.

# class Student:

#     def __init__(self,name,grades):
#         self.__name=name
#         self.__grades=grades

#     # Getter method for the student's name
#     @property
#     def name(self):
#         return self.__name
    
#     # Setter method for the student's name
#     @name.setter
#     def name(self,new_name):
#         self.__name=new_name

#     # Getter method for the student's grade
#     @property
#     def grades(self):
#         return self.__grades
    
#     # Setter method for the student's grade
#     @grades.setter
#     def grades(self,new_grades):
#         self.__grades=new_grades

#     def display_info(self):
#         print(f"Student Name:{self.__name}")
#         print(f"Grades:{self.__grades}")

# s1 = Student('yash','A')
# s1.display_info()



    


### 3. Inheritance

## Q5: Create a base class called Animal with a method speak(). Derive two classes, Dog and Cat, from it, overriding the speak() method to return "Woof" for dogs and "Meow" for cats.

# class Animal:

#     def speak(self):
#         raise NotImplementedError("Subclasses must implement this method")

# class Dog(Animal):

#     def speak(self):
#         return "Woof!"

# class Cat(Animal):

#     def speak(self):
#         return "Meow!"

# if __name__ == "__main__":
#     dog=Dog()
#     cat=Cat()

#     print(f"Dog says {dog.speak()}")
#     print(f"Cat says {cat.speak()}")


## Q6: Implement a class hierarchy where you have a base class Shape with derived classes like Circle and Rectangle. Each derived class should implement a method to calculate its area.

# class Shape:

#     def area(self):
#         pass

# class Circle(Shape):

#     def __init__(self,radius:int):
#         self.r = radius

#     def area(self):
#         return 3.14 * self.r**2
    
# class Rectangle(Shape):

#     def __init__(self,radius,height):
#         self.radius=radius
#         self.height=height

#     def area(self):
#         return self.radius*self.height
    
# if __name__ == "__main__":

#     circle = Circle(radius=5)
#     rectangle = Rectangle(radius=5, height=6)

#     print(f"Area of the circle: {circle.area():.2f}")
#     print(f"Area of the rectangle: {rectangle.area()}")



### 4. Polymorphism
## Q7: Create a function that takes an object of type Shape (from the previous question) and calls its area method. Demonstrate polymorphism by passing different shape objects to this function.

# class Shape:

#     def area(self):
#         raise NotImplementedError("Subclasses must implement this method")

# class Circle(Shape):

#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14*(self.radius**2)
    
# class Rectangle(Shape):

#     def __init__(self,height,width):
#         self.width=width
#         self.height=height

#     def area(self):
#         return self.height*self.width
    
# def calculate_area(shape:Shape) ->float:
#     return shape.area()

# if __name__ == "__main__":
#     circle=Circle(radius=5)
#     rectangle=Rectangle(height=6,width=4)

#     print(f"Area of the Circle: {calculate_area(circle):.2f}")
#     print(f"Area of rectangle: {calculate_area(rectangle)}")



## Q8: Define a class Employee with a method called work(). Create subclasses like Manager and Intern, overriding the work() method to provide different implementations.

# class Employee:

#     def work(self):
#         raise NotImplementedError("Subclasses must implement this method")

# class Manager(Employee):

#     def work(self):
#         return "Managing the team and overseeing projects."
    
# class Intern(Employee):

#     def work(self):
#         return "Assisting with tasks and learning from the team."
    
# if __name__ == "__main__":
#     manager=Manager()
#     intern=Intern()

#     print(f"Manager: {manager.work()}")
#     print(f"Intern: {intern.work()}")


### 5. Abstraction

## Q9: Create an abstract base class called Vehicle with an abstract method called start_engine(). Implement concrete classes like Car and Motorcycle that provide specific implementations of the abstract method.

# from abc import ABC, abstractmethod

# class Vehicle:

#     @abstractmethod
#     def start_engine(self):
#         pass
    
# class Car(Vehicle):

#     def start_engine(self):
#         print("Car engine started.")


# class Motorcycle(Vehicle):

#     def start_engine(self):
#         print("Motorcycle engine started.")

# car = Car()
# car.start_engine()

# motorcycle = Motorcycle()
# motorcycle.start_engine()

## Q10: Design an abstract class called Appliance with methods like turn_on() and turn_off(). Implement subclasses such as WashingMachine and Refrigerator, providing specific functionality for each appliance.

# from abc import ABC,abstractmethod

# class Appliance:

#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def trun_off(self):
#         pass

# class WashingMachine(Appliance):

#     def turn_on(self):
#         print("Washing machine is on")
    
#     def turn_off(self):
#         print("Washing machine is off")
    
# class Refrigerator(Appliance):

#     def turn_on(self):
#         print("Refrigerator is on")
    
#     def turn_off(self):
#         print("Refrigerator is off")

# washing_machine = WashingMachine()
# washing_machine.turn_on()
# washing_machine.turn_off()

# refrigerator = Refrigerator()
# refrigerator.turn_on()
# refrigerator.turn_off()



### 6. Composition

## Q11: Create a class called Library that contains a list of books (instances of the Book class). Implement methods to add, remove, and display books in the library.

# class Book:

#     def __init__(self,title,author,publication_year):
#         self.title=title
#         self.author=author
#         self.publication_year=publication_year

#     def __str__(self):
#         return f"'{self.title}' by {self.author} ({self.publication_year})"

# class Library:

#     def __init__(self,name):
#         self.name = name
#         self.books = []

#     def add_book(self,book):
#         self.books.append(book)
#         print(f"Book '{book.title}' added in the library.")

#     def remove_book(self,title):
#         for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 print(f"Book '{title}' removed from the library")
#                 return
#             print(f"Book '{title}' not found in the library.")

#     def display_books(self):

#         if not self.books:
#             print("No books in the library.")
#             return
#         for book in self.books:
#             print(book)

# if __name__ == "__main__":
#     my_library = Library("My Personal Library")

#     # Create instances of Book
#     book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
#     book2 = Book("1984", "George Orwell", 1949)
#     book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

#     # Add books to the library
#     my_library.add_book(book1)
#     my_library.add_book(book2)
#     my_library.add_book(book3)

#     # Display all books in the library
#     my_library.display_books()

#     # Remove a book from the library
#     my_library.remove_book("1984")

#     # Display all books after removal
#     my_library.display_books()



## Q12: Define a class called Person that has an attribute for an address (another class). Show how composition can be used to represent this relationship.

# class Address:

#     def __init__(self,street,city,state,zip_code):
#         self.street = street
#         self.city = city
#         self.state = state
#         self.zip_code = zip_code

#     def __str__(self):
#         return f"{self.street}, {self.city}, {self.state}, {self.zip_code}"

# class Person:

#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address

#     def __str__(self):
#         return f"{self.name}, {self.age} year old, livesat {self.address}"

# if __name__ == "__main__":
#     # Creaete an address
#     home_address = Address("123 Main St","New York","CA","1234")

#     # Create a person with the address
#     person = Person("John Cena",55,home_address)

#     print(person)



### 7. Real-world Scenario

## Q13: Model a simple online shopping system with classes like Product, Cart, and Order. Implement methods to add products to the cart, calculate total price, and place an order.

class Product:

    def __init__(self,item,price):
        self.item = item
        self.price = price

class Cart:

    def __init__(self):
        self.basket = []

class Order:
    
    def __init__(self):
        pass

    def remove(self,item):
        self.item = item
        if self.item() not in self.basket():
            print(f"{self.item} not in Cart")
        else:
            self.item()-=self.basket()
            print(f"{self.item} removed from {self.basket}")

    


## Q14: Design a simple banking system where you have classes for different account types (e.g., SavingsAccount, CheckingAccount) that inherit from a base class Account. Include methods for depositing, withdrawing, and checking balances.



### 8. Exception Handling in OOP

## Q15: Modify your BankAccount class (from question Q3) to raise exceptions for invalid operations (like withdrawing more than the balance). Handle these exceptions gracefully in your main program.