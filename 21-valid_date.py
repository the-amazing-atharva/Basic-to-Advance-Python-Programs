import leapyear


def isValidDate(year, month, day):
    if not (1 <= month <= 12):
        return False

    if leapyear.isLeapYear(year) and month == 2 and day == 29:
        return True

    if month in (1, 3, 5, 7, 8, 10, 12) and not (1 <= day <= 31):
        return False

    elif month in (4, 6, 9, 11) and not (1 <= day <= 30):
        return False

    return True
