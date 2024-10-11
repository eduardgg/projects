
# En aquest codi trobem tots els camins que es poden fer en un 
# graf sense repetir vèrtexos, a través d'un matriu de programació
# dinàmica. El primer paràmetre és el conjunt de nodes visitats,
# codificat en binari, i el segon és l'últim node que s'ha vist.
# El valor de l'array serà True si és possible o False si no.

# Si la longitud és igual al nombre de nodes del graf, serà un
# camí hamiltonià i si, a més, el primer i l'últim nodes d'alguna
# combinació estan connectats, serà un cicle hamiltonià.
# És un problema NP i comprovar-ho sense dp (backtracking) tindria
# un cost factorial O(n!), que queda reduït amb dp a O(n^2·2^n).

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 0]
]

n = len(graph)

dp = [[False for _ in range(n)] for _ in range(1 << n)]
for i in range(n):
    dp[1 << i][i] = True

top = 0
for i in range(1 << n):
    for j in range(n):
        if dp[i][j]:
            top = max(top, bin(i).count('1'))
            for k in range(n):
                if not i & (1 << k) and graph[j][k]:
                    dp[i | (1 << k)][k] = True

print(top)

# Amb aquest codi trivial podem escriure un camí hamiltonià
# (es podria editar amb backtracking per reportar-los tots,
# o bé afegir la condició d'encaix per cicles hamiltonians.
ok = False
for i in range(1 << n):
    for j in range(n):
        if dp[i][j] and bin(i).count('1') == top:
            nodes = []
            x, y = i, j
            while x > 0:
                nodes.append(j)
                x ^= (1 << j)
                for k in range(n):
                    if dp[x][k] and graph[j][k]:
                        j = k
                        break
            ok = True
            break
    if ok:
        break
print(nodes)