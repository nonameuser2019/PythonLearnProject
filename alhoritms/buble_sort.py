def buble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


arr = [7, 1, 4, 2, 8, 0]
print(buble_sort(arr))