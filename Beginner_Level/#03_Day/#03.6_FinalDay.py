# This is the final project of the day 3rd

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

decision = input("You are standing in between this big jungle.\nThere are only two paths from here: Left and Right\nSelect one by enter 'L' for LEFT and 'R' for RIGHT ")
if decision == 'R':
    print("GAME OVER: You were encountered and attacked by the Lion......;* ")
else:
    decision = input(
        "\nYou came to the bank of the River which have lot's of alligator in it.\nYou want to 'WAIT' or 'SWIM'?!\nSelect one by enter 'W' for WAIT and 'S' for SWIM ")
    if decision == 'S':
        print(
            "You are attacked by the group of alligators and don't know but after attacking you the river water turn into red........;*")
    else:

        print("\nAfter waiting some times the river is cleared, alligators are gone and you safely crossed the river.")
        decision = input(
            "Now you have come to a very old house which is destructed very roughly.\nThere are three doors present here:\nRED\nBLUE\nGREEN\nSelect one by enter 'R' for RED door\n'B' for BLUE door\n'G' for GREEN door ")
        if decision == 'R':
            print("Great, you found the treasure.\nNow are the richest in your family ;)")
        elif decision == 'Blue':
            print(
                "GAME OVER: You were encountered and attacked by the spirits of the family members used to live in this house which was murder in searching of the treasure ......;* ")
        else:
            print(
                "GAME OVER: Greedy person there is no treasure present in this house, come again tomorrow for searching again......;* ")