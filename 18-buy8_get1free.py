def getCostOfCoffe(numberOfCoffees, pricePerCoffee):
    totalPrice = 0
    cupsUntilFreeCoffee = 8

    while numberOfCoffees > 0:
        # Decrement the number of coffees left to buy:
        numberOfCoffees -= 1
        # If this cup of coffee is free, reset the number to buy until
        # a free cup back to 8:
        if cupsUntilFreeCoffee == 0:
            cupsUntilFreeCoffee = 8
        else:
            totalPrice += pricePerCoffee
            cupsUntilFreeCoffee -= 1

    return totalPrice
