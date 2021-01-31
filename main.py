import colorgram
from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()

screen.colormode(255)
rgb_colours = []
colours = colorgram.extract('image.jpg', 20)
# print(colours)
for colour in colours:
    rgb_colours.append((colour.rgb.r, colour.rgb.g, colour.rgb.b))
rgb_colours = list(rgb_colours)
# print(rgb_colours)
# print(random.choice(rgb_colours))

# timmy_the_turtle.dot(50, "red")
timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
for i in range(10):
    for j in range(10):
        timmy_the_turtle.dot(20, random.choice(rgb_colours))
        timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(90)     # Face up when 10 dots have been drawn in 1 line
    timmy_the_turtle.forward(50)        # Give a space of 50 between 2 rows
    timmy_the_turtle.setheading(180)    # Face the turtle in West direction to go back to the start of row
    timmy_the_turtle.forward(500)       # 10 dots * 50 spaces = 500 spaces to move in West to reach
                                        # the starting point
    timmy_the_turtle.setheading(0)      # Face again in East direction to start drawing

screen.exitonclick()