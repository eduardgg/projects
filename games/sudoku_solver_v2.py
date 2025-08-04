
def printSudoku(sudoku):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(sudoku[i][j] if sudoku[i][j] != 0 else "-", end=" ")
        print()
    print()

def finished(sudoku):
    tots = {i+1 for i in range(9)}
    if any([{sudoku[i][j] for i in range(9)} != tots for j in range(9)]):
        return False
    if any([{sudoku[i][j] for j in range(9)} != tots for i in range(9)]):
        return False
    if any([{sudoku[3*x+i][3*y+j] for i in range(3) for j in range(3)} != tots for x in range(3) for y in range(3)]):
        return False
    return True

def opcions(sudoku, i, j):
    opcs = set(range(1, 10))
    opcs -= set(sudoku[i])
    opcs -= {sudoku[x][j] for x in range(9)}
    bi, bj = 3 * (i // 3), 3 * (j // 3)
    opcs -= {sudoku[bi + x][bj + y] for x in range(3) for y in range(3)}
    return opcs

def neteja(sudoku):
    canvis = True
    while canvis:
        canvis = False
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    os = opcions(sudoku, i, j)
                    if len(os) == 1:
                        sudoku[i][j] = os.pop()
                        canvis = True
    print("Sudoku simplificat:")
    printSudoku(sudoku)

def bruteForce(sudoku):
    neteja(sudoku)
    if finished(sudoku):
        print("Sudoku resolt!")
        printSudoku(sudoku)
        return True
    min_opcions = (10, None, None, None)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                opcs = opcions(sudoku, i, j)
                if not opcs:
                    return False
                if len(opcs) < min_opcions[0]:
                    min_opcions = (len(opcs), i, j, opcs)
    _, i, j, opcionsMillor = min_opcions
    for val in opcionsMillor:
        sudoku_copia = [row[:] for row in sudoku]
        sudoku_copia[i][j] = val
        print(f"Provant {val} a ({i+1},{j+1})")
        if bruteForce(sudoku_copia):
            return True
    print("Retrocés necessari")
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

bruteForce(sudoku1)


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

bruteForce(sudoku2)


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

bruteForce(sudoku3)