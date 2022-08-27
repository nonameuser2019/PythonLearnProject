def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] and arr2[i] == arr1[i]:
            score += 4
        elif not arr2[i]:
            continue
        else:
            score -= 1
    return score if score > 0 else 0


def check_exam_1(arr1, arr2):
    pass


if __name__ == '__main__':
    assert check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]) == 6
    assert check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]) == 16
    assert check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]) == 7