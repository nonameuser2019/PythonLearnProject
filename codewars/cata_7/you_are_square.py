from math import sqrt


def is_square(n):
    return True if n >= 0 and sqrt(n) % 1 == 0 else False


if __name__ == '__main__':
    assert is_square(4)
    assert not is_square(3)
