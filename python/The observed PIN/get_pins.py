from itertools import product


def get_pins(observed):
    combination_dict = {'1': ['1', '2', '4'], '2': ['1', '2', '3', '5'],
                        '3': ['2', '3', '6'], '4': ['1', '4', '5', '7'],
                        '5': ['2', '4', '5', '6', '8'],
                        '6': ['3', '5', '6', '9'], '7': ['4', '7', '8'],
                        '8': ['0', '5', '7', '8', '9'],
                        '9': ['6', '8', '9'], '0': ['0', '8']}
    tmp = [combination_dict[i] for i in observed]
    comb_pins = list(product(*tmp))
    res = [''.join(i) for i in comb_pins]
    return res
