import turtle
turtle.Screen().bgcolor("orange")
w=turtle.Screen()
w.setup(400,400)
turtle.title("My Drawings")

#triangle#
turtle.pencolor("black")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.end_fill()

turtle.penup()
turtle.goto(150,80)
turtle.pendown()

#square#

turtle.pencolor("black")
turtle.fillcolor("blue")
turtle.begin_fill()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.end_fill()

turtle.done()
