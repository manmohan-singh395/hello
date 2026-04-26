# num = int(input("enter a number:"))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num,"is not prime")
#             break
#     else:
#         print(num,"is prime")

numbers = list(map(int,input("enter numbers seperasted by space: ").split()))
min_num = max_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num
    elif num > max_num:
        max_num = num
print("smallest:",min_num,"largest:",max_num)
