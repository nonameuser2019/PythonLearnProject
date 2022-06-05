# сортировка выбором алгоритм который сортирует массив путем нахждения мин. эл масива на каждой итерации и добавения его
# в результирующий масив одновременно удаляя из исходного

def find_min(arr):
    min_elem = arr[0]
    min_idex = 0
    for i in range(len(arr)):
        if arr[i] < min_elem:
            min_elem = arr[i]
            min_idex = i
    return min_idex


def select_sort(arr):
    result = []
    for i in range(len(arr)):
        result.append(arr.pop(find_min(arr)))
    return result


if __name__ == '__main__':
    data = [3, 7, -3, 4, 9]
    print(select_sort(data))
