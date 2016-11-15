#Problem 7-4
#Name: Jessenia Lopez
#Date: November 3, 2013

##This program changes colors depending where the user clicks on the window.
##If the user clicks on the left side, my initials (JL) appears in green.
##If the user clicks on the right side, my initials (JL) appears in red.
##This program allows the user to click 5 times before ending
##the program and closing the window. 

from graphics import *

def side(jl):
    w = jl.getWidth()
    x = jl.getMouse()
    y = x.getX()

    if y < w/2:
        return "l"
    if y > w/2:
        return "r"

def initial(jl):
    color = "black"
    jl.getMouse()
    
    p1 = Point(65,70)
    p2 = Point(155,70)
    l1 = Line(p1,p2)
    l1.setOutline(color)
    l1.draw(jl)

    p3 = Point(110,70)
    p4 = Point(110,150)
    l2 = Line(p3,p4)
    l2.setOutline(color)
    l2.draw(jl)

    p5 = Point(65,150)
    l3 = Line(p4,p5)
    l3.setOutline(color)
    l3.draw(jl)

    p6 = Point(65,130)
    l4 = Line(p5,p6)
    l4.setOutline(color)
    l4.draw(jl)

    p7 = Point(170,70)
    p8 = Point(170,150)
    l5 = Line(p7,p8)
    l5.setOutline(color)
    l5.draw(jl)

    p9 = Point(230,150)
    l6 = Line(p8,p9)
    l6.setOutline(color)
    l6.draw(jl)

    p10 = Point(230,130)
    l7 = Line(p9,p10)
    l7.setOutline(color)
    l7.draw(jl)

    c = side(jl)
    if c == "l":
        color = "green"
    if c == "r":
        color = "red"
    l1.undraw()
    l1.setOutline(color)
    l1.draw(jl)
    l2.undraw()
    l2.setOutline(color)
    l2.draw(jl)
    l3.undraw()
    l3.setOutline(color)
    l3.draw(jl)
    l4.undraw()
    l4.setOutline(color)
    l4.draw(jl)
    l5.undraw()
    l5.setOutline(color)
    l5.draw(jl)
    l6.undraw()
    l6.setOutline(color)
    l6.draw(jl)
    l7.undraw()
    l7.setOutline(color)
    l7.draw(jl)

def main():
    a = GraphWin("Jessenia Lopez's Initials", 290, 220)

    initial(a)
    initial(a)

    a.getMouse()
    a.close()
main()
