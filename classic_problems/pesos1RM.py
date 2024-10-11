
reps_std = [1,2,3,4,5,6,7,8,9,10,11,12,15]
pesos_std = [100,95,93,90,87,85,83,80,77,75,70,67,65]


def print1RM(reps, pes, formula):
    print("    " + str(reps) + " with " + str(pes) + " kg: 1RM should be " + str(formula) + " kg.")

def gorostiaga1RM(pes, reps):
    C = 0.0278
    maxRep = pesos[i]/(1-C*(reps[i] + 1))
    return maxRep

# DOMINADES
meu_pes = 75
pesos = [10, 20, 30, 40]
reps = [15, 9, 7, 4]
print("PULL UP:")
for i in range(len(pesos)):
    print("  Model 1: Fórmula de Gorostiaga")
    maxRep = gorostiaga1RM(pesos[i] + meu_pes, reps[i]) - meu_pes
    print1RM(reps[i], pesos[i], maxRep)

# BENCH PRESS
pesos = [80, 90, 95, 100]
reps = [14, 7, 4, 2]
print("BENCH PRESS:")
for i in range(len(pesos)):
    print("  Model 1: Fórmula de Gorostiaga")
    maxRep = gorostiaga1RM(pesos[i], reps[i])
    print1RM(reps[i], pesos[i], maxRep)