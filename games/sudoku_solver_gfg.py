
class Solution:
    
    def solveSudoku(self, sudoku):
        
        def finished():
            tots = {i+1 for i in range(9)}
            if any([{sudoku[i][j] for i in range(9)} != tots for j in range(9)]):
                return False
            if any([{sudoku[i][j] for j in range(9)} != tots for i in range(9)]):
                return False
            if any([{sudoku[3*x+i][3*y+j] for i in range(3) for j in range(3)} != tots for x in range(3) for y in range(3)]):
                return False
            return True
        
        def opcions(i, j):
            opcs = set(range(1, 10))
            opcs -= set(sudoku[i])
            opcs -= {sudoku[x][j] for x in range(9)}
            bi, bj = 3 * (i // 3), 3 * (j // 3)
            opcs -= {sudoku[bi + x][bj + y] for x in range(3) for y in range(3)}
            return opcs
        
        def bruteForce():
            if finished():
                return True
            min_opcions = (10, None, None, None)
            for i in range(9):
                for j in range(9):
                    if sudoku[i][j] == 0:
                        opcs = opcions(i, j)
                        if not opcs:
                            return False
                        if len(opcs) < min_opcions[0]:
                            min_opcions = (len(opcs), i, j, opcs)
            _, i, j, opcionsMillor = min_opcions
            for val in opcionsMillor:
                sudoku[i][j] = val
                if bruteForce():
                    return True
                sudoku[i][j] = 0  
            return False
        
        bruteForce()



if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")