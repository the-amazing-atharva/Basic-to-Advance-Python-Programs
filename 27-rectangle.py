def drawRectangle(width, height):
    # Special case: If width or height is less than 1, draw nothing:
    if width < 1 or height < 1:
        return
    # Loop over each row:
    for row in range(height):
        # Loop over each column in this row:
        for column in range(width):
            # Print a hashtag:
            print('#', end='')
    # At the end of the row, print a newline:
    print()
