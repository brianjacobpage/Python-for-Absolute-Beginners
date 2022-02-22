#!/usr/bin/env python3

from random import randint

#Remember that in python a function can be the input/argument for a higher level function, hence, you can call the random int within the print function
#otherwise we have to declare die and use it as a varible call in the print function
#die = randint(1, 6)

print("The outcome of the die is " + str(randint(1, 6)))