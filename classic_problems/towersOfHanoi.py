import sys
sys.path.insert(0, r'C:\Users\gonzalvo\Documents\Pycode\sedgewick\stdlib-python')
import stdio

def moves(n, left):
    if n == 0:
        return
    moves(n-1, not left)
    if left:
        stdio.writeln(str(n) + ' left')
    else:
        stdio.writeln(str(n) + ' right')
    moves(n-1, not left)

n = 3
moves(n, True)