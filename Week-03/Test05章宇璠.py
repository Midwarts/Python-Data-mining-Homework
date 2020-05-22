from __future__ import division

def permutation(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i:i + 1]
        if n == 1:
            yield v
        else:
            rest = items[:i] + items[i + 1:]
            for p in permutation(rest, n - 1):
                yield v + p


def F(a, b):
    arr = []
    for i in a:
        for j in b:
            arr.append("(" + i + "+" + j + ")")
            arr.append("(" + i + "-" + j + ")")
            arr.append("(" + j + "-" + i + ")")
            arr.append("(" + i + "*" + j + ")")

            eval(j) != 0 and arr.append("(" + i + "/" + j + ")")
            eval(i) != 0 and arr.append("(" + j + "/" + i + ")")
    return arr


def main(arr):
    vaild_exprs = []
    for lst in permutation(arr):
        a_expr = F(F(F([lst[0]], [lst[1]]), [lst[2]]), [lst[3]])

        b_expr = F(F([lst[0]], [lst[1]]), F([lst[2]], [lst[3]]))
        all_expr = a_expr + b_expr
        for expr in all_expr:
            if abs(eval(expr) - 24) < 0.0001:
                vaild_exprs.append(expr)
                print(expr)
    print('None' if len(vaild_exprs) == 0 else 'Total:{}'.format(len(vaild_exprs)))


if __name__ == '__main__':
    sample = [2, 5, 6, 4]
    arr = [str(i) if i >= 0 else '(' + str(i) + ')' for i in sample]
    main(arr)
