def DNA_strand(dna):
    res = ''
    for i in dna:
        if i == 'A':
            res += 'T'
        elif i == 'T':
            res += 'A'
        elif i == 'C':
            res += 'G'
        elif i == 'G':
            res += 'C'
    return res
