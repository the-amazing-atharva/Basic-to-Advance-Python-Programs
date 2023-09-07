def average(numbers):
    if len(numbers) == 0:
        return None
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average
