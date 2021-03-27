def snail(snail_map):
    if len(snail_map) == 0:
        return []
    if len(snail_map) == 1:
        return snail_map[0]
    res = snail_map[0] + [x[-1] for x in snail_map[1:-1]] + \
          snail_map[-1][::-1] + [x[0] for x in snail_map[-2:0:-1]]
    snail_map = [x[1:-1] for x in snail_map[1:-1]]
    return res + snail(snail_map)
