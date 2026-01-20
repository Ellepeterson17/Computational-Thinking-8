import turtle, time, random
from utils import *

# Section 1 - Variables

x1 =-250
y1 =155
x2 =-250
y2 =54
x3 =-250
y3 =-46
x4 =-250
y4 =-150


# Section 2 - Setup

set_background("Lap Pool (1)")
t1 = create_sprite("Salmon (1)",x1,y1)
t2 = create_sprite("dolphin (1)",x2,y2)
t3 = create_sprite("Crab (1)",x3,y3)
t4 = create_sprite("Squid (2)",x4,y4)


# # Section 3 - Racing

for i in range(36):
    x1 +=7
    x2 +=15
    x3 += 11
    x4 += random.randint (2,23)
# Salmon is the slowest at 7 speed, can't win
# Crab is 11 speed faster then the salmon but slower then the dolphin so it can't win 
# Dolphin is the most likely to win at 15 speed
# Squid could win by chance but is less likely then the dolphin

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner

if x1 >= x2 and x1 >= x3 and x1 >= x4:
     print("Salmon wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
   print("Dolphin wins!")
elif x3 >= x1 and x3 >= x2 and x3 >= x4:
    print ("Crab wins!")
elif x4 >= x1 and x4 >= x2 and x4 >= x3:
    print ("Squid wins!")


turtle.exitonclick()