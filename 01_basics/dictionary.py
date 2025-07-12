# >>> tea_types = {"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# >>> tea_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
# >>> tea_types["Masala"]
# 'Spicy'
# >>> tea_types.get("Ginger")
# 'Zesty'
# >>> tea_types.get("Gingery")
# >>> tea_types.get("ginger")
# >>> tea_types["Ginger"]
# 'Zesty'
# >>> tea_types["Gingery"]
# Traceback (most recent call last):
#   File "<python-input-7>", line 1, in <module>
#     tea_types["Gingery"]
#     ~~~~~~~~~^^^^^^^^^^^
# KeyError: 'Gingery'
# >>> tea_types["Green"]= "Fresh"
# >>> tea_types["Green"]
# 'Fresh'
# >>> tea_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
# >>> for tea in tea_types:
# ...     print(tea)
# ...     
# Masala
# Ginger
# Green
# >>> for tea in tea_types:
# ...     print(tea, tea_types[tea])
# ...     
# Masala Spicy
# Ginger Zesty
# Green Fresh
# >>> tea_types = {"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# >>> tea_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
# >>> tea_types["Masala"]
# >>> for key, value in tea_types.items():
# ...     print(key,value)
# ...     
# Masala Spicy
# Ginger Zesty
# Green Fresh
# >>> if "Masala" in tea_types:
# ...     print("Masala Present")
# ...     
# Masala Present
# >>> print(len(tea_types))
# 3
# >>> tea_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
# >>> tea_types["Earl Grey"]="Citrus"
# >>> tea_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
# >>> tea_types.pop("Ginger")
# 'Zesty'
# >>> tea_types
# {'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
# >>> tea_types.popitem()
# ('Earl Grey', 'Citrus')
# >>> tea_types
# {'Masala': 'Spicy', 'Green': 'Fresh'}
# >>> del tea_types["Green"]
# >>> tea_types
# {'Masala': 'Spicy'}
# >>> tea_types_copy = tea_types.copy()
# >>> tea_types_copy
# {'Masala': 'Spicy'}
# >>> tea_shop = {}
# >>> tea_shop = {
# ... }
# >>> tea_shop = {
# ... "chai":{"Masala":"Spicy","Ginger":"Zesty"},
# ... "Tea":{"Green":"Mild","Black":"Strong"},
# ... }
# >>> 
# >>> tea_shop
# {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
# >>> print(tea_shop)
# {'chai': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'Tea': {'Green': 'Mild', 'Black': 'Strong'}}
# >>> 
# >>> tea_shop["chai"]
# {'Masala': 'Spicy', 'Ginger': 'Zesty'}
# >>> tea_shop["chai"]["Ginger"]
# 'Zesty'
# >>> tea_shop["chai"]["Gingery"]

# >>> tea_types = {"Masala":"Spicy","Ginger":"Zesty","Green":"Mild"}
# >>> tea_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Mild'}
# >>> tea_types["Masala"]
# >>> for key, value in tea_types.items():
# ...     print(key,value)
# ...     
# Masala Spicy
# Ginger Zesty
# Green Fresh
# >>> if "Masala" in tea_types:
# ...     print("Masala Present")
# ...     
# Masala Present
# >>> print(len(tea_types))
# 3
# >>> tea_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
# >>> tea_types["Earl Grey"]="Citrus"
# >>> tea_types
# {'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
# >>> tea_types.pop("Ginger")
# 'Zesty'
# >>> tea_types
# {'Masala': 'Spicy', 'Green': 'Fresh', 'Earl Grey': 'Citrus'}
# >>> tea_types.popitem()
# ('Earl Grey', 'Citrus')
# >>> tea_types
# {'Masala': 'Spicy', 'Green': 'Fresh'}
# >>> del tea_types["Green"]
# >>> tea_types
# {'Masala': 'Spicy'}
# >>> tea_types_copy = tea_types.copy()
# >>> tea_types_copy
# {'Masala': 'Spicy'}
# >>> tea_shop = {}
# >>> tea_shop = {
# ... }
# >>> tea_shop = {
# ... "chai":{"Masala":"Spicy","Ginger","Zesty"},
# ... "Tea":{"Green":"Mild","Black","Strong"},
# ... }
# >>> squared_num = {x:x**2 for x in range(6)}
# >>> squared_num
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# >>> squared_num.clear()
# >>> squared_num
# {}
# >>> keys = ["Masala","Ginger","Lemon"]
# >>> keys
# ['Masala', 'Ginger', 'Lemon']
# >>> default_value = "Tasty"
# >>> new_dict = dict.fromkeys(keys,default_value)
# >>> new_dict
# {'Masala': 'Tasty', 'Ginger': 'Tasty', 'Lemon': 'Tasty'}
# >>> new_dict = dict.fromkeys(keys,keys)
# >>> new_dict
# {'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}