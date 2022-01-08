#In this I will make a project of calculating the tip

#Greeting on opening the application
print("Welcome to the tip calculator!")

#Asking for the total bill:
totalBill = float(input("What was the total bill? $"))

#Asking for what percentage of tip they want to give
tipPercen = int(input("How much tip would you like to give? 10, 12 or 15? "))

#Asking the number of persons to split the bill
pNum = int(input("How many people to split the bill? "))

#Calculating the tip and total bill
tip = totalBill*tipPercen/100
tipBill = totalBill+tip

#Calculating the amount of bill on each person
eachPerson = tipBill/pNum

#Printing the result for the bill
print("Each person should pay: ${0:.2f}".format(eachPerson))