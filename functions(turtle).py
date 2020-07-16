import turtle

rohit= turtle.Turtle()



def square():
    rohit.forward(50)
    rohit.right(90) 

for i in range(4):
    rohit.forward(50)

    for j in range(2):
        rohit.forward(50)

        for k in range(2):
            rohit.forward(50)

            square()

rohit.left(60)
rohit.forward(50)
rohit.right(120)
rohit.forward(50)

turtle.done()




