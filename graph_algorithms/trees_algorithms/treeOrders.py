
# Problemes d'arbres i ordres:
# Donat un arbre binari, imprimir el preordre, inordre i postordre 
# Donat l'in-order i el pre-order d'un arbre, trobar l'arbre.

class Node():

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def printPreorder(root):
    if not root:
        return
    print(root.val, end=" ")
    printPreorder(root.left)
    printPreorder(root.right)

def printInorder(root):
    if not root:
        return
    printInorder(root.left)
    print(root.val, end=" ")
    printInorder(root.right)

def printPostorder(root):
    if not root:
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.val, end=" ")

def f(p, i):
    if len(p) != len(i):
        print("Lenght of preorder and inorder must be the same")
        return
    if len(p) == 0:
        return None
    if len(p) == 1:
        return Node(p[0])
        
    root = p[0]
    for j in range(len(i)):
        if i[j] == root:
            break
    n = Node(root)
    n.left = f(p[1:j+1], i[:j])
    n.right = f(p[j+1:], i[j+1:])
    return n



preorder0 = [1,2,4,5,6,3,7]
inorder0 = [4,2,6,5,1,3,7]

root = f(preorder0, inorder0)
printPreorder(root)
print()
printInorder(root)
print()
printPostorder(root)
print()

"""
print(root.val)
print(root.left.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.left.right.left.val)
print(root.right.val)
print(root.right.right.val)
"""