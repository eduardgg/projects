import bisect

class SortedSet:
    
    def __init__(self, iterable=None):
        self._items = []
        if iterable:
            for item in iterable:
                self.add(item)

    def __contains__(self, item):
        i = bisect.bisect_left(self._items, item)
        return i < len(self._items) and self._items[i] == item

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def add(self, item):
        i = bisect.bisect_left(self._items, item)
        if i == len(self._items) or self._items[i] != item:
            self._items.insert(i, item)

    def remove(self, item):
        i = bisect.bisect_left(self._items, item)
        if i < len(self._items) and self._items[i] == item:
            self._items.pop(i)
        else:
            raise KeyError(f"Item {item} not found in SortedSet")

    def __getitem__(self, index):
        return self._items[index]

    def __repr__(self):
        return f"SortedSet({self._items})"

    def first(self):
        """Return the smallest element"""
        if not self._items:
            raise IndexError("SortedSet is empty")
        return self._items[0]

    def last(self):
        """Return the largest element"""
        if not self._items:
            raise IndexError("SortedSet is empty")
        return self._items[-1]

    def pop(self, index=-1):
        """Remove and return the element at the given index (default: the last element)"""
        return self._items.pop(index)



# Test Cases:
my_set = SortedSet([5, 1, 3, 9])
print("Sorted set inicial:", my_set)

my_set.add(7)
print("Després d'afegir 7:", my_set)

my_set.remove(3)
print("Després d'eliminar 3:", my_set)

print("Primer element:", my_set.first())
print("Últim element:", my_set.last())

print("Iterem pel conjunt:")
for element in my_set:
    print(element)
