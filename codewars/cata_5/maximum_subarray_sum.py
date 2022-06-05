def max_sequence(arr):
    result = []
    if not arr:
        return 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            result.append(sum(arr[i:j + 1]))
    return max(result) if max(result) > 0 else 0

if __name__ == '__main__':
    data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_sequence(data) == 6
