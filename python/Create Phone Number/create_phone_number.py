def create_phone_number(n):
    str_n = [str(i) for i in n]
    return ('({0}) {1}-{2}'.format(''.join(str_n[0:3]),
                                   ''.join(str_n[3:6]), ''.join(str_n[6:])))
