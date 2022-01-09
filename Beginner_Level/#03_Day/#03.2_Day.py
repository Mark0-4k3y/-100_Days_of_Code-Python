# In this, I will make an application which determine whether the given year is leap or not
# For the information leap year is that year which has 366 days in it.

#Asking the use for enter the value of year
year = int(input("Enter the year, you wanna find whether it is leap or not?:  "))


# To determine whether a year is a leap year, follow these steps:

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).
isLeap = True

if year % 4 == 0:
    # If the year is evenly divisible by 4, check with 100. Otherwise, go to else statement.
    if year % 100 == 0:
        # If the year is evenly divisible by 100, check with. Otherwise, go to else of 100 if statement.
        if year % 400 == 0:
            # If the year is evenly divisible by 400, isLeap = True. Otherwise, false.
            isLeap = True
        else:
            isLeap = False
    else:
        isLeap = True
else:
    isLeap = False


print(f"Is the year {year} leap year?: {isLeap}")