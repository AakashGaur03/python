# username = "Aakash"

# {

# }

# def test():
#     # print(username,"1") # Gives error UnboundLocalError
#     name ="John"
#     username ="Depp"
#     print(name)
#     print(username,"2")
# # print(name)
# print(username)
# test()
# print(username)

x = 99

# def func(y):
#     z = x+y
#     return z
# print(func(2))

# def func3():
#     global x  # overrides global variable
#     x = 88

# func3()
# print(x)

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()
# f1()
# Lexical Scope

def f1():
    x = 88
    def f2():
        print(x)
    return f2
refOfF2 = f1()
refOfF2()  # Closure Referecne of value of x is also present here


# Closure or Factory Functions
def someFunc(num):
    def actualFunc(x):
        return x ** num
    return actualFunc

calcute_square = someFunc(2)
calcute_cube = someFunc(3)
calcuteSome = someFunc(5)
print(calcuteSome)
res = calcuteSome(2)   # means 2 ** 5
print(res)

print(calcute_square(12))
print(calcute_cube(4))