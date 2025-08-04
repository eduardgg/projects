
from collections import deque

DEBUG = False

its = [0]
sostres, terres = [], []
nums = [[0 for _ in range(9)] for _ in range(9)]
opcions = [[{i for i in range(1, 10)} for _ in range(9)] for _ in range(9)]



def printSudoku():

    for i in range(9):
        for j in range(9):
            if (nums[i][j] == 0):
                print("·", end=" ")
            else:
                print(str(nums[i][j]), end=" ")
            if j < 8:
                print(hIneqs[i][j], end=" ")
        print()
        if i < 8: 
            for x in range(9):
                print("^" if vIneqs[x][i] == '<' else "v", end="   ")
        print()


def finished():

    # Check si algun element no està posat
    for i in range(9):
        for j in range(9):
            if nums[i][j] == 0:
                return False
    return True


def valid():

    # Check de files
    for i in range(9):
        numeros = set()
        for j in range(9):
            if (nums[i][j] != 0 and nums[i][j] in numeros):
                return False
            numeros.add(nums[i][j])
    
    # Check de columnes
    for j in range(9):
        numeros = set()
        for i in range(9):
            if (nums[i][j] != 0 and nums[i][j] in numeros):
                return False
            numeros.add(nums[i][j])
    
    # Check d'inequacions horitzontals:
    for i in range(9):
        for j in range(8):
            if hIneqs[i][j] == '<' and nums[i][j] > nums[i][j+1] > 0:
                return False
            if hIneqs[i][j] == '>' and 0 < nums[i][j] < nums[i][j+1]:
                return False
    
    # Check d'inequacions verticals:
    for i in range(9):
        for j in range(8):
            if vIneqs[i][j] == '<' and nums[j][i] > nums[j+1][i] > 0:
                return False
            if vIneqs[i][j] == '>' and 0 < nums[j][i] < nums[j+1][i]:
                return False
            
    return True


def solve():

    global poss, nums, opcions, hIneqs, vIneqs

    if type(hIneqs) == str:
        hIneqs = [hIneqs[8*i: 8*i+8] for i in range(9)]
        vIneqs = [vIneqs[8*i: 8*i+8] for i in range(9)]

    its[0] = 0
    sostres.clear()
    terres.clear()
    opcions = [[{i for i in range(1, 10)} for _ in range(9)] for _ in range(9)]
    nums = [[0 for _ in range(9)] for _ in range(9)]
    for (i, j, k) in poss:
        nums[i][j] = k

    for i in range(9):
        for j in range(9):
            if j > 0 and hIneqs[i][j-1] == '>':
                continue
            if j < 8 and hIneqs[i][j] == '<':
                continue
            if i > 0 and vIneqs[j][i-1] == '>':
                continue
            if i < 8 and vIneqs[j][i] == '<':
                continue
            sostres.append((i, j))

    for i in range(9):
        for j in range(9):
            if j > 0 and hIneqs[i][j-1] == '<':
                continue
            if j < 8 and hIneqs[i][j] == '>':
                continue
            if i > 0 and vIneqs[j][i-1] == '<':
                continue
            if i < 8 and vIneqs[j][i] == '>':
                continue
            terres.append((i, j))

    for i in range(9):
        for j in range(9):
            if nums[i][j] != 0:
                opcions[i][j] = {nums[i][j]}
                netejaSimple(i, j)
    
    print("Sudoku a resoldre:")
    printSudoku()
    bruteForce()
    print("Iteracions de Força Bruta: ", its[0])
    print()


