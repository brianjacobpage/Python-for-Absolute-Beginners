#!/usr/bin/env python3
#Look at random.choice method to use a list of the operators
import random

def random_calc(a, b):
    operators = ["+", "-", "/", "*"]
    operator = (random.choice(operators))
    print(operator)
    if operator == "+":
        result = a + b
        return result
    elif operator == "-":
        result = a - b
        return result
    elif operator == "*":
        result = a * b
        return result
    else:
        result = a / b
        return result

num1 = int(input("Provide your first int: "))
num2 = int(input("Provide your second int: "))
print(random_calc(num1, num2))