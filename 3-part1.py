def nextPos(position, instr, wires, wire):
    length = int(instr[1:])

    for i in range(length):
        if instr[0] == 'R':
            nextPos = (position[0], position[1] + 1)
        if instr[0] == 'U':
            nextPos = (position[0] - 1, position[1])
        if instr[0] == 'L':
            nextPos = (position[0], position[1] - 1)
        if instr[0] == 'D':
            nextPos = (position[0] + 1, position[1])

        if nextPos in wires:
            if not(wires[nextPos] == wire):
                wires[nextPos] = -1
        else:
            wires[nextPos] = wire

        position = nextPos
            
    return position

inputFile = "3-input.txt"

with open(inputFile) as fp:
    line = fp.readline()
    wire1 = line.split(',')

    line = fp.readline()
    wire2 = line.split(',')

wires = {}

position = (0,0)
for direction in wire1:
    position = nextPos(position, direction, wires, 'a')

position = (0,0)
for direction in wire2:
    position = nextPos(position, direction, wires, 'b')

minDistance = -1

for pos in wires:
    if not(wires[pos] == -1):
        continue

    dist = abs(pos[0]) + abs(pos[1])

    if minDistance == -1:
        minDistance = dist
        continue

    if dist < minDistance:
        minDistance = dist

print(minDistance)