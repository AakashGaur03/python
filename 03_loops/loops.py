numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

# Question 1
positive_number_count = 0
for num in numbers:
    if(num>0):
        positive_number_count+=1
print(positive_number_count)

# Question 2
numberTillN = 10
sum = 0
for someNum in range(1,numberTillN+1):
    if(someNum % 2 == 0):
        sum=sum+someNum
print(sum)

# Question 3
numberForTable = 6
for num in range(1,11):
    if num == 5:
        continue
    print(numberForTable, "X" , num, "=" ,numberForTable*num)

# Question 4
input_str = "Python"
reverse_str= ""

for char in input_str:
    reverse_str = char + reverse_str
    # reverse_str = reverse_str + char
print(reverse_str)

# Question 5
input_str = "teeterabcdedf"

for char in input_str:
    print(char)
    if input_str.count(char) ==1:
        print("First Non Repeting Char is : ",char)
        break

# Question 6
factorial_number = 6
res = 1
while(factorial_number>1):
    res *= factorial_number
    factorial_number-=1
print(res)

# Question 7
while True:
    number = int(input("Enter value btw 1 and 10 : "))
    if 1 <= number <= 10:
        print("Correct")
        break
    else:
        print("Invalid Number")

# Question 8

prime_or_not = 29
isPrime = True
if prime_or_not>1:
    for i in range(2,prime_or_not):
        if (prime_or_not % i) == 0:
            isPrime = False
            print("Not Prime")
            break
print(isPrime)

# Question 9

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ",item)
        break
    unique_item.add(item)

# Question 10

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attemps :",attempts + 1 ,"-wait time", wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1