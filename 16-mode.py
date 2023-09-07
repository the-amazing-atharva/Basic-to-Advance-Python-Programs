def mode(numbers):
    count = {}
    most = None
    mostCount = 0

    for num in numbers:
        if num not in count:
            count[num] = 0
        count[num] += 1
        if count[num] > mostCount:
            most = num
            mostCount = count[num]
    return most
