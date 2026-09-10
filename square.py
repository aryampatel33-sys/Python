import turtle
turtle.Screen().setup(333,333)
turtle.Screen().title("Square")
turtle.Screen().bgcolor("lavender")
pen = turtle.Turtle()
side = 4 
angle = 360/4
length = 50
for i in range(side+1):
    pen.forward(length)
    pen.right(angle)
turtle.done()