def bruteForce():

    global nums, opcions
    netejaOpcions()

    if not valid():
        if DEBUG: print("El sudoku no és vàlid, tornem enrere")
        return False
    
    if finished():
        print("Sudoku resolt!")
        printSudoku()
        return True

    its[0] += 1
    opcionsTop = 10

    for i in range(9):
        for j in range(9):
            if nums[i][j] == 0:
                if len(opcions[i][j]) < opcionsTop:
                    topi, topj = i, j
                    opcionsTop = len(opcions[i][j])
    
    if opcionsTop == 10:
        return False
    
    if DEBUG: print("La millor casella per iniciar brute force és (", topi, ",", topj, ") amb opcions: ", opcions[topi][topj])
    copiaNums = [[nums[i][j] for j in range(9)] for i in range(9)]
    copiaOpcions = [[{e for e in opcions[i][j]} for j in range(9)] for i in range(9)]
    for k in opcions[topi][topj]:
        if DEBUG: print("Assumim un", k, "a la fila", topi + 1, ", columna ", topj + 1)
        nums[topi][topj] = k
        opcions[topi][topj] = {k}
        if netejaSimple(topi, topj) and netejaOpcions() and bruteForce():
            return True
        nums = [[copiaNums[i][j] for j in range(9)] for i in range(9)]
        opcions = [[{e for e in copiaOpcions[i][j]} for j in range(9)] for i in range(9)]
    
    if DEBUG: print("No ha funcionat cap opció per", topi + 1, ",", topj + 1, ", tornem enrere")
    return False


def unicaOpcio():
    # ESTRATEGIA:
    # Omplir les caselles quan són les úniques de la fila o columna
    # on hi pot anar un nombre concret
    # Fer sempre que hi hagi canvis a les opcions
    # Un bon lloc seria just després d'usar "netejaOpcions", o sigui
    # activant-la des de dins de la funció mateix.

    for e in range(1, 10):

        # Check de cada fila
        for i in range(9):
            count = 0
            for j in range(9):
                if nums[i][j] == e:
                    count = 0
                    break
                if e in opcions[i][j]:
                    count += 1
                    last = j
                    if count > 1:
                        break
            if count == 1:
                nums[i][last] = e
                opcions[i][last] = {e}
                if not netejaOpcions():
                    return False

        # Check de cada columna
        for j in range(9):
            count = 0
            for i in range(9):
                if nums[i][j] == e:
                    count = 0
                    break
                if e in opcions[i][j]:
                    count += 1
                    last = i
                    if count > 1:
                        break
            if count == 1:
                nums[last][j] = e
                opcions[last][j] = {e}
                if not netejaOpcions():
                    return False

    return True


def netejaSimple(i, j):
    # ESTRATEGIA:
    # Eliminar un nombre concret de les opcions de tota una fila i columna.
    # Fer sempre que s'escrigui un nombre al sudoku "nums"

    # Neteja de Columna
    for y in range(9):
        if y != i and nums[i][j] in opcions[y][j]:
            opcions[y][j].remove(nums[i][j])
            if not opcions[y][j]: return False

    # Neteja de Fila
    for x in range(9):
        if x != j and nums[i][j] in opcions[i][x]:
            opcions[i][x].remove(nums[i][j])
            if not opcions[i][x]: return False
            
    return True


