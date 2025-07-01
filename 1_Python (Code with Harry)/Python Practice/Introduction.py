def pr(self):
    print('Hello World')

def add(a,b):
    return a+b

def sqr_root(number):
    return number**1/2

def area_of_tri(number):
    return 1/2*(base*height)

def quad_eqn(a,b,c):
    import cmath
    # -b+-b^2 -2ac
    e1 = -b + (b**2) - (2*a*c)
    e2 = b - (b**2) - (2*a*c)
    return e1,e2

def swap(a,b):
    a,b == b,a
    return a,b

def generate_random(number):
    gene = random.randint(99)
    return gene

def k_m(n):
    miles = 0.62137119 * n
    return miles

def c_f(C):
    f = (3/16*c)+32
    return f

input = int(input('Enter the input number: '))
a = int(input('Enter the a number: '))
b = int(input('Enter the b number: '))
c = int(input('Enter the c number: '))
C = int(input('Enter the Celsius value: '))

if input = 1:
    print(pr(self))
elif input = 2:
    print(add())
elif input = 3:
    print(sqr_root)
elif input = 4:
    print(area_of_tri())
elif input = 5:
    print(quad_eqn())
elif input = 6:
    print(swap())
elif input = 7:
    print(generate_random())
elif input = 8:
    print(k_m())
else input = 9:
    print(c_f())