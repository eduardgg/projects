import random

def fitxes():
    deck = []
    jug1 = []
    jug2 = []
    for i in range(7):
        for j in range(i,7):
            deck += [(i,j)]
    random.shuffle(deck)
    for i in range(7):
        jug1 += [deck.pop()]
        jug2 += [deck.pop()]
    return deck, jug1, jug2

def reverse(cua):
    n = len(cua)
    return [(cua[n-1-i][1], cua[n-1-i][0]) for i in range(n)]

def inici(jug1, jug2):
    for i in range(7):
        if (6-i,6-i) in jug1:
            return 1, (6-i,6-i)
        if (6-i,6-i) in jug2:
            return 2, (6-i,6-i)
    for i in range(6):
        if (5-i,6) in jug1:
            return 1, (5-i,6)
        if (5-i,6) in jug2:
            return 2, (5-i,6)
    for i in range(5):
        if (4-i,5) in jug1:
            return 1, (4-i,5)
        if (4-i,5) in jug2:
            return 2, (4-i,5)

def domino(deck, jug1, jug2):

    tirades = [0,0,0,0,0,0,0]
    torn, inicial = inici(jug1, jug2)

    # Torn inicial:
    if torn == 1:
        jug1.remove(inicial)
        # print("Jugador 1 tira ", inicial)
    if torn == 2:
        jug2.remove(inicial)
        # print("Jugador 2 tira ", inicial)
    torn = 3-torn
    
    tirades[inicial[0]] += 1
    tirades[inicial[1]] += 1
    esq = inicial[0]
    dre = inicial[1]
    cuaEsq = []
    cuaDre = []

    while True:
        # print("Tauler: ", reverse(cuaDre) + [inicial] + cuaEsq)
        # print("Jugador 1: ", jug1)
        # print("Jugador 2: ", jug2)
        # print()

        if torn == 1:
            # Torn jugador 1:
            # Estratègia una mica millor

            tirat = False

            quants = [0,0,0,0,0,0,0]
            for fitxa in jug1:
                quants[fitxa[0]] += 1
                quants[fitxa[1]] += 1
            
            if quants[esq] + quants[dre] == 0:
                if len(deck) > 0:
                    robada = deck.pop()
                    jug1 += [robada]
                    # print("Jugador 1 roba ", robada)

            elif quants[dre] > quants[esq]:
                for fitxa in jug1:
                    if fitxa[0] == dre:
                        cuaDre += [fitxa]
                        dre = fitxa[1]
                        jug1.remove(fitxa)
                        tirat = True
                        torn = 2
                        break
                    if fitxa[1] == dre:
                        cuaDre += [(fitxa[1],fitxa[0])]
                        dre = fitxa[0]
                        jug1.remove(fitxa)
                        tirat = True
                        torn = 2
                        break

            else:
                for fitxa in jug1:
                    if fitxa[0] == esq:
                        cuaEsq += [fitxa]
                        esq = fitxa[1]
                        jug1.remove(fitxa)
                        tirat = True
                        torn = 2
                        break
                    if fitxa[1] == esq:
                        cuaEsq += [(fitxa[1],fitxa[0])]
                        esq = fitxa[0]
                        jug1.remove(fitxa)
                        tirat = True
                        torn = 2
                        break
                
            if tirat:
                # print("Jugador 1 tira ", fitxa)
                tirades[fitxa[0]] += 1
                tirades[fitxa[1]] += 1
                if len(jug1) == 0:
                    # print("Tauler: ", reverse(cuaDre) + [inicial] + cuaEsq)
                    # print("Guanyador: Jugador 1")
                    # print("Jugador 2: ", jug2)
                    return 1
            
            torn = 2

        if torn == 2:
            # Torn jugador 2:
            # Estratègia bàsica de tirada
            random.shuffle(jug2)
            tirat = False
            for fitxa in jug2:
                if fitxa[0] == esq:
                    cuaEsq += [fitxa]
                    esq = fitxa[1]
                    jug2.remove(fitxa)
                    tirat = True
                    torn = 1
                    break
                if fitxa[1] == esq:
                    cuaEsq += [(fitxa[1],fitxa[0])]
                    esq = fitxa[0]
                    jug2.remove(fitxa)
                    tirat = True
                    torn = 1
                    break
                if fitxa[0] == dre:
                    cuaDre += [fitxa]
                    dre = fitxa[1]
                    jug2.remove(fitxa)
                    tirat = True
                    torn = 1
                    break
                if fitxa[1] == dre:
                    cuaDre += [(fitxa[1],fitxa[0])]
                    dre = fitxa[0]
                    jug2.remove(fitxa)
                    tirat = True
                    torn = 1
                    break
            if tirat:
                # print("Jugador 2 tira ", fitxa)
                tirades[fitxa[0]] += 1
                tirades[fitxa[1]] += 1
                if len(jug2) == 0:
                    # print("Tauler: ", reverse(cuaDre) + [inicial] + cuaEsq)
                    # print("Guanyador: Jugador 2")
                    # print("Jugador 1: ", jug1)
                    return 2
            elif len(deck) > 0:
                robada = deck.pop()
                jug2 += [robada]
                # print("Jugador 2 roba ", robada)
            torn = 1
 
        if esq == dre and tirades[esq] == 8:
            # print("Joc tancat")
            # print("Tauler: ", reverse(cuaDre) + [inicial] + cuaEsq)
            # print("Jugador 1: ", jug1)
            # print("Jugador 2: ", jug2)
            return 0


# Simulació d'una partida aleatòria:
# deck, jug1, jug2 = fitxes()
# print("Deck: ", deck)
# print("Jugador 1: ", jug1)
# print("Jugador 2: ", jug2)


# Simulació de diverses partides:
resultats = [0, 0, 0]
for i in range(100000):
    deck, jug1, jug2 = fitxes()
    guanyador = domino (deck, jug1, jug2)
    resultats[guanyador] += 1

S = sum(resultats)
print("Partides guanyades pel jugador 1: ", resultats[1]/S*100, "%")
print("Partides guanyades pel jugador 2: ", resultats[2]/S*100, "%")
print("Partides acabades en taules: ", resultats[0]/S*100, "%")