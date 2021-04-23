from math import sqrt
import time


'''def decompose(n, res=[], target=0):
    if n == 1 and 1 not in res:
        res = [1] + res
        return res
    elif 1 in res and len(res) > 1:
        res.pop(0)
        res.pop(0)
        return res
    elif 1 in res and len(res) == 1:
        res.pop(0)
        return
    elif n == 0:
        res = [0] + res
        return res
    else:
        if target == 0:
            target = n
        for i in range(n-1, 0, -1):
            sum_of_squares = sum(map(lambda x: x * x, res), i ** 2)
            if sum_of_squares < target ** 2:
                res = decompose(i, [i] + res, target)
            if sum_of_squares == target ** 2:
                return [i] + res
    return res'''
def decompose(n):
    res = []
    target = n ** 2
    i = n - 1
    while i > 0:
        if i ** 2 < target:
            target -= i ** 2
            res = [i] + res
        elif i ** 2 == target:
            if i in res:
                res.pop(0)
                target += i ** 2 + res[0] ** 2 + 1
                res[0] -= 1
                continue
            res = [i] + res
            return res
        i = int(sqrt(target))



print(decompose(5))
print(decompose(8))
print(decompose(11))
print(decompose(50))
start = time.time()
print(decompose(1000))
print(time.time() - start)
