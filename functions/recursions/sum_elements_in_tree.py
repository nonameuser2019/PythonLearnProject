import free as free


def sum_tree(array):
    total = 0
    for elem in array:
        if not isinstance(elem, list):
            # check if the item not a list
            total += elem
        else:
            total += sum_tree(elem)
    return total


def sum_tree_quee(array):
    total = 0
    items = list(array)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            total += front
        else:
            items[:0] = front
    return total


def sum_tree_stack(array):
    total = 0
    items = list(array)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            total += front
        else:
            items.extend(front)
    return total

data = [1, [2, 3, [4]], 5, [2, [3]]]
assert sum_tree(data) == 20
assert sum_tree_quee(data) == 20
assert sum_tree_stack(data) == 20

func_count = [x for x in dir(sum_tree_stack) if not x.startswith('__')]
print(func_count)
