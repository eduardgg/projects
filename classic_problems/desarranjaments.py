# Permutacions:
def permutacions(n):
    v = [-1]*n
    u = [False]*n
    def perm(n, i):
        if i == n:
            print([elem + 1 for elem in v])
        for j in range(n):
            if not u[j]:
                v[i] = j
                u[j] = True
                perm(n, i+1)
                v[i] = -1
                u[j] = False
        return
    print("Permutacions de " + str(n) + ":")
    perm(n, 0)
    print()

# Desarranjaments:
def desarranjaments(n):
    v = [-1]*n
    u = [False]*n
    def derr(n, i):
        if i == n:
            print([elem + 1 for elem in v])
        for j in range(n):
            if i != j and not u[j]:
                v[i] = j
                u[j] = True
                derr(n, i+1)
                v[i] = -1
                u[j] = False
        return
    print("Desarranjaments de " + str(n) + ":")
    derr(n, 0)
    print()

n = 5
permutacions(n)
desarranjaments(n)