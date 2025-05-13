'''
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20, . . . ,100.

✅ Features:

Simulates 1000 experiments for each group size.
Uses random birthdays between day 0 and 364 (ignores leap years for simplicity).
Calculates the probability of at least one shared birthday.
Tests the paradox for values of n = 5 to 100 in steps of 5.
'''

import random

def has_duplicate(birthdays):
    return len(birthdays) != len(set(birthdays))

def birthday_paradox_simulation(trails = 1000):
    print("Group | Probability of Shared Birthday")
    print("--------------------------------------")
    for i in range(5, 105, 5):
        count = 0
        for j in range(trails):
            birthdays = [random.randint(0, 364) for _ in range(i)]
            if has_duplicate(birthdays=birthdays):
                count +=1
        probability = count / trails
        print(f"{i:10d} | {probability:.3f}")

birthday_paradox_simulation()