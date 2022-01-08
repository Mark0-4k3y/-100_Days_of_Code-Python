# In this I will make an application which shows life in weeks, days and months
#The concepts of making life determination app is acquired from: https://waitbutwhy.com/2014/05/life-weeks.html
# This will also help us to understand f-String in python

#First, I will take input as current age
age = round(float(input("Enter your current age Sir/Ma'am: ")))

#Then I will find out how much life he/she has remained:
#In this I assume that the average life of a human is 80years
remainAge = 80-age

#Now I will find remaining life in the days, weeks, and months
# 1 Year = 365 Days(exclude leap year)
# 1 Year = 52 Weeks
days = remainAge*365
weeks = remainAge*52
months = remainAge*12

#Now I will store the result in variable "datas" using f-String.
#f-String is uses to concatenate other data types(integer, float, boolean) with string without the need of type casting.
datas = f"You remaining life in the terms of\nDays: {days} \nWeeks: {weeks} \nMonths: {months} "
print(datas)

#Here our task or project is completed but to add some more functionality to it, I will add another section in this.
isPlenty = True
if age >= 70:
    isPlenty = False

print(f"Is you have plenty of life to live?! {isPlenty}")
