
# Implementació d'un Binary Search Tree (fet amb Chat GPT)
# Permet mantenir elements ordenats i en permet l'eliminació
# eficient, a diferència de la funció pop(i) en un array.
# Aquesta estructura no permet elements repetits.
# És, per tant, equivalent a un "SORTED SET" (set, en C++).

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursively(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursively(node.right, value)
        # Si el valor ja existeix, no fem res

    def delete(self, value):
        self.root = self._delete_recursively(self.root, value)

    def minim(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def maxim(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def _delete_recursively(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursively(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursively(node.right, value)
        else:
            # Cas en què trobem el node a eliminar
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node amb dos fills: troba el mínim del subarbre dret
            min_node = self._find_min(node.right)
            node.value = min_node.value
            node.right = self._delete_recursively(node.right, min_node.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        return self._inorder_recursively(self.root, [])

    def _inorder_recursively(self, node, result):
        if node is not None:
            self._inorder_recursively(node.left, result)
            result.append(node.value)
            self._inorder_recursively(node.right, result)
        return result
    
    def first_greater(self, value):
        return self.first_greater_recursively(self.root, value)

    def first_greater_recursively(self, node, value):
        if node is None:
            return None

        if node.value == value:
            return node.value
        elif node.value < value:
            return self.first_greater_recursively(node.right, value)
        else:
            left_result = self.first_greater_recursively(node.left, value)
            if left_result is not None:
                return left_result
            else:
                return node.value
    
    def first_less(self, value):
        return self.first_less_recursively(self.root, value)

    def first_less_recursively(self, node, value):
        if node is None:
            return None

        if node.value == value:
            return node.value
        elif node.value > value:
            return self.first_less_recursively(node.left, value)
        else:
            left_result = self.first_less_recursively(node.right, value)
            if left_result is not None:
                return left_result
            else:
                return node.value

# Exemple d'ús:
bst = BST()
bst.insert(5)
bst.insert(1)
bst.insert(11)
bst.insert(2)
bst.insert(4)
bst.insert(14)
bst.insert(16)
bst.insert(8)

print("Inorder traversal:", bst.inorder_traversal())
print("L'arrel de l'arbre és ", bst.root.value)

bst.delete(4)
print("Inorder traversal after deleting 4:", bst.inorder_traversal())
print("L'arrel de l'arbre és ", bst.root.value)

bst.delete(5)
print("Inorder traversal after deleting 5:", bst.inorder_traversal())
print("L'arrel de l'arbre és ", bst.root.value)

for i in range(20):
    print("Primer element superior a", i, "és:", bst.first_greater(i))
print()
for i in range(20):
    print("Primer element inferior a", i, "és:", bst.first_less(i))

print()
print("El mínim element del BST és", bst.minim())
print("El màxim element del BST és", bst.maxim())