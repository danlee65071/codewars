from bisect import bisect_left
import array

def smaller(arr):
    sorted = array.array('q')
    result = [0] * len(arr)
    p = len(arr) - 1
    for n in reversed(arr):
        i = bisect_left(sorted, n)
        sorted.insert(i, n)
        result[p] = i
        p -= 1
    return result