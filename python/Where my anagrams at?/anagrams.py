"""from collections import Counter

def anagrams(word, words):
    return [x for x in words if Counter(x) == Counter(word)]"""


# Решение в 1 строку
def anagrams(word, words):
    return [x for x in words if sorted(word) == sorted(x)]
