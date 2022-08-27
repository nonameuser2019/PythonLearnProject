def fib(n):
    if 2 <= n < 4:
        return n
    elif n >= 4:
        return fib(n -1) + fib(n-2)
    return 1


def fib_2(n):
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b


if __name__ == '__main__':
    assert fib(4) == 5, print(fib(5))
    assert fib_2(4) == 5