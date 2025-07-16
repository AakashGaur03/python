# Question 1

def square(num):
    print(num **2)

res = square(4)
print(res)
def square2(num):
    return num **2
squareVal  = square2(4)
print(squareVal)

# Question 2

def sum_two_num(num1,num2):
    return num1+num2
print(sum_two_num(7,8))

def poly_multiply(p1,p2):
    return p1*p2
print(poly_multiply(5,8))
print(poly_multiply("g",20))
print(poly_multiply(4,"h"))

# Question 4
import math
def circle_stats(radius):
    area = math.pi * radius **2
    circumfrence = 2 * math.pi * radius
    return area ,circumfrence
    
a,c = circle_stats(3)
print("Area : ",round(a,2))
print("Circumfrence : ",round(c,4))

# Question 5
def greet_user(name = "Guest"):
    return "Hello, "+ name + "!"
print(greet_user("Aakash"))
print(greet_user())

# Question 6 
# Lambda (Anonymous Function) That has no Name

cube = lambda x: x ** 3
add = lambda x,y: x+y

print(cube(3))
print(cube(4))
print(add(4,12))

# Question 7
# *args predefined * is must we can use anything in place of args
def sum_all(*args):
    print(*args)
    print(args)
    for i in args:
        print("Mul 2 : ",i*2)
    return sum(args)

print(sum_all(1,23))
print(sum_all(1,23,56,65))
print(sum_all(1,23,5,6,32))

# Question 8
def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_kwargs(age = "27",name="Guest")
print_kwargs(name="Guest",age = "27")
print_kwargs(name="Guest")
print_kwargs(age="27")
print_kwargs(height="185")

# Question 9
def even_generator(limit):
    for i in range(2,limit+1,2):
        print(i)

even_generator(10)
def even_generator_with_return(limit):
    li=[]
    for i in range(2,limit+1,2):
       li.append(i)
    return li

print(even_generator_with_return(10))


# yield turns a function into a generator.

# Instead of returning all values at once, it pauses and resumes with each call (e.g., in a for loop).

# It is memory efficient — especially for large sequences — because it generates one value at a time.
def even_generator_with_yield(limit):
    li=[]
    for i in range(2,limit+1,2):
       yield i

for num in even_generator_with_yield(10):
    print(num)

# Question 10
def factorial_num(number):
    if number == 1: return 1
    return number * factorial_num(number-1)
print(factorial_num(6))