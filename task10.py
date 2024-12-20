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
                print(" ",end='')
            # if len(str(array[i][j])) == 2:
            #     print(" ", end='')
            print(str(array[i][j]),end=' ')
        print('')

def fill_array_randint(x,y):
    array = create2DArray(x,y)
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            array[i][j] = int(randint(0,99))

    return array

def task(array):
    maxBotDiag = float(array[0][0])
    maxBotDiagCollumn = 0
    for i in range(0,len(array)):
        for j in range(0,len(array[0])):
            if i >= j:
                if float(array[i][j]) > maxBotDiag:
                    maxBotDiag = float(array[i][j])
                    maxBotDiagCollumn = j

    minTopDiag = float(array[0][0])
    minTopDiagCollumn = 0
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            if i < j:
                if float(array[i][j]) < minTopDiag:
                    minTopDiag = float(array[i][j])
                    minTopDiagCollumn = j



    print(maxBotDiagCollumn,minTopDiagCollumn)

    if minTopDiagCollumn > maxBotDiagCollumn:
        minTopDiagCollumn -= 1

    if minTopDiagCollumn < maxBotDiagCollumn:
        minTopDiagCollumn += 1

    if minTopDiagCollumn == maxBotDiagCollumn:
        minTopDiagCollumn = "SAME"

    for i in range(0,len(array)):
        array[i].pop(maxBotDiagCollumn)

    if minTopDiagCollumn != "SAME":
        for i in range(0, len(array)):
            array[i].pop(minTopDiagCollumn)

    display2DArray(array)

array1 = fill_array_randint(7,7)

display2DArray(array1)

print("--------------------------------------")

task(array1)