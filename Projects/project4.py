import turtle, time, random
from utils import *

# Click space to make dogs appear on the screen.
# Click t when you have enough dogs to pay for the cost, this will give you a tennis ball.
# Get as many tennis balls as you can and get the highest score!


# Section 1 - setup
# Background
set_background("Meadow")

# Sprites

# Variables
dogs = 0
cost = 5
tennis_balls = 0
score = 0





# Section 2 - controls
# get_dog action
def get_dog():
    global dogs
    dogs += 1
    x = random.randint(-250, 250)
    y = random.randint (-100, 100)
    create_sprite ("puppy",x,y)

# Space key makes a dog appear
window.onkeypress(get_dog, "space")

# get_tennis_balls action
def get_tennis_balls():
    global dogs, cost, tennis_balls
    if dogs >= cost:
        cost = 2*cost
        tennis_balls += 1
        x = -395 + 70*tennis_balls
        y = -230
        create_sprite("Tennis_ball",x,y)

# t key makes a tennis ball appear
# t key will only work if there are more or equal dogs then the cost
window.onkeypress(get_tennis_balls, "t")


a1 = create_sprite("alien", -300, 170)
a2 = create_sprite("alien", 75, 200)
a1.hideturtle()
a2.hideturtle()


# Section 3 - game loop
window.listen()
for i in range(1000000000):
    

    a1.clear()
    a1.write(f"Dogs: {dogs}\nCost: {cost}\nTennis balls: {tennis_balls}", font=("Arial", 25, "normal"))
    score = tennis_balls
    a2.clear()
    a2.write(f"Your score is {score}!",font=("Arial", 25, "normal"))


    time.sleep(0.01)
    window.update()

