#Even and odd

# num = int(input("Enter a number"))
# if num % 2 == 0:
#     print("Even Number !")
# else:
#     print("Odd Number !")


#BMI


# w = float(input("Enter your weight in kg : "))
# h = float(input("Enter your height in cm : "))
# bmi = w/((h*h)/10000)
# print(bmi)
# if bmi <= 18.5:
#     print("Under weight")
# elif (bmi >= 18.5) and (bmi <= 25):
#     print("Normal Weight")
# elif (bmi >= 25) and (bmi <= 30):
#     print("Slightly Overweight")
# elif(bmi >= 30) and (bmi <= 35):
#     print("Obese")
# else:
#     print("Clinically Obese")


#Leap year
#In the Gregorian calendar, three conditions are used to identify leap years:
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year,
# unless: The year is also evenly divisible by 400.

# year = int(input("Enter Year "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


#pizza bill generate

# bill = 0
# p = input("We have three type of pizza what type of pizza you want - Small(S) , Medium(M) , Large(L) - ").lower()
# pi = input("You want pepperoni (Y/N) ").lower()
# c = input("You want extra cheese (Y/N) ").lower()
#
# if p == 's':
#     bill += 15
# elif p == 'm':
#     bill += 20
# elif p == 'l':
#     bill += 25
#
# if pi == 'y':
#     if p == 's':
#         bill += 2
#     else:
#         bill += 3
#
# if c == 'y':
#     bill += 1
#
# print(f"Your final bill is ${bill}")



# Love calculater


# name1 = input("Enter Your Name ")
# name2 = input("Enter Your Partner Name ")
# cn = name1+name2
# lc = cn.lower()
#
# t = lc.count("t")
# r = lc.count("r")
# u = lc.count("u")
# e = lc.count("e")
# first_digit = t + r + u + e
#
# l = lc.count("l")
# o = lc.count("o")
# v = lc.count("v")
# e = lc.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
# if (score >= 10) or (score <= 90):
#     print(f"Your score is {score} you are like coke and mentos ")
# elif (score >= 40) or (score <= 50):
#     print(f"Your score is {score} you are like alright together ")
# else:
#     print(f"Your score is{score}")


# Treasure island


print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("welcome to Treasure Island your mission is to find the treasure ")
path = input("Here is two path what you want to take (left or right) ").lower()
if (path == 'left') or (path == 'l'):
    river = input("Here is a river you want to wait for boat or swim (wait or swim) ").lower()
    if (river == 'wait') or (river == 'w'):
        door = input("Here is three door which you want to open (Red , Green , Yellow ) ").lower()
        if (door == 'yellow') or (door == 'y'):
            print("You Win This is your Treasure !")
        elif (door == 'red') or (door == 'r'):
            print("There is fire Game Over !")
        elif (door == 'green') or (door == 'g'):
            print("There is Snake Game Over !")
        else:
            print("Invalid Input !")
    else:
        print("Crocodile eat you Game Over !")
else:
    print("Here is a Lion Game Over !")
