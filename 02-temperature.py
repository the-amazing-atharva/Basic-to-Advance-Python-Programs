def convertToFahrenheit(degreeCelsius):
    fah = degreeCelsius*(9/5) + 32
    return fah


def convertToCelsius(degreeFahrenheit):
    cel = (degreeFahrenheit-32)*(5/9)


assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
# Rounding errors cause a slight discrepancy:
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001
