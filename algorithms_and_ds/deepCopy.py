
def deepCopy(v):
    if type(v) == list:
        return [deepCopy(e) for e in v]
    return v

def wrongCopy(v):
    if type(v) == list:
        return [e for e in v]
    return v

b = [[1], [], [0,[9,7,1],2], [3,4,[2]], [5], []]



print("b before deep copy:", b)
a1 = deepCopy(b)
print("deep copy is:", a1)
a1[2][1] = [3,4]
print("deep copy after change is:", a1)
print("b after deep copy: ", b)
a2 = wrongCopy(b)
a2[2][1] = [3,4]
print("wrong copy after change is:", a2)
print("b after wrong copy:", b)
