def writeToFile(fname, text):
    with open(fname, 'w') as f:
        f.write(text)


def appendToFile(fname, text):
    with open(fname, 'a') as f:
        f.write(text)


def readFromFile(fname):
    with open(fname, 'r') as f:
        return f.read()
