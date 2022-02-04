#This is the final project of Day4 in which I will make a Rock, Paper and Scissors game.
#In this first I will give choice to the user to select the option between rock paper and scissors.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Here making a loop so can user play at max they want to.
isloop = True
while isloop:
    choice = input("\nWhat do you choose?\n0 for Rock\n1 for Paper\n2 for Scissor\n'E' for end the game\n")
    if choice == '0':
        yourChoice = rock
    elif choice == '1':
        yourChoice = paper
    elif choice == '2':
        yourChoice = scissors
    else:
        break

    listt = [rock, paper, scissors, rock, scissors, scissors]
    computerChoice = random.choice(listt)

    print("You chose:\n",yourChoice)
    print("\nComputer chose:\n", computerChoice)

    if yourChoice == computerChoice:
        print("Match Draw")
    elif yourChoice == paper and computerChoice == rock:
        print("You won")
    elif yourChoice == rock and computerChoice == scissors:
        print("You won")
    elif yourChoice == scissors and computerChoice == paper:
        print("You won")
    else:
        print("You lose")


