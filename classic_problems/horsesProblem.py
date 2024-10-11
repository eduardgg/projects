
# Aquest codi és eficient, no és un Backtracking.
# Permet trobar un camí eulerià que passi per totes les caselles del tauler,
# fent servir un cavall.


def candidates(i, j):
    dirs = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
    res = []
    for (x, y) in dirs:
        if x+i >= 0 and x+i < 8 and y+j >= 0 and y+j < 8 and board[i+x][j+y] == -1:
            res.append((i+x, j+y))
    return res

def printBoard(board):
    for i in range(8):
        for j in range(8):
            print(board[i][j], end= " "*(3-len(str(board[i][j]))))
        print()

board = [[-1 for _ in range(8)] for _ in range(8)]

pos = (0,0)
cands = [(1,2)]
board[0][0] = 1
board[2][1] = 64

# Amb aquesta condició aconseguim acabar al mateix punt on comencem.
# Crec que funciona de casualitat, ja que el moviment 63 no té per què
# caure a una casella a distància vàlida de 64.

movs = 2
while movs < 64:
    best = [-1]*10
    for (x, y) in cands:
        newCands = candidates(x, y)
        if len(newCands) < len(best):
            pos = (x, y)
            best = newCands
    cands = best
    board[pos[0]][pos[1]] = movs
    movs += 1

printBoard(board)