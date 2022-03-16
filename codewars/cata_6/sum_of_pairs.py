# this cata isn't complete
def sum_pairs(ints, s):
    result = []
    for i in range(len(ints)):
        if ints[i] != s:
            for j in range(i+1, len(ints)):
                if ints[i] + ints[j] == s:
                    result.append(ints[i])
                    result.append(ints[j])
                    return result
        else:
            continue


l1= [1, 4, 8, 7, 3, 15]
l2 = [1, -2, 3, 0, -6, 1]
l3 = [10, 5, 2, 3, 7, 5]
assert sum_pairs(l1, 8) == [1, 7]
assert sum_pairs(l2, -6) == [0, -6]
assert sum_pairs(l3, 10) == [3, 7]