def sum_pairs(ints, s):
    cache_set = set()
    for i in ints:
        if s - i in cache_set:
            return [s - i, i]
        cache_set.add(i)
