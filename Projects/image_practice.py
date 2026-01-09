# Section 1 - Your code
from utils import *
set_background("beach")

s1 = create_sprite("fish", 250, -130)
s2 = create_sprite("fish", 200, -170)
s2 = create_sprite ("fish", 160, -100)
s2 = create_sprite("shell", -80, -200)

message1 = create_sprite("alien",-200,200)
message1.color("black")
message1.write("The Beach",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()