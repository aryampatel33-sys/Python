import turtle
turtle.Screen().setup(333,333)
turtle.Screen().bgcolor("lightblue")
turtle.Screen().title("Pentagon")
pen = turtle.Turtle()
sides = 5
angle = 360/5
length = 50
for i in range(sides+1):
    pen.forward(length)
    pen.right(angle)
turtle.done()