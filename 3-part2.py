def nextPos(position, instr, wires, wire, totalSteps):
    length = int(instr[1:])

    for i in range(length):
        totalSteps += 1

        if instr[0] == 'R':
            nextPos = (position[0], position[1] + 1)
        if instr[0] == 'U':
            nextPos = (position[0] - 1, position[1])
        if instr[0] == 'L':
            nextPos = (position[0], position[1] - 1)
        if instr[0] == 'D':
            nextPos = (position[0] + 1, position[1])

        if nextPos in wires:
            if not(wires[nextPos][0] == wire):
                wires[nextPos] = (-1, totalSteps + wires[nextPos][1])
        else:
            wires[nextPos] = (wire, totalSteps)

        position = nextPos
            
    return (position, totalSteps)

inputFile = "3-input.txt"

with open(inputFile) as fp:
    line = fp.readline()
    wire1 = line.split(',')

    line = fp.readline()
    wire2 = line.split(',')

wires = {}

position = (0,0)
totalSteps = 0
for direction in wire1:
    retVal = nextPos(position, direction, wires, 'a', totalSteps)
    position = retVal[0]
    totalSteps = retVal[1]

position = (0,0)
totalSteps = 0
for direction in wire2:
    retVal = nextPos(position, direction, wires, 'b', totalSteps)
    position = retVal[0]
    totalSteps = retVal[1]
    
minDistance = -1

for pos in wires:
    if not(wires[pos][0] == -1):
        continue

    dist = wires[pos][1]

    if minDistance == -1:
        minDistance = dist
        continue

    if dist < minDistance:
        minDistance = dist

print(minDistance)