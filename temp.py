
arr = [1, 2, 3, 4, 5]
arr_2 = [1, 5]

result = []

def intersect(arr_1, arr_2):
    result = []
    for item in arr_2:
        if item in arr_1:
            result.append(item)
    return list(set(result))

assert intersect(arr, arr_2) == [1, 5]


