#This is the final project for the fifth day.
#In this project I have to make a password generator application

#Ascii Value ranges of
#   Letters -> Capital(A, Z) : 65-90
#              SmallCase(a, z) : 97-122
#   Numbers -> (0-9) : 48-57
#   Symbols -> 33-45

#Importing the random library for the random operation
import random

#Creating a list of numbers, letters and symbols
#Letters
letters = []
for letter in range(65, 123):

    #For ignoring the symbols between 90 and 97
    if letter in range(91, 97):
        continue
    letters.append(chr(letter))

#Numbers
numbers = []
for number in range(0, 10):
    numbers.append(number)

#Symbols
symbol = []
for sym in range(33, 46):
    symbol.append(chr(sym))

#Randomising the list so make this application more advanced.
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbol)


#Asking the user for their choices in generating the password
letterNum = int(input("How many letters do you want in your password? "))
numberNum = int(input("How many numbers do you want in your password? "))
symbolNum = int(input("How many symbol do you want in your password? "))

#Generating the password now:
password = []
for i in range (0, letterNum):
    password.append(random.choice(letters))
for i in range (0, numberNum):
    password.append(str(random.choice(numbers)))
for i in range (0, symbolNum):
    password.append(random.choice(symbol))


#Printing the final password but before that we will do a final randomisation
random.shuffle(password)
result = ""
for i in password:
    result += i
print(f"You password is: {result} ")

