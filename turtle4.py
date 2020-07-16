import turtle 

painter = turtle.Turtle()
painter.speed(40)

painter.pencolor("blue")

for i in range(51):
    painter.forward(100)
    painter.left(123) # Let's go counterclockwise this time 

painter.penup()
painter.forward(200)
painter.pendown()

painter.pensize(1)
painter.pencolor("red")
for i in range(200):
    painter.forward(200)
    painter.left(123)
    
painter.hideturtle()
turtle.done()