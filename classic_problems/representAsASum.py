
def represent(n, value):

    if n == 0 and value == 0:
        return []

    total = sum(range(1, n + 1))

    if abs(value) > total or (total - value) % 2 != 0:
        return False

    if value >= 0:
        return represent(n - 1, value - n) + [n]
    else:
        return represent(n - 1, value + n) + [-n]


for v in (7, 15, 22, 33, 40, 47):
    
    print(v, end='')
    result = represent(9, v)
    if not result:
        print(' is not representable')
    else:
        print('=', end='')
        for i in result:
            if i < 0:
                print(f'{i}', end='')
            else:
                print(f'+{i}', end='')
        print()