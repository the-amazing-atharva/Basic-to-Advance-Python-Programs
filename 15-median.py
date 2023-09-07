def median(numbers):
    if len(numbers) == 0:
        return None
    numbers.sort()

    middle = len(numbers)//2

    if len(numbers) % 2 == 0:
        return (numbers[middle] + numbers[middle - 1]) / 2
    else:
        return [middle]
