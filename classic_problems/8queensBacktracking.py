# If we want to return the number of different combinations,
# activate the commented lines and remove the "exit()" line

def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    # global C
    if len(perm) == n:
        # C += 1
        # return
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()

# C = 0
extend(perm = [], n = 8)
# print(C)