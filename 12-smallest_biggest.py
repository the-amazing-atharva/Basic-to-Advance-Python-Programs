def getSmallest(numbers):
    if len(numbers) == 0:
        return None
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
