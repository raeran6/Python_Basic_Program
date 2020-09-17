import random
lst = ["s","w","g"]
total_change = 10
no_of_chance = 0
human_point = 0
computer_point = 0

print("welcome to Snake_____Water_____Gun  game")
print("Please Enter\n s for snake\n w for water\n g for gun")
while no_of_chance < total_change:
    _input = input("enter your choice  ")
    _rand = random.choice(lst)
    if _input == _rand :
        print("its a tie \n Both Have 0 points")
    # if user enter s
    elif _input == "s" and   _rand == "w":
        print("You won")
        human_point = human_point + 1
    elif _input == "s" and _rand == "g":
        print(" Computer won")
        computer_point = computer_point + 1
    # if user enter w
    elif _input == "w" and _rand == "g":
        print(" Human  won")
        human_point = human_point + 1
    elif _input == "w" and _rand == "s":
        print(" Computer won")
        computer_point = computer_point + 1
    # if user enter g
    elif _input == "g" and _rand == "s":
        print(" Human  won")
        human_point = human_point + 1
    elif _input == "g" and _rand == "w":
        print(" Computer won")
        computer_point = computer_point + 1
    else:
        print("wrong choice entered")
    no_of_chance = no_of_chance + 1


if computer_point > human_point:
    print(f"computer wins {computer_point} ")
else:
    print(f"Human wins {human_point}")
