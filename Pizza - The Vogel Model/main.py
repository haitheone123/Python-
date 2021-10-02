# The Pizzaiolo's Puzzle - www.101computing.net/the-pizzaiolos-puzzle/
import turtle
import math
from random import randint

myPen = turtle.Turtle()
myPen.tracer(0)
myPen.speed(0)
screen = turtle.Screen()
screen.bgcolor("#FFFFFF")
myPen.penup()
myPen.goto(0, 0)


def drawPizza(x, y, radius):
    myPen.penup()
    myPen.goto(x, y - radius)
    myPen.pendown()
    myPen.color("#f4c542")
    myPen.pensize(6)
    myPen.fillcolor("#c42513")
    myPen.begin_fill()
    myPen.circle(radius)
    myPen.end_fill()


def drawOlive(x, y, radius):
    myPen.pensize(1)
    myPen.penup()
    myPen.goto(x, y - radius)
    myPen.pendown()
    myPen.color("#000000")
    myPen.fillcolor("#000000")
    myPen.begin_fill()
    myPen.circle(radius)
    myPen.end_fill()


def drawSausage(x, y, radius):
    myPen.pensize(1)
    myPen.penup()
    myPen.goto(x, y - radius)
    myPen.pendown()
    myPen.color("yellow")
    myPen.fillcolor("yellow")
    myPen.begin_fill()
    myPen.circle(radius)
    myPen.end_fill()

# Draw the Pizza
drawPizza(0, 0, 180)

c = 18  # scaling factor
for n in range(80):
    # Generate Polar Coordinates using Vogel's Model
    r = c * (n ** 0.5)
    teta = n * 137.508
    # Convert polar coordinates to Cartesian coordinates using trigonometric formulas (SOHCAHTOA)
    x = r * math.cos(math.radians(teta))
    y = r * math.sin(math.radians(teta))

    drawOlive(x, y, 4)
    drawSausage(x,y,8)


myPen.hideturtle()
myPen.done()