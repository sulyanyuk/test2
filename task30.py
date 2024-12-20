from random import *

def create2DArray(y,x):
    array = []
    for i in range(0,y):
        array.append([])
        for j in range(0,x):
            array[i].append([])
            array[i][j] = '0'
    return array

def display2DArray(array):
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if len(str(array[i][j])) == 1:
                print("  ",end='')
            if len(str(array[i][j])) == 2:
                print(" ", end='')
            print(str(array[i][j]),end=' ')
        print('')

def fill_array_randint(x,y):
    array = create2DArray(x,y)
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            array[i][j] = int(randint(-99,99))

    return array

def task(array):
    iRowMaxDiag = 0
    MaxDiag = float(array[0][0])
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if i == j:
                if float(array[i][j]) > MaxDiag:
                    MaxDiag = float(array[i][j])
                    iRowMaxDiag = i

    iRowFirstNegThirdCollumn = -1
    for i in range(0,len(array)):
        if float(array[i][2]) < 0:
            iRowFirstNegThirdCollumn = i
            break
    if iRowFirstNegThirdCollumn == -1:
        print("No negatives in 3rd collumn!")
    else:
        array[iRowMaxDiag], array[iRowFirstNegThirdCollumn] = array[iRowFirstNegThirdCollumn], array[iRowMaxDiag]
        display2DArray(array)

array1 = fill_array_randint(5,5)

display2DArray(array1)

print("--------------------------------------")

task(array1)

