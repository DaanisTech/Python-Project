name = input ("Enter Your name: ")
print("Welcome", name, "to this adventure!..")

answer =input ("you are on dirty road, it has come to an end and you can go left or right . which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if answer == "walk":
        print("You walked for a many miles, ran out of water and you lost the game.")

    elif answer == "swim":
        print("You swam across and were eaten by an alligator.")
    else:
        print("Not a valid option. You lose.")


elif answer == "right":
    answer = input("You come to bridge, it looks wobbly, do you want cross it or head back(cross/back)?").lower()

    if answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes  / No)?").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN!..")
        elif answer =="No":
            print("You ignore the stranger and they are offended. YOU LOSE!..")
        else:
            print("Not a valid option. You lose.")

    elif answer == "back":
        print("You go back and lose.")
    else:
        print("Not a valid option. You lose.")       
else:
    print("Not a valid option. You lose.")

print("Thank you for trying!..")