def netejaOpcions():
    # ESTRATEGIA
    # Netejar les opcions de totes les caselles utilitzant els camins
    # formats per les inequacions, i valors max/min que poden assolir
    # Això es fa amb un BFS a partir dels terres i sostres del joc.
    # Fer sempre que hi hagi canvis a les opcions.

    queue = deque(e for e in sostres)
    while queue:
        i, j = queue.popleft()
        ma = max(opcions[i][j])
        if j > 0 and hIneqs[i][j-1] == '<' and max(opcions[i][j-1]) >= ma:
            for e in list(opcions[i][j-1]):
                if e >= ma:
                    opcions[i][j-1].remove(e)
                    if not opcions[i][j-1]: return False
            queue.append((i, j-1))
        if j < 8 and hIneqs[i][j] == '>' and max(opcions[i][j+1]) >= ma:
            for e in list(opcions[i][j+1]):
                if e >= ma:
                    opcions[i][j+1].remove(e)
                    if not opcions[i][j+1]: return False
            queue.append((i, j+1))
        if i > 0 and vIneqs[j][i-1] == '<' and max(opcions[i-1][j]) >= ma:
            for e in list(opcions[i-1][j]):
                if e >= ma:
                    opcions[i-1][j].remove(e)
                    if not opcions[i-1][j]: return False
            queue.append((i-1, j))
        if i < 8 and vIneqs[j][i] == '>' and max(opcions[i+1][j]) >= ma:
            for e in list(opcions[i+1][j]):
                if e >= ma:
                    opcions[i+1][j].remove(e)
                    if not opcions[i+1][j]: return False
            queue.append((i+1, j))

    queue = deque(e for e in terres)
    while queue:
        i, j = queue.popleft()
        mi = min(opcions[i][j])
        if j > 0 and hIneqs[i][j-1] == '>' and min(opcions[i][j-1]) <= mi:
            for e in list(opcions[i][j-1]):
                if e <= mi:
                    opcions[i][j-1].remove(e)
                    if not opcions[i][j-1]: return False
            queue.append((i, j-1))
        if j < 8 and hIneqs[i][j] == '<' and min(opcions[i][j+1]) <= mi:
            for e in list(opcions[i][j+1]):
                if e <= mi:
                    opcions[i][j+1].remove(e)
                    if not opcions[i][j+1]: return False
            queue.append((i, j+1))
        if i > 0 and vIneqs[j][i-1] == '>' and min(opcions[i-1][j]) <= mi:
            for e in list(opcions[i-1][j]):
                if e <= mi:
                    opcions[i-1][j].remove(e)
                    if not opcions[i-1][j]: return False
            queue.append((i-1, j))
        if i < 8 and vIneqs[j][i] == '<' and min(opcions[i+1][j]) <= mi:
            for e in list(opcions[i+1][j]):
                if e <= mi:
                    opcions[i+1][j].remove(e)
                    if not opcions[i+1][j]: return False
            queue.append((i+1, j))

    # Usant aquesta funció a continuació, restem iteracions de força bruta
    # Tot i així, el mètode global no resulta més eficient.
    if not unicaOpcio():
        return False
    
    return True



    


# ----------------------------------------------
# TEST CASES:
# ----------------------------------------------

# TEST 1 --- EASY:
hIneqs = ["<<>><><>", "<<><<><>", "><<><><<", "<>><>><<", "><<<><><", ">><><>><", "><><><><", "<><>>><>", ">><>><<>"]
vIneqs = ["<<><><><", "<<<><<<>", "<>>>><><", "><><<><>", ">><<><>>", "<>><<><>", "<>><>>>>", ">><>>><<", ">><><>><"]
poss = [(4, 6, 9), (8, 4, 5)]
solve()

# ----------------------------------------------

# TEST 2 --- HARD:
hIneqs = ["><><<><<", ">>><<><<", "<<><><><", "<><<><><", "<><><><>", "<><><<<>", "><><><><", "<<<><<>>", "><>><><>"]
vIneqs = ["<>><><>>", "<><<>><>", "><>>><<<", "><<><><>", "><<><<><", "<><<>><<", "><><<<<>", ">><<<>><", ">><><<><"]
poss = [(1, 8, 8), (5, 4, 3)]
solve()

# ----------------------------------------------

# TEST 3 --- HARD:
hIneqs = ["<>>><<><", "><<><><>", "<><><<>>", "><><>><>", ">><>><<>", "<<><<>>>", "<<><>>><", ">><><<>>", "<<>><<>>"]
vIneqs = ["<>><>><>", "><><>>><", ">><><>><", "<>>>><<>", "<><><<>>", "<>>><>>>", "><><<<<<", "<><<>><<", ">><><<><"]
poss = [(6, 2, 5), (7, 2, 1)]
solve()

# ----------------------------------------------

# TEST 4 --- HARD:
# Another way of entering the input data (left -> right and up -> down)
hIneqs = "<<><><>><>>><><>>><<><>><><>>><><<<>><<>><>><>><><<><>><<><<><<<><>><<<<"
vIneqs = "><><<>><<><><><>>><<<>><<<<>><<>><>>><<><>>><<><><><><><<><<><<<<><><<<>"
poss = [(2, 4, 9), (7, 1, 4)]
solve()

# ----------------------------------------------