
def qSort(L):
    if len(L) <= 0:
        return L
    return qSort([x for x in L[1:] if x<L[0]]) + L[0:1] + qSort([x for x in L[1:] if x>L[0]])

list = [44,33,22,5,77,55,999,22,33,8]
print(qSort(list))
