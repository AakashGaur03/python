# >>> tea_varities = ["Black","Green","Oolong","White"]
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'White']
# >>> print(tea_varities[0])
# Black
# >>> print(tea_varities[-1])
# White
# >>> print(tea_varities[0:2])
# ['Black', 'Green']
# >>> print(tea_varities[1:3])
# ['Green', 'Oolong']
# >>> print(tea_varities[:2])
# ['Black', 'Green']
# >>> print(tea_varities[2:])
# ['Oolong', 'White']
# >>> tea_varities[3] = "Herbal"
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'Herbal']
# >>> print(tea_varities[1:2])
# ['Green']
# >>> tea_varities[1:2]="Lemon"
# >>> print(tea_varities)
# ['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
# >>> tea_varities = ["Black","Green","Oolong","White"]
# >>> print(tea_varities)
# ['Black', 'Green', 'Oolong', 'White']
# >>> tea_varities[1:2]=["Lemon"]
# >>> print(tea_varities)
# ['Black', 'Lemon', 'Oolong', 'White']
# >>> tea_varities[1:3]
# ['Lemon', 'Oolong']
# >>> tea_varities[1:3]=["Greem","Masala"]
# >>> print(tea_varities)
# ['Black', 'Greem', 'Masala', 'White']
# >>> tea_varities[1:1]
# []
# >>> tea_varities[1:1] = ["test","test"]
# >>> print(tea_varities)
# ['Black', 'test', 'test', 'Greem', 'Masala', 'White']
# >>> tea_varities[1:2]
# ['test']
# >>> tea_varities[1:3]
# ['test', 'test']
# >>> tea_varities[1:3]=[]
# >>> print(tea_varities)
# ['Black', 'Greem', 'Masala', 'White']
# >>> tea_varities.insert(0, "Tulsi")
# >>> print(tea_varities)
# ['Tulsi', 'Black', 'Greem', 'Masala', 'White']
# >>> for tea in tea_varities:
# ...     print(tea)
# ...     
# Tulsi
# Black
# Greem
# Masala
# White
# >>> for tea in tea_varities:
# ...     print(tea,end="-")
# ...     
# Tulsi-Black-Greem-Masala-White->>> 
# >>> tea_varities
# ['Tulsi', 'Black', 'Greem', 'Masala', 'White']
# >>> if "Oolong" in tea_varities:
# ...     print("Oolong Tea Present")
# ...     
# >>> tea_varities.append("Oolong")
# >>> if "Oolong" in tea_varities:
# ...     print("Oolong Tea Present")
# ...     
# Oolong Tea Present
# >>> tea_varities
# ['Tulsi', 'Black', 'Greem', 'Masala', 'White', 'Oolong']
# >>> tea_varities.pop()
# 'Oolong'
# >>> tea_varities
# ['Tulsi', 'Black', 'Greem', 'Masala', 'White']
# >>> tea_varities.remove("Greem")
# >>> tea_varities
# ['Tulsi', 'Black', 'Masala', 'White']
# >>> tea_varities.insert(1,"Green")
# >>> tea_varities
# ['Tulsi', 'Green', 'Black', 'Masala', 'White']
# >>> tea_varities_copy = tea_varities.copy()
# >>> tea_varities_copy.append("Lemon")
# >>> tea_varities
# ['Tulsi', 'Green', 'Black', 'Masala', 'White']
# >>> tea_varities_copy
# ['Tulsi', 'Green', 'Black', 'Masala', 'White', 'Lemon']
# >>> range(10)
# range(0, 10)
# >>> y = range(10)
# >>> print(y)
# range(0, 10)
# >>> squared_nums = [x**2 for x in range(10)]
# >>> squared_nums
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> cube_num = [y**3 for y in range(5)]
# >>> cube_num