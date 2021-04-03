def sum_pairs(ints, s):
    cache_set = set()
    for i in ints:
        if s - i in cache_set:
            return [s - i, i]
        cache_set.add(i)

'''def sum_pairs(ints, s):
    for i in range(1, len(ints)):
        subints = ints[: i]
        if s - ints[i] in subints:
            return [s - ints[i], ints[i]]'''


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))
