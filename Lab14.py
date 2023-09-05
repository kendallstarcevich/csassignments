#author: Kendall Starcevich
#description: lab #14
from graphics import *

"""width = 640
height = 480
#create a window
win = GraphWin("Lab 14", width, height)

p = Point(320, 240)
p.draw(win)
p.move(100, 100)
p.setOutline("white")

circ = Circle(p,50)
circ.setOutline("white")
circ.draw(win)"""

"""win = GraphWin("Window's title", 1000, 1000)
hello = Text(Point(500, 500), "Hello, world!")
hello.draw(win)
hello.setSize(32) #sizes from 5 to 36 are legal
hello.setFace("courier")
hello.setTextColor("blue")
hello.move(0,100)
hello.setText("Text #1")


text2=Text(Point(200,250), "Text #2")
text2.draw(win)
text2.setFace("courier")
text2.setTextColor("yellow")
text2.setSize(15)"""

#section 4
"""
win = GraphWin("Hello", 400, 400)

#draw a green-filled circle with center (100, 200) and radius 50
circ = Circle(Point(300, 270), 50)
circ.setFill("green")
circ.draw(win)


#draw a rectangle with opposite corners at (10, 50) and (145, 280)
rect = Rectangle(Point(10, 60), Point(145, 280))
rect.draw(win)"""

#Exerise #3
"""
win = GraphWin("Hello", 400, 400)

#draw a green-filled circle with center (100, 200) and radius 50
circ = Circle(Point(200, 200), 100)
circ.setFill("yellow")
circ.draw(win)

left_eye=Circle(Point(150, 150), 15)
left_eye.setFill("black")
left_eye.draw(win)

right_eye=Circle(Point(250, 150), 15)
right_eye.setFill("black")
right_eye.draw(win)

mouth=Circle(Point(200, 230), 50)
mouth.setFill("black")
mouth.draw(win)

rect = Rectangle(Point(200, 180), Point(250, 230))
rect.setFill("yellow")
rect.setOutline("yellow")
rect.draw(win)

rect2 = Rectangle(Point(150, 180), Point(200, 230))
rect2.setFill("yellow")
rect2.setOutline("yellow")
rect2.draw(win)"""
#Exercise #4
"""import random
from graphics import *
win = GraphWin("Random Circles", 400, 400)
circ_num=int(input("How many circles would you like?"))
for x in range(circ_num):
    

#a random color
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = color_rgb(r,g,b)

#a random location
    x = random.randint(0,350)
    y = random.randint(0,350)

#a random radius
    radius = random.randint(10,50)

#a random circle
    circ = Circle(Point(x,y), radius)
    circ.setFill(color)
    circ.draw(win)
    """
#Section 6, exercise #5

"""import random
from graphics import *
win = GraphWin("Random Rectangles", 400, 400)
rect_num=int(input("How many rectangles would you like?"))
for x in range(rect_num):
    

#a random color
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = color_rgb(r,g,b)

#a random location
    x1 = random.randint(0,350)
    y1 = random.randint(0,350)
    
    x2 = random.randint(0,350)
    y2 = random.randint(0,350)



#a random circle
    rect = Rectangle(Point(x1,y1), Point(x2,y2))
    rect.setFill(color)
    rect.draw(win)
    """








