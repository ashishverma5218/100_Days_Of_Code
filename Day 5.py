# sh = input("Enter heights ").split()
# for i in range(0, len(sh)):
#     sh[i] = int(sh[i])
# th = 0
# for h in sh:
#     th += h
# print(f"total height = {th}")
#
# nos = 0
# for s in sh:
#     nos += 1
# print(f"number of students = {nos}")
#
# avg_h = round(th/nos)
# print(f"average height = {avg_h}")


# ss = input("Enter scores ").split()
# for i in range(0, len(ss)):
#      ss[i] = int(ss[i])
# l1 = 0
# for i in ss:
#     if i > l1:
#         l1 = i
# print(l1)

# add 1 to 100

# a = 0
# for i in range(1,101):
#     a +=i
# print(a)


# add even number for given input
# num = int(input("Enter number "))
# sum = 0
# for i in range(2,num+1,2):
#     sum += i
# print(sum)

# num = int(input("Enter number "))
# sum = 0
# for i in range(1,num+1):
#     if i % 2 == 0:
#         sum+=i
# print(sum)


# Fizzbuzz
#
# for i in range(1,101):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print("Fizzbuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# password generator


import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

l1 = []

for i in range(1,nr_numbers + 1):
    l1.append(random.choice(letters))
for j in range(1,nr_numbers + 1):
    l1.append(random.choice(numbers))
for k in range(1,nr_numbers + 1):
    l1.append(random.choice(symbols))

random.shuffle(l1)

password = ""

for char in l1:
    password += char

print(f"Your Password is {password}")