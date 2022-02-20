#In this day of programming I will make a FizzBuzz application
#Rules of the game are simple:
#   1.Your program should print each number from 1 to 100.
#   2.When number is divisible by 3, print "Fizz".
#   3.When the number is divisible by 5, print "Buzz".
#   4.When the number is divisible by both(3 & 5 ie. 15) print "FizzBuzz"

#I will start with a for loop
for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
