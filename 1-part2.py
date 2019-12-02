import math

def fuelRecursive(mass):
    fuel = math.floor(mass/3) - 2

    if fuel <= 0:
        return 0

    return fuel + fuelRecursive(fuel)


inputFile = "1-input.txt"

totalFuel = 0

with open(inputFile) as fp:
    line = fp.readline()
    while line:
        num = int(line)
        fuelFromMass = math.floor(num/3) - 2
        fuelFromFuel = fuelRecursive(fuelFromMass)

        totalFuel += fuelFromMass + fuelFromFuel
        line = fp.readline()

print(totalFuel)
