hawaii_points = 0
new_york_points = 0
alaska_points = 0

print ()
print ("Welcome to the vacation quiz!")
print ("-----------------------------")
print ()
print ()
answer1 = input("Do you prefer A beaches, B Cities, or C mountains?")
if answer1 == "A":
    hawaii_points += 1
elif answer1 == "B":
    new_york_points += 1
elif answer1 == "C":
    alaska_points += 1
print ()
print ()
answer2 = input ("Do you prefer A snow, B sun, or C rainy?")
if answer2 == "A":
    alaska_points += 2
elif answer2 =="B" or "C":
    hawaii_points += 2
print ()
print ()
answer3 = input ("When on vacation, do you prefer A shopping, B skiing, or C swimming?")
if answer3 == "A":
    new_york_points += 2
elif answer3 == "B":
    alaska_points += 2
    hawaii_points -= 1
    new_york_points -= 1
elif answer3 == "C":
    hawaii_points += 2
print ()
print ()
answer4 = input ("Do you prefer A cold weather, B hot weather, or C both?")
if answer4 == "A":
    new_york_points += 1
    alaska_points += 1
elif answer4 == "B":
    hawaii_points += 2
elif answer4 == "C":
    new_york_points += 1
print ()
print ()
answer5 = input ("Would you rather have A relaxing vacation, B detailed itinerary?")
if answer5 == "A":
    hawaii_points += 1
elif answer5 == "B":
    new_york_points += 2
    hawaii_points -= 1
print ()
print ()
answer6 = input ("Do you enjoy planning things?")
if answer6 == "yes" or "Yes":
    new_york_points += 1
if answer5 == "no" or "No":
    alaska_points += 2
    hawaii_points += 1
print ()
print ()
answer7 = input ("Do you enjoy spending time in nature?")
if answer7 == "Yes" or "yes":
    new_york_points -= 1
    hawaii_points += 1
    alaska_points +=1
elif answer7 == "no" or "No":
    new_york_points += 1
print ()
print ()
answer8 = input ("Would you rather A go to a luau, B see the northern lights, or C go to Times Square?")
if answer8 == "A":
    hawaii_points += 1
if answer8 == "B":
    alaska_points += 1
if answer8 == "C":
    new_york_points += 1
print ()
print ()
if hawaii_points >= alaska_points and hawaii_points >= new_york_points:
    print ("Your ideal vacation is to Hawaii!")
elif new_york_points >= alaska_points and new_york_points >= hawaii_points:
    print("Your ideal vacation would be to New York!")
elif alaska_points >= hawaii_points and alaska_points >= new_york_points:
    print ("Your ideal vacation would be to Alaska!")