import random

def genPartida(n):
    deck = []
    mans = []
    for i in range(n):
        mans += [[]]
    for i in range(7):
        for j in range(i,7):
            deck += [(i,j)]
    random.shuffle(deck)
    for i in range(7):
        for j in range(n):
            mans[j] += [deck.pop()]
    return deck, mans

def printTaula(cuaDre, cuaEsq, deck, mans):
    n = len(cuaDre)
    reverse = [(cuaDre[n-1-i][1], cuaDre[n-1-i][0]) for i in range(n)]
    print("Taula: ", reverse + cuaEsq)
    print("Deck: ", deck)
    for j in range(len(mans)):
        print("Jugador ", j, ": ", mans[j])
    print()

def inici(mans):
    # Comença qui té el doble més alt o, si no hi ha dobles,
    # Qui tingui un nombre més alt en les peces
    # Per exemple, (6-3) > (5-4) > (5-2)
    for i in range(7):
        for j in range(len(mans)):
            if (6-i,6-i) in mans[j]:
                return j, (6-i,6-i)
    for i in range(6):
        for j in range(len(mans)):
            if (5-i,6) in mans[j]:
                return j, (5-i,6)
    # No cal més casos, ja que entre 14 peces és gairebé segur
    # que sortirà o bé un doble o bé un 6, encara que fem molts
    # milions de partides (prob = 1 - 15/(28 choose 14)).

def domino(deck, mans):
    global nJugadors
    tirades = [0,0,0,0,0,0,0]
    
    torn, inicial = inici(mans)
    # print("Jugador ", torn, " tira ", inicial)
    mans[torn].remove(inicial)
    torn = (torn + 1) % nJugadors
    
    tirades[inicial[0]] += 1
    tirades[inicial[1]] += 1
    esq = inicial[0]
    dre = inicial[1]
    cuaEsq = []
    cuaDre = [inicial]

    while True:
        # printTaula(cuaDre, cuaEsq, deck, mans)
        # Estratègia bàsica de tirada
        
        if esq == dre and tirades[esq] == 8:
            # print("Joc tancat")
            # printTaula(cuaDre, cuaEsq, deck, mans)
            return -1

        quants = [0,0,0,0,0,0,0]
        for fitxa in mans[torn]:
            quants[fitxa[0]] += 1
            quants[fitxa[1]] += 1

        if quants[esq] + quants[dre] == 0:
            if len(deck) > 0:
                robada = deck.pop()
                mans[torn] += [robada]
                # print("Jugador ", torn, " roba ", robada)

        else:
            random.shuffle(mans[torn])
            for fitxa in mans[torn]:
                if fitxa[0] == esq:
                    cuaEsq += [fitxa]
                    esq = fitxa[1]
                    break
                if fitxa[1] == esq:
                    cuaEsq += [(fitxa[1],fitxa[0])]
                    esq = fitxa[0]
                    break
                if fitxa[0] == dre:
                    cuaDre += [fitxa]
                    dre = fitxa[1]
                    break
                if fitxa[1] == dre:
                    cuaDre += [(fitxa[1],fitxa[0])]
                    dre = fitxa[0]
                    break

            # print("Jugador ", torn, " tira ", fitxa)
            mans[torn].remove(fitxa)
            tirades[fitxa[0]] += 1
            tirades[fitxa[1]] += 1
            if len(mans[torn]) == 0:
                # print("Guanyador: Jugador ", torn)
                # printTaula(cuaDre, cuaEsq, deck, mans)
                return torn

        torn = (torn + 1) % nJugadors       


"""
# Simulació d'una partida aleatòria:
nJugadors = 2
deck, mans = genPartida(nJugadors)
printTaula([], [], deck, mans)
domino(deck, mans)
"""

# Simulació de diverses partides:
nJugadors = 2
partides = 10000
resultats = {i:0 for i in range(-1,nJugadors)}
for i in range(partides):
    deck, mans = genPartida(nJugadors)
    guanyador = domino(deck, mans)
    resultats[guanyador] += 1
for i in range(nJugadors):
    print("Partides guanyades pel jugador ", i, ": ", resultats[i]/partides*100, "%")
print("Partides acabades en taules: ", resultats[-1]/partides*100, "%")