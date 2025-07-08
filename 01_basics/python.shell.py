# >>> import first_file
# Aakash
# 4
# Nicee
# >>> first_file.printSome("YoYo")
# YoYo
# >>> first_file.print_one
# Traceback (most recent call last):
#   File "<python-input-15>", line 1, in <module>
#     first_file.print_one
# AttributeError: module 'first_file' has no attribute 'print_one'. Did you mean: 'printSome'?
# >>> import first_file
# >>> first_file.print_one
# Traceback (most recent call last):
#   File "<python-input-17>", line 1, in <module>
#     first_file.print_one
# AttributeError: module 'first_file' has no attribute 'print_one'. Did you mean: 'printSome'?
# >>> from importlib import reload
# >>> first_file.print_one
# Traceback (most recent call last):
#   File "<python-input-19>", line 1, in <module>
#     first_file.print_one
# AttributeError: module 'first_file' has no attribute 'print_one'. Did you mean: 'printSome'?
# >>> reload(first_file)
# Aakash
# 4
# Nicee
# <module 'first_file' from '/Users/aakashgaur/Documents/GitHub/pyhton/01_basics/first_file.py'>
# >>> first_file.print_one
# 'This is First'
# >>> first_file.print_two
# 'This is Second'
# >>> first_file.print_three
# 'This is Third'
# >>> 