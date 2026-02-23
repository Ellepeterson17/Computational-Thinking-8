import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",-100,-150)
s2 = create_sprite("puppy", 100, -150)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right,"Right")
window.onkeypress(move_left, "Left")


def move_up2():
    x = s2.xcor ()
    y = s2.ycor () + 10
    s2.goto (x,y)

def move_down2():
    x = s2.xcor ()
    y = s2.ycor () - 10
    s2.goto (x,y)

def move_left2():
    x = s2.xcor () -10
    y = s2.ycor ()
    s2.goto (x,y)

def move_right2():
    x = s2.xcor () + 10
    y = s2.ycor ()
    s2.goto (x,y)

window.onkeypress(move_up2, "w")
window.onkeypress(move_down2, "s")
window.onkeypress(move_left2, "a")
window.onkeypress(move_right2, "d")

# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

def draw():
    s1.pendown ()
window.onkeypress (draw, "c")

def stop_drawing():
    s1.penup ()
window.onkeyrelease(stop_drawing, "c")

def erase():
    s1.clear()
window.onkeypress(erase, "e")

def red_pen():
    s1.color("red")
window.onkeypress(red_pen, "r")

def green_pen():
    s1.color("green")
window.onkeypress(green_pen, "g")

def reset (x,y):
    s1.goto(x, y)
window.onscreenclick(reset)

# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()