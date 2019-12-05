inputFile = "5-input.txt"

def opAdd(index, arr, A, B, C):
    input1 = arr[index+1]
    input2 = arr[index+2]

    loc = arr[index+3]

    if C == 1:
        param1 = input1
    else:
        param1 = arr[input1]

    if B == 1:
        param2 = input2
    else:
        param2 = arr[input2]

    arr[loc] = param1 + param2

def opMult(index, arr, A, B, C):
    input1 = arr[index+1]
    input2 = arr[index+2]

    loc = arr[index+3]

    if C == 1:
        param1 = input1
    else:
        param1 = arr[input1]

    if B == 1:
        param2 = input2
    else:
        param2 = arr[input2]

    arr[loc] = param1 * param2

def opSave(index, arr, A, B, C):      
    input1 = arr[index+1]

    arr[input1] = 1

def opOutput(index, arr, A, B, C):
    if C == 1:
        param1 = arr[index+1]
    else:
        param1 = arr[arr[index+1]]

    print(param1)

with open(inputFile) as fp:
    line = fp.readline()
    arr = line.split(',')

arr = list(map(int, arr))

index = 0

while True:
    chars = str(arr[index])

    op = 99
    A = 0
    B = 0
    C = 0

    if len(chars) == 5:
        A = int(chars[0])
        B = int(chars[1])
        C = int(chars[2])
        op = int(chars[3:5])
    elif len(chars) == 4:
        B = int(chars[0])
        C = int(chars[1])
        op = int(chars[2:4])
    elif len(chars) == 3:
        C = int(chars[0])
        op = int(chars[1:3])
    else:
        op = int(chars)

    if op == 1:
        opAdd(index, arr, A, B, C)
        index += 4
    elif op == 2:
        opMult(index, arr, A, B, C)
        index += 4
    elif op == 3:
        opSave(index,arr, A, B, C)
        index += 2
    elif op == 4:
        opOutput(index,arr, A, B, C)
        index += 2
    elif op == 99:
        break
    else:
        print("error")
        break

    

