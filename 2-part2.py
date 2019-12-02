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

firstArr = list(map(int, arr))

target = 19690720
trial1 = 0
trial2 = 0 
flip1 = True

for trial1 in range(0,100):
    for trial2 in range(0,100):
        try:
            arr = firstArr.copy()
            arr[1] = trial1
            arr[2] = trial2

            index = 0
            while True:
                if arr[index] == 1:
                    opAdd(index, arr)
                if arr[index] == 2:
                    opMult(index, arr)
                if arr[index] == 99:
                    break

                index += 4

            if arr[0] == target:
                print(100*trial1 + trial2)
                break
        except:
            # invalid range
            continue



