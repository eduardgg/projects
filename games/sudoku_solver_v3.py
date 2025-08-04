

sudoku = [
    [6,0,0,0,7,0,0,0,1],
    [4,0,2,0,5,0,0,0,0],
    [9,0,0,0,0,0,2,4,0],
    [8,0,0,1,0,0,0,0,7],
    [0,0,9,0,0,6,0,0,3],
    [0,0,0,0,0,9,0,2,0],
    [0,0,0,0,0,0,3,0,0],
    [0,0,1,0,0,0,7,0,0],
    [0,4,0,0,6,5,0,0,0]
    ]


def printSudoku():
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(sudoku[i][j] if sudoku[i][j] != 0 else "-", end=" ")
        print()
    print()

def finished():
    tots = {i+1 for i in range(9)}
    if any([{sudoku[i][j] for i in range(9)} != tots for j in range(9)]):
        return False
    if any([{sudoku[i][j] for j in range(9)} != tots for i in range(9)]):
        return False
    if any([{sudoku[3*x+i][3*y+j] for i in range(3) for j in range(3)} != tots for x in range(3) for y in range(3)]):
        return False
    return True

def opcions(i, j):
    opcs = set(range(1, 10))
    opcs -= set(sudoku[i])
    opcs -= {sudoku[x][j] for x in range(9)}
    bi, bj = 3 * (i // 3), 3 * (j // 3)
    opcs -= {sudoku[bi + x][bj + y] for x in range(3) for y in range(3)}
    return opcs

def bruteForce():
    if finished():
        print("Sudoku resolt!")
        printSudoku()
        return True
    min_opcions = (10, None, None, None)
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                opcs = opcions(i, j)
                if not opcs:
                    return False
                if len(opcs) < min_opcions[0]:
                    min_opcions = (len(opcs), i, j, opcs)
    _, i, j, opcionsMillor = min_opcions
    for val in opcionsMillor:
        # print(f"Provant {val} a ({i+1},{j+1})")
        sudoku[i][j] = val
        if bruteForce():
            return True
        sudoku[i][j] = 0  
        # print(f"Retrocés a ({i+1},{j+1})")
    return False

bruteForce()