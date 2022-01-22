#In this practical application I will make an application, which will tell who have to pay the bill.
#It's like all members put there ATM card in the bowl and randomly one ATM card pick's up by waiter.
#Then, the person have to pay the bill for whom the card is belonged.
#Importing the random module
import random


# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
persons = names_string.split(", ")
print(persons)
#.................................................................................................
#Another long method to take input from the user as list:
#Create a list and take input for the usernames.
#persons = []
#Creating a loop which will take input
# while True:
#     name = input("Enter the name of the person or press 'S' for STOP this.")
#     if name == 'S' or name == 's' or name == ' ':
#         break
#     persons.append(name)
#.................................................................................................

#Now I will perform randomization on the list.
#The shuffle function will randomise the order of names present in the list than the original list.
random.shuffle(persons)

#Now I will randomly choose a number between the indexes
payBill = random.randint(0, len(persons)-1)
print(f"\nThe person who have to pay the bill is: {persons[payBill]}")

#And the simplest way to do is: by choice keyword, which will random pick the name from the list
print(f"The person who have to pay the bill is: {random.choice(persons)}")
