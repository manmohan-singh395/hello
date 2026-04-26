# string
#a = 'Man Mohan'
#print(a)

#b = "Man Mohan"
#print(b)

# c= '''india
# won
# the
# match'''
# print(c)

# slishing
# text ="pyton programming"
# print(text[0:6])
# print(text[:2])
# print(text[::3])
# print(text[::-1])

# concatenation

# a = "hello"
# b = "world"
# result = a +" "+ b
# print(result)

# name = "Ganesh ji"
# print((name+ "\n") *5)

#reverse a string
# text = 'pyton'
# print(text[::-1])

#vowel count in senence
# sentence = 'programing language'
# vowels = 'aeiou'
# count = 0

# for char in sentence:
#     if char in vowels:
#         count += 1

# print("vowels count:",count)

# palindrome check

# word = 'madam'
# if word == word[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#remove whitespace

# word = "pyton programmimg"
# print(word.strip())

# nested loop 
# row = 5
#  squre pattern
# for i in range (1,row+1):
#     for j in range (1,row+1):
#         print("*",end = "")
#     print()

# right angle trungle
# for i in range(1,row+1):
#     print("*" *i)

# multiplication table grid
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j, end="")
#     print()

#number pyramid pattern
# for i in range(1,row+1):
#     for j in range(i):
#         print(i,end="")
#     print()

# # prime number in range

# for num in range(2,50):
#     for i in range(2,num):
#         if num %i == 0:
#             break

#     else:
#         print(num)

# cordinate pairs

# for i in range(1,5):
#     for j in range(1,5):
#         print(f"({i},{j})",end =" ")
#     print()

# inverted triangle pyramid
# for i in range(row,0,-1):
#     print("*" *i)

# unique combination
# nums = [1,2,3]
# for i in nums:
#     for j in nums:
#         print(f"{i},{j}")

# sum of matrix

# A = [[1,2],[3,4]]
# B = [[1,2],[3,4]]
# for i in range(2):
#     for j in range(2):
#         print(A[i][j] + B[i][j] , end ="")
#     print()

# diamond pattern

# n = 5
# for i in range(n):
#     print(" "*(n-i-1) + "*" *(2*i+1))
# for i in range(n-2, -1, -1):
#     print(" "*(n-i-1)+"*"*(2*i+1))

# remove whitespace
# s = " hello world "
# print(s.strip())

# word counter
# sentence = "i love pyton coding"
# word = sentence.split(" ")
# print(len(word))

# capitilize words
# a= "aman manmohan"
# print(a.title())

# find and replace 
# a = "i like apples"
# print(a.replace("apple","banana"))

# anagrams check
# a = "silent"
# b = "listen"
# if sorted(a) == sorted(b):
#     print("anagrams")

# password validator
# password = "Ganesh123"
# if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit()  for  char in password ):
#     print("Valid password")
# else:
#     print("Invalid password")
