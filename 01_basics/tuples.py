# Same as List but basic differnece is Tuples are Immutable and List are Mutable
# >>> tea_types = ("Black","Green","Oolong")
# >>> tea_types
# ('Black', 'Green', 'Oolong')
# >>> tea_types[0]
# 'Black'
# >>> tea_types[-1]
# 'Oolong'
# >>> tea_types[1:2]
# ('Green',)
# >>> tea_types[1:]
# ('Green', 'Oolong')
# >>> tea_types[0] = "Lemon"
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     tea_types[0] = "Lemon"
#     ~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# >>> len(tea_types)
# 3
# >>> more_tea = ("Herbal","Lemon")
# >>> all_tea = more_tea + tea_types
# >>> all_tea
# ('Herbal', 'Lemon', 'Black', 'Green', 'Oolong')
# >>> if "Green" in all_tea:
# ...     print("Available")
# ...     
# Available
# >>> more_tea = ("Herbal","Green","Hebal")
# >>> more_tea.count("Herbal")
# 1
# >>> more_tea = ("Herbal","Green","Herbal")
# >>> more_tea.count("Herbal")
# 2
# >>> more_tea.count("Herb")
# 0
# >>> (black,green,Oolong) = tea_types
# >>> black
# 'Black'
# >>> green
# 'Green'
# >>> oolong
# Traceback (most recent call last):
#   File "<python-input-20>", line 1, in <module>
#     oolong
# NameError: name 'oolong' is not defined. Did you mean: 'Oolong'?
# >>> Oolong
# 'Oolong'
# >>> type(tea_types)
# <class 'tuple'>
# >>> type(green)
# <class 'str'>
# >>> some = ("",(1,2,3),"")
# >>> some
# ('', (1, 2, 3), '')
# >>> 