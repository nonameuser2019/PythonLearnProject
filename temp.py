from datetime import datetime


def speed_checker(func):
    def wrapper(*args):
        time_start = datetime.now()
        for i in range(100000000):
            func(*args)
        time_finish = datetime.now()
        print(f'Function: {func.__name__} was finished for {time_finish - time_start}')
        return func(*args)

    return wrapper


@speed_checker
def find_shortest(word_list: list):
    return min(len(word) for word in word_list)


@speed_checker
def find_shortest_3(word_list: list):
    return min(map(len, word_list))


@speed_checker
def find_shortest_2(word_list: list):
    min_length = len(word_list[0])
    for word in word_list:
        if len(word) < min_length:
            min_length = len(word)
    return min_length

@speed_checker
def find_elem(data):
    return 3 in data

@speed_checker
def find_elem_2(x):
    if x == 1:
        return True
    elif x == 2:
        return True
    elif x == 3:
        return True


if __name__ == '__main__':
    assert find_shortest(['hello', 'hi', 'hey', 'yo', 'fuc']) == 2
    assert find_shortest_2(['hello', 'hi', 'hey', 'yo', 'fuc']) == 2
    assert find_shortest_3(['hello', 'hi', 'hey', 'yo', 'fuc']) == 2





