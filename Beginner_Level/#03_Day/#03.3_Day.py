# This is a roller coaster machine application in an amusement park

#First I will ask user to enter their height to check the allowance based on it:
height = int(input("Please enter your height in cm: "))

#If the height is greater than 120cm they are allowed on the ride.
if height >= 120:
    print("Welcome to the ride Sir/Ma'am :)")
    # Now I will ask the age to determine the price of the ticket:
    age = int(input("Please enter your age: "))
    bill = 0

    if age < 12:
        bill = 5
    elif age < 18:
        bill = 7
    else:
        bill = 12

    #Asking the user if they want photos or not
    wantPhotos = input("Do you want a photo taken? Y or N. ")
    if wantPhotos == 'Y':
        print(f"Your final bill Sir/Ma'am is ${bill+3}")
    else:
        print(f"You total bill Sir/Ma'am is ${bill}")
else:
    print("You are not allowed on the ride, please come back after some time :_")


