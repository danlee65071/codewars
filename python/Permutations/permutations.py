def permutations(string):
    list_string = []
    if len(string) <= 1:
        return string
    for perm in permutations(string[1:]):
        for i in range(len(string)):
            list_string.append(perm[:i] + string[0: 1] + perm[i:])
    return list(set(list_string))
