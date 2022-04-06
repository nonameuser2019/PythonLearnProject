def descending_order(num):
    result = [int(x) for x in str(num)]
    result.sort(reverse=True)
    return int(''.join([str(x) for x in result]))


def descending_order2(num):
    return int(''.join(sorted(str(num), reverse=True)))


def main():
    assert descending_order(42145) == 54421
    assert descending_order(145263) == 654321
    assert descending_order(91872) == 98721

    assert descending_order2(42145) == 54421
    assert descending_order2(145263) == 654321
    assert descending_order2(91872) == 98721


if __name__ == '__main__':
    main()