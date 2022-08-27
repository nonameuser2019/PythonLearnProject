def square_digits(num):
    return int(''.join([str(int(x) ** 2) for x in str(num)]))


if __name__ == '__main__':
    assert square_digits(9119) == 811181