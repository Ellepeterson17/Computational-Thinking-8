# Section 1 - Your code
from utils import *
set_background("Coat_Of_Arms (1)")

s1 = create_sprite("flower", 150, 190)
s2 = create_sprite("puppy", -100, 50)
s3 = create_sprite("Irish_Flag", 0, 190)
s4 = create_sprite("Lax_Stick", -38, -50)
s5 = create_sprite("Koala (1)", 100, 50)
s6 = create_sprite("flower",-150, 190)
message1 = create_sprite("alien",-110,-185)
message1.color("black")
message1.write("Peterson",font = ("Arial", 38, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Your motto",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()