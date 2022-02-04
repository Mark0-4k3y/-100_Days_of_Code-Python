#This a treasure hunting application using nested list
import random

#First creating the rows for the map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

#Here I make the shuffling of the thumbs up emoji in each of the row
row1 = ["👍", "👎", "👎"]
row2 = ["👎", "👍", "👎"]
row3 = ["👎", "👎", "👍"]
random.shuffle(row1)
random.shuffle(row2)
random.shuffle(row3)
mapN = [row1, row2, row3]

#Now  I will take input from the user at which they want to try there luck!
position = input("Enter the position to find out whether the treasure is present or not: ")
verti = int(position[1]) - 1
hori = int(position[0]) - 1

#Now I will select the option based on the input of position
print(mapN[hori][verti], end=" ")
if mapN[hori][verti] == "👍":
    print("You got the treasure, Congratulations :) ")
else:
    print("Not found, Better luck next time :* ")



