def find_outlier(integers: list):
    even = []
    odd = []
    for i in integers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even[0] if len(even) < len(odd) else odd[0]


assert find_outlier([2, 4, 6, 8, 10, 3]) == 3
assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11