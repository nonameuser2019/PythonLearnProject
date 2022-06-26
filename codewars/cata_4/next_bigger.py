def next_bigger(n):
    num = [int(i) for i in str(n)]
    if len(num) == 2:
        if num[1] > num[0]:
            num[1], num[0] = num[0], num[1]
            return int(''.join([str(i) for i in num]))
        else:
            return -1
    for i in range(len(num) - 1, -1, -1):
        for j in range(i - 1, 0, -1):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]
                return int(''.join([str(i) for i in num]))
    return -1

if __name__ == '__main__':
    # assert next_bigger(12) == 21, print(next_bigger(12))
    # assert next_bigger(513) == 531, print(next_bigger(513))
    # assert next_bigger(2017) == 2071
    print(next_bigger(144))