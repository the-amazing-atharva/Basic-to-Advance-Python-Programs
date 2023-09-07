for numberOfBottles in range(99, 1, -1):
    print(numberOfBottles, 'bottles of beer on the wall,')
    print(numberOfBottles, 'bottles of beer,')
    print('Take one down,')
    print('Pass it around,')
    # If there is only one, print "bottle" instead of "bottles".
    if (numberOfBottles - 1) == 1:
        print('1 bottle of beer on the wall,')
    else:
        print(numberOfBottles - 1, ' bottles of beer on the wall,')
# The last stanza has singular "bottle" and a different final line:
print('1 bottle of beer on the wall,')
print('1 bottle of beer,')
print('Take one down,')
print('Pass it around,')
print('No more bottles of beer on the wall!')
