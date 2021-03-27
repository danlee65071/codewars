def snail_oleg(map_s):
    if len(map_s) == 1:
        return map_s[0]
    res = [map_s[0][0]] + [x[0] for x in map_s[1:-1]] + map_s[-1] + \
          [x[-1] for x in map_s[-2:0:-1]] + map_s[0][-1:0:-1]
    map_s = [x[1:-1] for x in map_s[1:-1]]
    return res + snail_oleg(map_s)


def reverse_snail_oleg(map_s):
    res = snail_oleg(map_s)
    return res[::-1]


map_s = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(reverse_snail_oleg(map_s))
map_s = [[3, 4, 5, 7, 7],
         [2, 1, 2, 5, 5],
         [1, 1, 0, 4, 5],
         [3, 3, 3, 5, 6],
         [1, 2, 3, 4, 5]]
print(reverse_snail_oleg(map_s))
