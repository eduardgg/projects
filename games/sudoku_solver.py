

def printSudoku(sudoku):
    for i in range(9):
        for j in range(9):
            if (sudoku[i][j] == 0):
                print("-", end=" ")
            else:
                print(str(sudoku[i][j]), end=" ")
            if j%3 == 2 and j != 8:
                print("|", end=" ")
        print()
        if i%3 == 2 and i != 8:
            print("----------------------")
    print()
    print()


def finished(sudoku):

    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False

    for i in range(9):
        numeros = set()
        for j in range(9):
            if (sudoku[i][j] != 0):
                if (sudoku[i][j] in numeros):
                    return False
                numeros.add(sudoku[i][j])

    for j in range(9):
        numeros = set()
        for i in range(9):
            if (sudoku[i][j] != 0):
                if (sudoku[i][j] in numeros):
                    return False
                numeros.add(sudoku[i][j])

    for bx in range(3):
        for by in range(3):
            numeros = set()
            for i in range(3):
                for j in range(3):
                    if (sudoku[3*bx+i][3*by+j] != 0):
                        if (sudoku[3*bx+i][3*by+j] in numeros):
                            return False
                        numeros.add(sudoku[3*bx+i][3*by+j])
    
    return True


def opcions(sudoku, i, j):
    opcs = {1,2,3,4,5,6,7,8,9}
    for a in range(9):
        if (sudoku[a][j] != 0) and (sudoku[a][j] in opcs):
            opcs.remove(sudoku[a][j])
    for b in range(9):
        if (sudoku[i][b] != 0) and (sudoku[i][b] in opcs):
            opcs.remove(sudoku[i][b])
    for a in range(3):
        for b in range(3):
            if sudoku[3*(i//3)+a][3*(j//3)+b] in opcs:
                opcs.remove(sudoku[3*(i//3)+a][3*(j//3)+b])
    return opcs


def neteja(sudoku):
    
    canvis = 1
    while canvis:
        canvis = 0
        for i in range(9):
            for j in range(9):
                if (sudoku[i][j] == 0):
                    os = opcions(sudoku, i, j)
                    if len(os) == 1:
                        sudoku[i][j] = os.pop()
                        canvis += 1

    print("I netegem el sudoku de manera trivial")
    printSudoku(sudoku)
    return


def bruteForce(sudoku):

    neteja(sudoku)

    if finished(sudoku):
        print("Sudoku Acabat!")
        printSudoku(sudoku)
        print("_________________________________")
        return True

    its[0] += 1
    numOpcionsMillor = 9
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                opcs = opcions(sudoku, i, j)
                if len(opcs) < 1:
                    return False
                if len(opcs) < numOpcionsMillor:
                    topi, topj = i, j
                    opcionsMillor = opcs
                    numOpcionsMillor = len(opcs)
    # print(millor, opcionsMillor)
    copiaSudoku = [[sudoku[i][j] for j in range(9)] for i in range(9)]
    for k in opcionsMillor:
        print("Assumim un ", k, " a la fila ", topi + 1, ", columna ", topj + 1)
        sudoku[topi][topj] = k
        if bruteForce(sudoku):
            return True
        sudoku = copiaSudoku
    print("Alguna cosa no ha funcionat, tornem enrere")
    return False



# ----------------------------------------------
# TEST CASES:
# ----------------------------------------------


# EASY:
sudoku1 = [[9,2,6,3,4,0,0,0,1],
           [0,0,1,7,0,0,3,0,9],
           [0,0,3,8,0,0,2,0,6],
           [0,0,0,0,0,7,0,0,0],
           [0,6,0,9,1,0,4,2,0],
           [0,9,7,2,0,0,6,0,3],
           [0,8,0,4,7,0,1,0,2],
           [7,0,4,1,6,2,0,0,8],
           [0,0,0,5,3,0,0,0,0]]

its = [0]
bruteForce(sudoku1)
print("Iteracions de Força Bruta: ", its[0])


# MEDIUM:
sudoku2 = [[0,4,3,0,0,0,0,5,6],
           [0,0,0,6,7,0,3,0,4],
           [6,0,8,3,0,0,0,0,0],
           [0,0,9,0,8,0,0,7,3],
           [3,6,0,2,0,0,1,9,0],
           [0,0,0,9,0,0,0,0,5],
           [0,8,0,0,9,2,0,0,0],
           [0,9,0,0,0,0,0,0,0],
           [4,3,7,0,0,0,8,2,9]]

its = [0]
bruteForce(sudoku2)
print("Iteracions de Força Bruta: ", its[0])


# HARD / EXPERT / EVIL:
sudoku3 = [[6,0,0,0,7,0,0,0,1],
           [4,0,2,0,5,0,0,0,0],
           [9,0,0,0,0,0,2,4,0],
           [8,0,0,1,0,0,0,0,7],
           [0,0,9,0,0,6,0,0,3],
           [0,0,0,0,0,9,0,2,0],
           [0,0,0,0,0,0,3,0,0],
           [0,0,1,0,0,0,7,0,0],
           [0,4,0,0,6,5,0,0,0]]

its = [0]
bruteForce(sudoku3)
print("Iteracions de Força Bruta: ", its[0])