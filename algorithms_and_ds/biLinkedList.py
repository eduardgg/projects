
class BLLNode(object):
    
    def __init__(self, val=None, pre=None, nex=None):
        self.val = val
        self.pre = pre
        self.nex = nex



def vecToBLL(v):
    root = BLLNode()
    copy = root
    for i in v[0:len(v)-1]:
        copy.val = i
        copy.nex = BLLNode()
        prev = copy
        copy = copy.nex
        copy.pre = prev
    if len(v) > 0:
        copy.val = v[-1]
    return root

def deleteNode(n):
    if n.pre and n.nex:
        (n.pre).nex = n.nex
        (n.nex).pre = n.pre
        n = n.pre
    elif n.pre:
        (n.pre).nex = None
        n = n.pre
    elif n.nex:
        (n.nex).pre = None
        n = n.nex

def printBLL(l):
    while True:
        if l.pre == None:
            break
        l = l.pre
    while l:
        print(l.val, end=" ")
        l = l.nex
    print()