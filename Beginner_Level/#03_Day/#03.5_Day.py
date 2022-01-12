# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the
# number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2-digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
# e.g.
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53
# Print: "Your score is 53."

#First I will take input from the users and then merge them in one word which will present in either upper case or lower case.
name1 = input("Enter you name Sir/Ma'am: ")
name2 = input("Enter their name: ")

#Upper function is used to convert the string to upper Case opposite of this can be done by the lower() function i.e, to lower case
name = (name1+name2).upper()

#In this I will use the count() function, which return the value of the letter present in the world.
digit1 = name.count('T') + name.count('R') + name.count('U') + name.count('E')
digit2 = name.count('L') + name.count('O') + name.count('V') + name.count('E')

#Now I will return the total percentage of the love and a statement
percentage = digit1 * 10 +digit2

if percentage < 10 or percentage > 90:
    print(f"Your score is {percentage}%, you go together like coke and mentos.")
elif 40 <= percentage <= 50:
    print(f"Your score is {percentage}%, you are alright together.")
else:
    print(f"Your score is {percentage}%.")






