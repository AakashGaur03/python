print("Hello")
username= "Aaka"
print(username)



# >>> f = open("some.py")
# >>> f.readline()
# 'print("Hello")\n'
# >>> f.readline()
# 'username= "Aaka"\n'
# >>> f.readline()
# 'print(username)'
# >>> f.readline()
# ''
# >>> f.readline()
# ''
# >>> f = open("some.py")
# >>> f.__next__()
# 'print("Hello")\n'
# >>> f.__next__()
# 'username= "Aaka"\n'
# >>> f.__next__()
# 'print(username)'
# >>> f.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     f.__next__()
#     ~~~~~~~~~~^^
# StopIteration
# >>> for line in open("some.py"):
# ...     print(line)
# ... 
# print("Hello")

# username= "Aaka"

# print(username)

# >>> for line in open("some.py"):
# ...     print(line,end='')
# ... 
# print("Hello")
# username= "Aaka"
# print(username)>>> 

# >>> f =open("some.py")
# >>> while True:
# ...     line = f.readline()
# ...     if not line: break
# ...     print(line,end="")
# ... 
# print("Hello")
# username= "Aaka"
# print(username)

# >>> test = "aakash"
# >>> if not test:
# ...     print("Heu")
# ... 
# >>> test = ""
# >>> if not test:
# ...     print("Hey")
# ... 
# Hey
# >>> myList = [1,2,3,4]
# >>> I=iter(myList)
# >>> I
# <list_iterator object at 0x1026a1a20>
# >>> I.__next__()
# 1
# >>> I
# <list_iterator object at 0x1026a1a20>
# >>> I.__next__()
# 2
# >>> I.__next__()
# 3
# >>> I.__next__()
# 4
# >>> I.__next__()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     I.__next__()
#     ~~~~~~~~~~^^
# StopIteration
# >>> f= open("some.py")
# >>> iter(f) is f
# True
# >>> iter(f) is f.__iter__()
# True
# >>> myNewList = [1,2,3]
# >>> iter(myNewList)
# <list_iterator object at 0x102956f80>
# >>> iter(myNewList) is myNewList
# False
# >>> di = {'a':1,'b':2}
# >>> for key in di.keys():
# ...     print(key)
# ... 
# a
# b
# >>> some = iter(di)
# >>> some
# <dict_keyiterator object at 0x1029701d0>
# >>> some.__next__()
# 'a'
# >>> next(some)
# 'b'
# >>> next(some)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     next(some)
#     ~~~~^^^^^^
# StopIteration
# >>> 
# >>> range(0,5)
# range(0, 5)
# >>> R = range(0,5)
# >>> R
# range(0, 5)
# >>> I = iter(R)
# >>> next(I)
# 0
# >>> next(I)
# 1
# >>> next(I)
# 2
# >>> next(I)
# 3
# >>> next(I)
# 4
# >>> next(I)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     next(I)
#     ~~~~^^^
# StopIteration