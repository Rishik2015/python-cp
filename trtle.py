# Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?

# import turtle
# turtle.Screen().bgcolor("orange")
# turtle.Screen().setup(300,400)
# polygon= turtle.Turtle()

# num_sides=int(input("enter the number of sides "))
# side_length=int(input("enter the side length "))
# angle= 360.0 / num_sides
# for i in range(num_sides):
#     polygon.forward(side_length)
#     polygon.right(angle)
# turtle.done()    

# import turtle
# turtle.Screen().bgcolor("skyblue")
# turtle.setup(400,300)
# w=turtle.Turtle()
# for i in range(3):
#     w.forward(80)
#     w.right(120)
# w.penup()  
# w.goto(0,-40)  
# w.pendown()
# for i in range(3):
#     w.forward(80)
#     w.left(120)
# turtle.done()    

import turtle
my_wn=turtle.Screen()
my_wn.bgcolor("sky blue")
my_wn.title("Turtle")
my_pen= turtle.Turtle()
size=0
while True:
    for i in range(4):
        my_pen.fd(size+1)
        my_pen.left(90)
        size = size - 5
    size = size + 1    