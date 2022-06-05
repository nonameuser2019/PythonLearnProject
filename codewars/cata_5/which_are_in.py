def in_array(array1, array2):
    result = []
    for word in set(array1):
        for int_word in array2:
            if word in int_word:
                result.append(word)
                break
    return sorted(result)


if __name__ == '__main__':
    a1 = ["live", "arp", "strong", "arp"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp', 'live', 'strong']
    assert in_array(a1, a2) == r, in_array(a1, a2)