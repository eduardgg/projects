
# Aquesta estructura de dades permet mantenir un conjunt
# d'intervals disjunts i fer operacions amb ells, com la unió,
# intersecció, o correcta "intervalització".

# Els elements són intervals [a, b] ordenats segons la primera
# coordenada a. Això fa que, a l'intervalitzar correctament,
# quedin també ordenats segons b (ja que, si no, hi hauria algun
# interval contingut dins un altre).
# Per trobar doncs intervals podem usar una funció "bisect".
# Per eliminar-ne mantenint-los ordenats, usem un BST.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b
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
            



# TODO:

class Intervals:

    def __init__(self, v):
        # Aquesta funció inicialitza i "intervalitza"
        # a partir dels intervals (a, b) en v
        v.sort()
        self.ints = []
        for interval in v:
            self.union(interval)

    def intervalize(self):

    def union(self, interval):

    def union(self, other):

    def intersection(self, interval):

    def intersection(self, other):
