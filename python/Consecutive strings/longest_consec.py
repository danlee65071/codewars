"""def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ''
    max_len = 0
    for i in range(n-k+1):
        consec_len = 0
        for j in range(i, k+i):
            consec_len += len(strarr[j])
        if consec_len > max_len:
            max_len = consec_len
            first_ind_longest_consec = i
    res = ''.join(strarr[first_ind_longest_consec:k+first_ind_longest_consec])
    return res"""


# Решение в 1 строку
def longest_consec(strarr, k):
    return '' if len(strarr) == 0 or k > len(strarr) or k <= 0 else \
        max([''.join(strarr[i:i + k]) for i in range(len(strarr)-k+1)], key=len)
