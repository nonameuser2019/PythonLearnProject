def checkio(array: list) -> int:
    if not array:
        return 0
    return sum([array[i] for i in range(len(array)) if i % 2 == 0]) * array[-1]


if __name__ == '__main__':
    print('Example:')
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, f"(1+5)*5=30 : {checkio([1, 3, 5])}"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")