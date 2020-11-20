from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    t = Turtle(shape="turtle");
    t.color(colors[i])
    t.penup()
    t.goto(x=-280, y=y_positions[i])
    all_turtles.append(t)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won, winner is {winning_color}!")
            else:
                print(f"You lost, winner is {winning_color}")

        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()