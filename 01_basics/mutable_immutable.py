# >>> username = "Aakash"
# >>> username
# 'Aakash'
# >>> username = "Aaka"
# >>> username
# 'Aaka'
# >>> x =12
# >>> y=x
# >>> x
# 12
# >>> y
# 12
# >>> x=15
# >>> y
# 12
# >>> 

username = "Aakash"       # Reference of value is created that is of Aakash
username="Aaka"           # here Aakash is not updated it is present there only new reference of Aaka is created that's why immutable

# SO here when Aakash is not used or referenced anywhere python garbage collection automatically cleans it ut

x = 12       # reference of 12 is created and x is pointing at that
y = x         # y is also pointing at same reference of x that is 12
x = 15        # now reference of 15 is created and x is pointing at that and y is still pointing at 12 only


# // List is Mutable In first example refereing to same memory reference 
# // in Second when we are doing  p2=[1,2,3] then creating new memory reference
# >>> l1=[1,2,3]
# >>> l2=l1
# >>> l1
# [1, 2, 3]
# >>> l2
# [1, 2, 3]
# >>> l1[0]=44
# >>> l1
# [44, 2, 3]
# >>> l2
# [44, 2, 3]
# >>> p1=[1,2,3]
# >>> p2=p1
# >>> p2=[1,2,3]
# >>> p1[0]=55
# >>> p1
# [55, 2, 3]
# >>> p2
# [1, 2, 3]
# >>> 
# in easy what we can do is
# This gives us copy so different memory reference for both
# h1=[1,2,3]
# h2=h1[:]
# OR
# import copy
# h2=copy.copy(h1) // Single Level
# h2=copy.deepcopy(h1) // Nested Levels too


# >>> n = [1,2,3]
# ... m =n 
# 
# >>> m
# [1, 2, 3]
# >>> n
# [1, 2, 3]
# >>> m ==n     // Checks equality
# True
# >>> m is n    // Checks Memory Reference
# True
# >>> n = [1,2,3]
# >>> m==n
# True
# >>> m is n
# False