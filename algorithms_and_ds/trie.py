
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.count = 0  # Comptador d'ocurrències

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True
        current_node.count += 1

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return 0
            current_node = current_node.children[char]
        if current_node.is_end_of_word:
            return current_node.count
        return 0

# Exemple d'ús
trie = Trie()
trie.insert("hola")
trie.insert("hola")
trie.insert("adéu")

print(trie.search("hola"))  # Output: 2
print(trie.search("adéu"))  # Output: 1
print(trie.search("hol"))   # Output: 0
