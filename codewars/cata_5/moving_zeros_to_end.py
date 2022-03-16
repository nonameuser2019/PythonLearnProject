def move_zeros(array):
    zero = []
    result = []
    for elem in array:
        if elem == 0:
            zero.append(elem)
        else:
            result.append(elem)
    return result + zero


def move_to_zero_2(array):
    zero = [i for i in array if i == 0]
    not_zero = [i for i in array if i != 0]
    return not_zero + zero


assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
assert move_to_zero_2([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]