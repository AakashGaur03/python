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