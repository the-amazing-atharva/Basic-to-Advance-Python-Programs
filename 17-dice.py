import random


def rollDice(numberOfDice):
    total = 0
    for i in range(numberOfDice):
        total += random.randint(1, 6)
    return total
