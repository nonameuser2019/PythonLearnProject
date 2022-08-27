def mymap(func, *seqs):
    result = []
    for args in zip(*seqs):
        result.append(func(*args))
    return result


def my_map_gen(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)


if __name__ == '__main__':
    data = [-2, 4, -1, 0, -81]
    data_2 = [[1, 2, 3], [2, 3, 4, 5]]
    print(mymap(abs, data))
    print(mymap(pow, *data_2))
    print(list(my_map_gen(abs, data)))
