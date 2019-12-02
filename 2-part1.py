inputFile = "2-input.txt"

def opAdd(index, arr):
    input1 = arr[index+1]
    input2 = arr[index+2]

    loc = arr[index+3]
    arr[loc] = arr[input1] + arr[input2]

def opMult(index, arr):
    input1 = arr[index+1]
    input2 = arr[index+2]

    loc = arr[index+3]
    arr[loc] = arr[input1] * arr[input2]

with open(inputFile) as fp:
    line = fp.readline()
    arr = line.split(',')

arr = list(map(int, arr))

index = 0

arr[1] = 12
arr[2] = 2

while True:
    if arr[index] == 1:
        opAdd(index, arr)
    if arr[index] == 2:
        opMult(index, arr)
    if arr[index] == 99:
        break

    index += 4

print(arr[0])
