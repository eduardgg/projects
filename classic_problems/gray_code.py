
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end = " ")
        print()

def gray_code(n):
    if n == 0:
        return []
    if n == 1:
        return [[0],[1]]
    # G = [[0 for i in range(n)] for j in range(2**(n-1))]
    G = gray_code(n-1)
    for i in range(2**(n-1)):
        G[i] = [0] + G[i]
    for i in range(2**(n-1)):
        v = [1] + G[2**(n-1)-1-i][1:]
        G = G + [v]
    return G

print_matrix(gray_code(4))