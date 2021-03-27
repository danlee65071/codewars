def find_outlier(integers):
    is_even = 0
    is_odd = 0
    index_even = 0
    index_odd = 0
    index = 0
    res = 0
    for i in integers:
        if i % 2 == 0:
            is_even += 1
            index_even = index
        elif i % 2 != 0:
            is_odd += 1
            index_odd = index
        index += 1
    if is_even == 1:
        res = integers[index_even]
    elif is_odd == 1:
        res = integers[index_odd]
    return res
