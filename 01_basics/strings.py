# >>> value = "one"
# >>> value
# 'one'
# >>> print(value)
# one
# >>> value = "new"
# >>> first_char = value[0]
# >>> print(first_char)
# n
# >>> value ="some random value"
# >>> print(value)
# some random value
# >>> slice_val = value[0:5]
# >>> print(slice_val)
# some 
# >>> value[-1]
# 'e'
# >>> num_list="0123456789"
# >>> num_list[:]
# '0123456789'
# >>> num_list[3:]
# '3456789'
# >>> num_list[:7]
# '0123456'
# >>> num_list[0:7]
# '0123456'
# >>> num_list[0:7:2]
# '0246'
# >>> num_list[0:7:3]
# '036'

# >>> val = "some random value"
# >>> print(val)
# some random value
# >>> print(val.lower())
# some random value
# >>> print(val.upper())
# SOME RANDOM VALUE
# >>> print(val)
# some random value
# >>> val = "      this is new     "
# >>> val
# '      this is new     '
# >>> print(val.strip())
# this is new
# >>> print(val.replace("some","NEW"))
#       this is new     
# >>> print(val.replace("this","replaced"))
#       replaced is new     
# >>> print(val)
#       this is new     
# >>> val = "one , two ,three "
# >>> print(val.split(", "))
# ['one ', 'two ,three ']
# >>> print(val.split())
# ['one', ',', 'two', ',three']
# >>> print(val.find(new))
# >>> val = "this is updated vals"
# >>> print(val.find("vals"))
# 16

# >>> print(val.find("Vals"))
# -1
# >>> val =" value is val that is val"
# >>> print(val.count("val"))
# 3
# >>> val_type ="Coffee"
# >>> quantity = 3
# >>> order = "I Ordered {} cups of "
# >>> order
# 'I Ordered {} cups of '
# >>> print(order.format(quantity,val_type))
# I Ordered 3 cups of 
# >>> order = "I Ordered {} cups of {}"
# >>> print(order.format(quantity,val_type))
# I Ordered 3 cups of Coffee
# >>> val_variety = ["hot","cold"]
# >>> val_variety
# ['hot', 'cold']
# >>> print("".join(val_variety))
# hotcold
# >>> print(" ".join(val_variety))
# hot cold
# >>> print(",".join(val_variety))
# hot,cold
# >>> val
# ' value is val that is val'
# >>> print(len(val))
# 25
# >>> for letter in val :
# ...     print(letter)
# ...     
 
# v
# a
# l
# u
# e
 
# i
# s
 
# v
# a
# l
 
# t
# h
# a
# t
 
# i
# s
 
# v
# a
# l

# >>> val = "Good\nboy"
# >>> val
# 'Good\nboy'
# >>> print(val)
# Good
# boy
# >>> val = r"good\nboy"
# >>> val
# 'good\\nboy'
# >>> print(val)
# good\nboy
# >>> val = c:\user\pwd
#   File "<python-input-48>", line 1
#     val = c:\user\pwd
#            ^
# SyntaxError: invalid syntax
# >>> val = "c:\user\pwd"
#   File "<python-input-49>", line 1
#     val = "c:\user\pwd"
#           ^^^^^^^^^^^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
# >>> val = r"c:\user\pwd"
# >>> print(val)
# c:\user\pwd
# >>> val = "c:\\user\\pwd"
# >>> print(val)
# c:\user\pwd
# >>> val = " sdfvsd sdf sdf this is some random asd fdsad"
# >>> print("random" in val)
# True
# >>> print("randomds" in val)
# False 