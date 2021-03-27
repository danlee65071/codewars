def row_sum_odd_numbers(n):
    num = 1
    res = 0
    if n == 1:
        return 1
    for i in range(n):
        num += 2 * i
    for i in range(n):
        res += num
        num += 2
    return res

