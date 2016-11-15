#Problem 8-4
#Name: Jessenia Lopez
#Date: November 10, 2013

##This program writes a function that uses turtle graphics to draw a petal.
##The function takes a turtle as its input parameter and draws a single petal.
##This program then draws a flower by repeatedly calling the function.
##The flower should have at least 10 petals.


import turtle
def main():
    turtle.Screen()
    turtle.title("Flower")
    turtle.color("purple")

    for i in range(0,11):
        turtle.left(i + 25)
        petal(turtle)

    turtle.exitonclick()

def petal(turtle):
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(25)
    turtle.right(115)
    turtle.forward(25)
    turtle.right(34)
    turtle.forward(100)

main()

    
