lower = 146810
upper = 612564
numDigits = 6

numValid = 0

for i in range(lower, upper + 1):
    valid = False

    for j in range(numDigits - 1):
        numString = str(i)
        if int(numString[j]) > int(numString[j+1]):
            valid = False
            break
        if ((numString[j] == numString[j+1]) 
            and ((j == 0) or (numString[j] != numString[j-1]))
            and ((j == numDigits - 2) or (numString[j+1] != numString[j+2]))):
            valid = True

    if (valid):
        numValid += 1

print(numValid)