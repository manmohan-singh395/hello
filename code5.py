# for i in range(start, end(n-1))
"""for i in range(1,5):
    print(i)
"""
"""for i in range(1,11):
    print(f"apple number {i} washed")
"""
#while condition
"""data= False
recharge = 0

while data == False:
    recharge+=10
    print(f"recharge done {recharge}")

    if recharge == 250:
        data = True
print("data")
"""
# battery charge

"""battery = 67

while battery < 100:
    battery +=1
    print(f"charging... current battery: {battery}%")
print("battery full")
"""
# table generator

"""for i in range(1,11):
    print(f"5 X{i}={5*i}")
"""
# sum of natural numbers

"""sum = 0
for i in range(1,101):
    sum += i
    print(f"sum :",sum)
"""
# vowel count

"""str ="Man Mohan"
vowels = 'aeiouAEIOU'
count = 0

for char in str:
    if char in vowels:
        count = count + 1
"""
# reverse pattern

"""for i in range(10,0,-1):
    print(i)
"""
# user unput exist

"""while True:("enter word:")
if word == "stop":
    break
print("you typed:",word)
"""
# factorial number

"""n = int(input("enter number:"))
fact = 1
i = 1
while i <= n:
    fact *= input
    i += 1
    print("factorial:",fact)
"""
# possword alert
"""correct = input("correct possword:")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pswd = input("enter password:")
    if pswd == correct:
        print("assess granted")
        break
    attempts += 1
    if attempts == max_attempts:
        print("assess denies")
"""
# digit sum

"""n = int(input("enter a number:"))
total = 0
while n > 0:
    total += n % 10
    n //= 10
print("digit sum:",total)
"""
# even number only

"""i = 2
while i <= 20:
    print(i)
    i += 2
"""
# mixed logic question(for & while with if-else)

#1. Fizzbuzz classic

"""for i in range(1,51):
    if i %15 == 0:
        print("Fizzbuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
i += 1
"""
# prime number checker

n = int(input("Enter a number: "))
if n>1:
    for i in range(2,n):
        if n%i == 0:
            print("Not Prime")
            break
        else:
            print("Prime")
    else:
        print("Not Prime")

# Login System

"""correct = input("Enter Correct password: ")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pswd = input("password: ")
    if pswd == correct:
        print("Welcome")
        break
    attempts += 1
    if attempts == max_attempts:
        print("Access Denies")
   """

# positive sum only

"""numbers =[1,2,-3,-5,6]
positive_sum = 0

for num in numbers:
    if num > 0:
        positive_sum += num

print("sum of positives:", positive_sum)
"""



