def fetChessSquareColor(column, row):
    sums = column + row
    if column < 1 or column > 8 or row < 1 or row > 8:
        return " "
    elif not (column % 2 ^ row % 2):
        return 'white'
    else:
        return 'black'
