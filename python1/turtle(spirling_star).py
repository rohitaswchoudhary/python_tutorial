import turtle 

spiral = turtle.Turtle()
spiral.speed(10)
spiral.pencolor("green")

for i in range(100):
    spiral.forward((i+6) * 10 )
    spiral.right(150)
    
turtle.done()