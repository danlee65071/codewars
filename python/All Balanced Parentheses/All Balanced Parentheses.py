def balanced_parens_algo(opened, closed, n, arr, str):
    if opened == n and closed == n:
        balanced_parens_algo(opened - 1, closed, n, arr, str + '(')
    if opened == 0 and closed == 0:
        arr.append(str)
        return
    if opened != 0 and closed >= opened and (opened != n or closed != n):
        balanced_parens_algo(opened - 1, closed, n, arr, str + '(')
    if closed != 0 and closed >= opened and (opened != n or closed != n):
        balanced_parens_algo(opened, closed - 1, n, arr, str + ')')


def balanced_parens(n):
    arr = []
    str = ''
    if n == 0:
        arr.append(str)
    else:
        balanced_parens_algo(n, n, n, arr, str)
    return arr


print(balanced_parens(0))

# Решение в 1 строку
# def balanced_parens(n):
#     return list(set([p[:i] + "()" + p[i:] for p in balanced_parens(n - 1) for i in range(0, len(p))])) if n > 1 else ([""], ["()"])[n]
