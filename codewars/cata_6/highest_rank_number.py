def highest_rank(arr: list):
    result = 0
    count = 0
    arr.sort()
    for i in arr:
         if arr.count(i) >= count:
            result = i
            count = arr.count(i)
    return result

assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12

