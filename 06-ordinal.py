def ordinalSuffix(number):
    numberStr = str(number)
    # 11, 12, and 13 have the suffix th:
    if numberStr[-2:] in ('11', '12', '13'):
        return numberStr + 'th'
    # Numbers that end with 1 have the suffix st:
    if numberStr[-1] == '1':
        return numberStr + 'st'
    # Numbers that end with 2 have the suffix nd:
    if numberStr[-1] == '2':
        return numberStr + 'nd'
    # Numbers that end with 3 have the suffix rd:
    if numberStr[-1] == '3':
        return numberStr + 'rd'
    # All other numbers end with th:
    return numberStr + 'th'
