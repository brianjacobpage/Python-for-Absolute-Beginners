#!/usr/bin/env python3
import random

def my_rand_results():
    my_rand_results1 = random.choice([True, False])
    my_rand_results2 = random.choice([True, False])
    my_rand_results3 = random.choice([True, False])
    print(my_rand_results1, my_rand_results2, my_rand_results3)
    if my_rand_results1 == my_rand_results2 == my_rand_results3:
        return True
    else:
        return False
    #return my_rand_results1, my_rand_results2, my_rand_results3

how_many_times = int(input("How many times do you want me to do this ridiculous task: "))
for i in range(how_many_times):
    results = my_rand_results()
    print(results)