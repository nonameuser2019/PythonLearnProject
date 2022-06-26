def fib(n):
    if 2 <= n < 4:
        return n
    elif n >= 4:
        return fib(n -1) + fib(n-2)
    return 1


if __name__ == '__main__':
    fib_nums = fib(5)
    print(fib_nums)