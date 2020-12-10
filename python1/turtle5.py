import turtle 

ninja = turtle.Turtle()

ninja.speed(255)
ninja.shape("turtle")


for i in range(180):

    ninja.pencolor('yellow')
    ninja.forward(100)
    ninja.pencolor('orange')
    ninja.forward(100)
    ninja.right(30)
    ninja.pencolor('red')
    ninja.forward(30)
    ninja.left(60)
    ninja.pencolor('dark red')
    ninja.forward(60)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()