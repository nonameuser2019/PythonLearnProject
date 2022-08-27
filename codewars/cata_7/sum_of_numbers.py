def get_sum(a, b):
    if b < a:
        a, b = b, a
    return sum(x for x in range(a, b + 1))


if __name__ == "__main__":
    assert get_sum(-1, 0) == -1
    assert get_sum(0, -1) == -1