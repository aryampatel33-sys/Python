import turtle
turtle.Screen().setup(333,333)
turtle.Screen().title("Star")
turtle.Screen().bgcolor("orange")
pen = turtle.Turtle()
side = 3
angle = 360/3
length = 50
for i in range(side+1):
    pen.forward(length)
    pen.right(angle)
pen.penup()
pen.goto(25,15)
pen.pendown()
for i in range(side+1):
    pen.forward(length)
    pen.left(angle)
turtle.done()