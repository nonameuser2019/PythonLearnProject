
def binary_search(arr, item):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
            mid = (low + high) // 2
        elif guess > item:
            high = mid - 1
            mid = (low + high) // 2


if __name__ == '__main__':
    search_number = 43
    data = list(range(1, 11))
    print(binary_search(data, 11))
