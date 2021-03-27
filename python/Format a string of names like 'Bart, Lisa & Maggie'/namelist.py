def namelist(names):
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]['name']
    else:
        res = ''
        for i in names:
            if i == names[-2]:
                res += i['name'] + ' & '
            elif i == names[-1]:
                res += i['name']
            elif i != names[-2]:
                res += i['name'] + ', '
        return res
