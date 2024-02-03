import random
from turtle import Turtle ,Screen
screen = Screen()
#
# def move_f():
#     t.forward(10)
# def move_b():
#     t.backward(10)
# def move_r():
#     t.right(10)
# def move_l():
#     t.left(10)
# def clear():
#     t.clear()
#     t.penup()
#     t.home()
#     t.pendown()
#
# screen.onkey(move_f, "d")
# screen.onkey(move_b, "s")
# screen.onkey(move_r, "e")
# screen.onkey(move_l, "x")
# screen.onkey(clear, "c")

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
cor = [-100,-60,-20,20,60,100]
all_turtles = []
for i in range(0,6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-230, y=cor[i])
    all_turtles.append(t)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"you won {win_color} is winner")
            else:
                print(f"you loose {win_color} is winner")

        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
screen.listen()
screen.exitonclick()