# Python Turtle Challenge - www.101computing.net/python-turtle-challenge/
import turtle

myPen = turtle.Turtle()
myPen.shape("arrow")

myPen.color("red")
myPen.speed(10)


def drawingAngles(xFrom, yFrom, xTo, yTo):
    myPen.penup()
    myPen.goto(xFrom, yFrom)
    myPen.pendown()
    myPen.goto(xTo, yTo)


for i in range(0, 11):
    drawingAngles(0, (10 - i) * 20, i * 20, 0)
    drawingAngles((10 - i) * 20, 0, 0, i * (-20))
    drawingAngles(0, (10 - i) * (-20), i * (-20), 0)
    drawingAngles((10 - i) * (-20), 0, 0, i * 20)
turtle.done()



