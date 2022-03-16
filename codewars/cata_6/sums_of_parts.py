def parts_sums(ls):
    res = [sum(ls)]
    for i in range(1, len(ls)):
        res.append(res[i -1] - ls[i -1])
    if len(ls) > 0:
        res.append(0)
    return res

def parts_sums_2(ls):
    # this decision work but it's too long
    res = [sum(ls[i: len(ls)]) for i in range(len(ls))]
    res.append(0)
    return res



assert parts_sums([0, 1, 3, 6, 10]) == [20, 20, 19, 16, 10, 0]
assert parts_sums([1, 2, 3, 4, 5, 6]) == [21, 20, 18, 15, 11, 6, 0]
assert parts_sums([]) == [0], f'{parts_sums([])}'

assert parts_sums_2([0, 1, 3, 6, 10]) == [20, 20, 19, 16, 10, 0]
assert parts_sums_2([1, 2, 3, 4, 5, 6]) == [21, 20, 18, 15, 11, 6, 0]
assert parts_sums_2([]) == [0]