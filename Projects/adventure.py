print("You wake up in the morning and your bus is already here")
print()
answer1 = input("Do you want to eat breakfast and miss the bus, type 'a' OR skip breakfast, type 'b'?")
if answer1 == "a":
    answer2 = input("Do you want to walk to school, type 'c' or skip class, type 'd'?")
    if answer2 == "c":
        print("You get hit by your bus, unfortunately you pass away")
    if answer2 == "d":
        print("You go back to sleep")
if answer1 =='b':
    answer3 = input("Do you sit next to the popular girl, type 'e' or guy, type 'f'")
    if answer3 == 'e':
        print("You watch tik tok with her")
    if answer3 == 'f':
        print("he tells you a joke, and you laugh")