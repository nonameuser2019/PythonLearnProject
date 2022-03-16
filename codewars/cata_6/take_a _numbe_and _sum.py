# not finished

def sum_dig_pow(a, b):
    result = []
    for i in range(a, b + 1):
        s = sum([int(i) ** len(str(i)) for i in str(i)])
        if s <= b:
            result.append(s)
    return result

print(sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9])
assert sum_dig_pow(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]