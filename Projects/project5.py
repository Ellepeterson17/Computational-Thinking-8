import turtle, math, time, random
from utils import *

# Goal: Try to stay in the dog bone as long as you can!
# Use the up, down, left, and right arrows to move the dog.
# Try to get a new high score every time. You can see your time in the top left corner.


# Section 1: Setup
sprite_list = []

s1 = create_sprite("dog_bone", 0, 0)
s2 = create_sprite("weiner_dog", 0, 0)
set_background("black_2.0")
Timer = 0
s3 = create_sprite("alien",-350, 250)
s3.hideturtle ()
# Section 2: Controls

def move_up():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x,y)
        
def move_down():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x,y)
    
def move_left():
    x = s2.xcor() - 10
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right(): 
    x = s2.xcor() + 10
    y = s2.ycor() 
    s2.goto(x,y)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right,"Right")
window.onkeypress(move_left, "Left")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    s3.color ("White")
    s3.clear ()
    s3.write(f"Timer: {Timer}",font=("Arial",20,"normal"))

    if i % 100 == 0:
        Timer += 1

    if i % 7 == 0:
        s1.right(random.randint(-10, 10))
        s1.forward(2)

        if s1.xcor() > 200:
            x = 200
            y = s1.ycor()
            s1.goto (x,y)

        # s1.left(random.randint(-10, 10))
        # s1.forward(2)

        if s1.xcor() < -200:
            x = -200
            y = s1.ycor()
            s1.goto (x,y)
        if s1.ycor() > 200:
            y = 200
            x = s1.xcor()
            s1.goto (x,y)
        if s1.ycor() < -200:
            y = -200
            x = s1.xcor()
            s1.goto (x,y)
        # y >= s1.ycor(250)
        # s1.left(random.randint(-10, 10))
        # s1.forward(2)
        # s1.up(random.randint(-10, 10))
        # s1.forward(2)
        # s1.down(random.randint(-10, 10))
        # s1.forward(2)
    
    
    
    
    



    if get_distance (s1, s2) > 80:
        break

    elif Timer >= 60:
        print ("You win!")
        break


    
    time.sleep(0.01)
    window.update()
    
	
print("Game Over")