def disemvowel(string):
    vowel_set = set('aeiouAEIOU')
    res = ""
    for i in string:
        if i not in vowel_set:
            res += i
    return res
