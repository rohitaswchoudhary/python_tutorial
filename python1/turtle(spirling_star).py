import turtle 

spiral = turtle.Turtle()
spiral.speed(50)

for i in range(50):
    spiral.forward((i+5) * 10 )
    spiral.right(144)
    
turtle.done()