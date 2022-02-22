#!/usr/bin/env python3

def int_comp(x: int) -> int:
    if (x) > -1:
        return True
    else:
        return False

u_int: int = int(input("Give me an int to compare: "))
result: bool = int_comp(u_int)
print(result)

if result == True:
    print("Your int is positive")
else:
    print("Your int is negative")