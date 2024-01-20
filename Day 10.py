# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("Leap year")
#             else:
#                 print("Not leap year")
#         else:
#             print("Leap year")
#     else:
#         print("Not leap year")
#
#
# # TODO: Add more code here 👇
# def days_in_month():
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and is_leap(year):
#         return 29
#     else:
#         return month_days[month - 1]
#
# # 🚨 Do NOT change any of the code below
# year = int(input())  # Enter a year
# month = int(input())  # Enter a month
# days = days_in_month()
# print(days)


def add(a,b):
    return a+b
def Sub(a,b):
    return a-b
def Mul(a,b):
    return a*b
def Div(a,b):
    return a/b

operation = {
    "+": add,
    "-": Sub,
    "*": Mul,
    "/": Div,
}
a = int(input())
b = int(input())
for symbol in operation:
    print(symbol)
os = input("choose one ")
cf = operation[os]
answer = cf(a,b)
print(f"{a} {cf} {b} = {answer}")