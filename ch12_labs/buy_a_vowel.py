#!/usr/bin/env python3
import random

def is_a_vowel(a):
    uni_vowels = [65, 69, 73, 79, 85, 89]
    vowel = None
    convert_unicode = ord(a)
    for i in uni_vowels:
        if i == convert_unicode:
            vowel = True
    print(convert_unicode)
    return vowel

#user input version
print("\nThis is the user portion of the script")
print("__________________________________________\n")
u_char = input("Give me your alphabetic character: ").upper()
vowel_result = is_a_vowel(u_char)
if vowel_result == True:
    print("that is a vowel")
else:
    print("that is not a vowel")

#automatic computer
print("\nThis is the automated computer portion of the script")
print("__________________________________________\n")
computer_char = random.randint(65, 90)
computer_char_chr = chr(computer_char)
print("I choose " + computer_char_chr)
computer_vowel_result = is_a_vowel(chr(computer_char))
if computer_vowel_result == True:
    print("that is a vowel")
else:
    print("that is not a vowel")