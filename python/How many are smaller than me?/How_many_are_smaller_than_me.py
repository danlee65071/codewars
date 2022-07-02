def smaller(arr):
    return [sum([el > j for j in arr[id + 1:]]) for id, el in enumerate(arr)]
