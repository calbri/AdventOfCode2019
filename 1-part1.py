import math

inputFile = "1-input.txt"

totalFuel = 0

with open(inputFile) as fp:
    line = fp.readline()
    while line:
        num = int(line)
        totalFuel += math.floor(num/3) - 2

        line = fp.readline()

print(totalFuel)
