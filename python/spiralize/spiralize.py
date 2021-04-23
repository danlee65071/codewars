def spiralize(size):
    spiral = [[0 for i in range(size)] for i in range(size)]
    start_i = i = 0
    start_j = j = 0
    len_spiral = size
    is_initial_spiral = 1
    while len_spiral > 0:
        if is_initial_spiral == 0:
            spiral[int((size - len_spiral)/2)][int((size - len_spiral)/2 - 1)] = 1
        if len_spiral == 1:
            spiral[start_i][start_j] = 1
        if len_spiral == 2:
            spiral[start_i][start_j] = 1
            spiral[start_i][start_j + 1] = 1
            spiral[start_i + 1][start_j + 1] = 1
            break ;
        # go right
        for j in range(start_j, len_spiral + start_j):
            spiral[i][j] = 1
        # go down
        for i in range(start_i, len_spiral + start_i):
            spiral[i][j] = 1
        # go left
        for j in reversed(range(start_j, len_spiral + start_j)):
            spiral[i][j] = 1
        # go up
        for i in range(len_spiral - 1 + start_i, start_i + 1, -1):
            spiral[i][j] = 1
        is_initial_spiral = 0
        start_i += 2
        start_j += 2
        len_spiral -= 4
    return spiral


size_spiral = 5
spiral = spiralize(size_spiral)
for i in range(size_spiral):
    print(spiral[i])

print()
size_spiral = 10
spiral = spiralize(size_spiral)
for i in range(size_spiral):
    print(spiral[i])
