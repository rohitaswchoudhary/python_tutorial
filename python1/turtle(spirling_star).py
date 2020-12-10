import turtle 

spiral = turtle.Turtle()
spiral.speed(10)

for i in range(50):
    spiral.forward((i+6) * 10 )
    spiral.right(150)
    
turtle.done()