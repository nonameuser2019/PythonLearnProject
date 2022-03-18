def any_duplicates(square):
    result = []
    for sub_list in square:
        for num in sub_list:
            result.append(num)
    return len(set(result)) != 9


def any_duplicates_2(square):
    result = [i for x in square for i in x]
    return len(set(result)) != 9


if __name__ == '__main__':
    test_set_1 = [[1, 2, 3], [4, 5, 6], [9, 7, 8]]
    test_set_2 = [[1, 1, 3], [6, 5, 4], [8, 7, 9]]
    assert any_duplicates(test_set_1) is False
    assert any_duplicates(test_set_2)

    assert any_duplicates_2(test_set_1) is False
    assert any_duplicates_2(test_set_2)
