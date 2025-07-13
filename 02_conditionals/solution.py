# Question 1
age = 18

if age<13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age<60:
    print("Adult")
else:
    print("Senior")
    
# Question 2

age = 22
day = "wednesday"

# if age is greater than 18 then price is 12 else 8
price = 12 if age>=18 else 8
if day == "wednesday":
    price = price - 2
    # price -=2

print(price)

# Question 3
score = 12

if score>=101:
    print("Please verify grade")
    exit()

if score>= 90:
    grade = 'A'
elif score>=80:
    grade="B"
elif score>=70:
    grade="C"
elif score>=60:
    grade="D"
else:
    grade="F"

print(grade)

# Question 4

fruit = "Banana"
color = "Brown"

if fruit == "Banana":
    if color == "Green":
        print("unRipe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")

# Question 5
order_size = "Large"
extra_shot = True

if extra_shot:
    coffee = order_size + " with Extra shot"
else :
    coffee = order_size + " coffee"
print(coffee)

# Question 6
# Note & and | are bitwise operation in python we use (and keyword) and (or keyword) 
year = 2002
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "Leap Year")
else:
    print(year, "is Not a Leap Year")