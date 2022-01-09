#In this I will make a small, pizza ordering application
# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Small Pizza: $15
# Medium Pizza: $20
# Medium Pizza: $20
# Large Pizza: $25
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

#Greeting for the user:
print("Welcome to the most delicious pizza hub, Place your order!  ")

#Asking the user for pizza specifications
size = input("What the size of pizza you want? S or M or L\t")
add_pepperoni = input("Do you want pepperoni? Y or N\t")
extra_cheese = input("Do you want extra cheese? Y or N\t")
bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your total bill is: {bill}\nHave a nice day :)")