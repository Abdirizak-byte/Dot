from graphics import *

def main():


    w = GraphWin("Dice",160,100)
    w.setBackground("Green")
    Rec = Rectangle(Point(70,70), Point(20,20))
    Rec.setFill("Red")
    Rec.draw(w)

    Recc = Rectangle(Point(140, 70), Point (90,20))
    Recc.setFill("Red")
    Recc.draw(w)




    for z in range (7):
        g = w.getMouse()
        x=g.getX()
        y=g.getY()
 
        center = Point(x,y)
        side1 = Circle(center, 5)
        side1.setFill("White")
        side1.draw(w)
        x= g.getX()
        y=g.getY()

    w.getMouse()
    w.close()
 


main()
