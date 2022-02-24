#!/usr/bin/env python3
#Goal: generate two random letters and print results
#Unicode for alphabet is 65 thru 90
import random

def two_random_letters():
    rand_int1 = chr(random.randint(65, 90))
    rand_int2 = chr(random.randint(65, 90))
    return rand_int1, rand_int2

print(two_random_letters())