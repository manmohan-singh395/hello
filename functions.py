# functions

# def greet():
#     print("Hello World")

# greet()

# # def welcome_user():
# #     print("Welcome to 4Achievers!")
# def welcome_user(Name):
#     print(f"Hello  {Name} , Welcome to 4Achievers!")

# welcome_user("Aman")

# multiplication

# def add_number(a,b):
#     return a * b

# print(add_number(12,67))


#senior devs find
years_of_exp = [2, 5, 8, 1, 12, 4, 7]
senior_devs =[]
for year in years_of_exp:
    if year > 5:
        senior_devs.append(year)
print(senior_devs)

# area calculator
# def calculate_area(length, width):
#     return length * width

# length = 10
# width = 5
# area = calculate_area(length, width)
# print(f"The area of the rectangle is: {area}")

# handle generae

# def generate_handle(name):
#     # return f"@{name.lower().replace(' ','_')}"

#      lower_name = name.lower()
#      nameF = lower_name.replace(" ", "_")
#      newUserName = f"@{nameF}"
#      return newUserName

# print(generate_handle("Ganesh Dutt"))

# sentence = input("enter a string:").lower()
# vowels = 'aeiou'
# v_count = c_count = 0
# for char in sentence:
#     if char.isalpha():
#         if char in vowels:
#            v_count += 1
#         else:
#             c_count += 1

# print(f"vowels:{v_count},constant:{c_count}") 
# 
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # Example usage
# num = int(input("Enter a number: "))
# print(f"Factorial of {num} is {factorial(num)}") 

def remove_duplicates(lst):
    return list(set(lst))


my_list = input("Enter elements separated by space: ").split()
my_list = [int(x) for x in my_list]
print("List after removing duplicates:", remove_duplicates(my_list))    