def persistence(n):
    count = 0
    while len(str(n)) > 1:
        n = (int(x) * int(x) for x in str(n))
        count += 1
    return count


def main():
    assert persistence(39) == 3
    assert persistence(999) == 4
    assert persistence(4) == 0


if __name__ == '__main__':
    main()