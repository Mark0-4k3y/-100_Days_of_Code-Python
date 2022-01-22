# In this I will make a Heads or Tails application
# First I will import random module

import random

# Make a variable which will store the coin face value:
#   1 = Heads
#   2 = Tails
coinFace = random.randint(0, 2)

# Now based upon the value I will print the result
print("It's a: ")
if coinFace == 1:
    print("Head")
else:
    print("Tail")
