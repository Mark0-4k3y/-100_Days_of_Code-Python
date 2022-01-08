# In this we will see how to round a float number

# Here will take the numerator and then the denominator from the user
num = int(input("Enter the numerator: "))
deno = int(input("Enter the denominator: "))

# Here I will ask user to enter the number of digits they want to round off
precision = int(input("Enter the precision number: "))

# Here I will print the result by round it off using the round function
result = round(num/deno, precision)
if precision == 0:
    print("The number after the rounding off is: ", int(result))
else:
    print("The number after the rounding off is: ",result)

# Here I want to show the difference between the round function and the // operator
# // : Give the integer value after dividing which belong to it's ground value of result
# for example: 5/2=2.5 but after 5//2=2(Which is ground value of 2.5)
# Where the round function will give round(5/2)=2, round function is do rounding;
# Whereas the // function always gives the floor value.


print("Operation performed on 5/2 using different perspective\nThe simple divide operator", 5/3)
print("The simple returning integer operator", 5//3)
print("The round function gives: ", round(5/3))


# Python code to demonstrate precision
# initializing value
a = 3

# using "%" to print value till 2 decimal places
print("The value of number till 2 decimal place(using %) is : ", end="")
print('%.2f' % a)

# using format() to print value till 2 decimal places
print("The value of number till 2 decimal place(using format()) is : ", end="")
print("{0:.8f}".format(a))

# using round() to print value till 2 decimal places
print("The value of number till 2 decimal place(using round()) is : ", end="")
print(round(a, 2))


# By using the %.nf and format function we will add 0's after the decimal point in a value