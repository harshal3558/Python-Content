# Multiple Inheritance

class A:
    varA = "welcome to calss A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)