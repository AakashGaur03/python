import time 

# Minimum Decorator

# func_name is a decorator factory (takes a function and returns a wrapped version).

# wrapper accepts any arguments (*args, **kwargs) — so it can decorate any function.

# It just calls the original function and returns the result.

# This decorator doesn't change behavior — it's just a wrapper that passes through.

def func_name(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        return result
    return wrapper


# Question 1
# Decorators are HOF of Javascript
def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_func(n):
    print("2")
    time.sleep(n)
    print("3")

# example_func(2)




# Question 2

def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key}={value}" for key,value in kwargs.items())
        print(f"Calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name,greeting="Hello"):
    print(f"{greeting}, {name}")

# hello()
# greet("Aak")
# greet("Aak","Good")
# greet("Aak",greeting="Good")

# , '.join(str(arg) Takes comma seperated value passed in function
# greet("Aak","Good")
# args_value = ', '.join(str(arg) for arg in args)


# Question 3

def cache(func):
    cache_value = {}
    #  when @cache is applied to long_running_func (i.e., at definition time), not during each function call. So it shows an empty dictionary.
    print(cache_value,"Cache Val")
    def wrapper(*args):
        if args in cache_value:
            print("Using cached result for", args)
            print(cache_value, "Cache Val")
            return cache_value[args]
        result =func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_func(a,b):
    time.sleep(4)
    return a+b

print(long_running_func(2,3))
print(long_running_func(2,3))
print(long_running_func(4,3))