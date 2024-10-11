
def perms(w, pos):

    if pos == len(w):
        print(paraula)
        return
    for i in range(len(w)):
        if not usat[i]:
            paraula[pos] = w[i]
            usat[i] = True
            perms(w, pos+1)
            usat[i] = False
    return

s = "oxma"
usat = [False] * len(s)
paraula = [''] * len(s)
perms(s, 0)